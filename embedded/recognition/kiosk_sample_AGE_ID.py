# COMMON lib
import sys
import os
import numpy as np
import cv2

# FaceAge lib
import logging
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# FACE ID lib
from person_db import Person
from person_db import Face
from person_db import PersonDB
import face_recognition
from datetime import datetime

# GPIO sensor lib
from gpiozero import DistanceSensor
from time import sleep
sensor = DistanceSensor(21, 20)  # Echo, Trig

# SYSTEMCALL lib

# FACE ID CLASS


class FaceClassifier():
    def __init__(self, threshold, ratio):
        self.similarity_threshold = threshold
        self.ratio = ratio

    def get_face_image(self, frame, box):
        img_height, img_width = frame.shape[:2]
        (box_top, box_right, box_bottom, box_left) = box
        box_width = box_right - box_left
        box_height = box_bottom - box_top
        crop_top = max(box_top - box_height, 0)
        pad_top = -min(box_top - box_height, 0)
        crop_bottom = min(box_bottom + box_height, img_height - 1)
        pad_bottom = max(box_bottom + box_height - img_height, 0)
        crop_left = max(box_left - box_width, 0)
        pad_left = -min(box_left - box_width, 0)
        crop_right = min(box_right + box_width, img_width - 1)
        pad_right = max(box_right + box_width - img_width, 0)
        face_image = frame[crop_top:crop_bottom, crop_left:crop_right]
        if (pad_top == 0 and pad_bottom == 0):
            if (pad_left == 0 and pad_right == 0):
                return face_image
        padded = cv2.copyMakeBorder(face_image, pad_top, pad_bottom,
                                    pad_left, pad_right, cv2.BORDER_CONSTANT)
        return padded

    # return list of dlib.rectangle
    def locate_faces(self, frame):
        # start_time = time.time()
        if self.ratio == 1.0:
            rgb = frame[:, :, ::-1]
        else:
            small_frame = cv2.resize(
                frame, (0, 0), fx=self.ratio, fy=self.ratio)
            rgb = small_frame[:, :, ::-1]
        boxes = face_recognition.face_locations(rgb)
        # elapsed_time = time.time() - start_time
        # print("locate_faces takes %.3f seconds" % elapsed_time)
        if self.ratio == 1.0:
            return boxes
        boxes_org_size = []
        for box in boxes:
            (top, right, bottom, left) = box
            left = int(left / ratio)
            right = int(right / ratio)
            top = int(top / ratio)
            bottom = int(bottom / ratio)
            box_org_size = (top, right, bottom, left)
            boxes_org_size.append(box_org_size)
        return boxes_org_size

    def detect_faces(self, frame):
        boxes = self.locate_faces(frame)
        if len(boxes) == 0:
            return []

        # faces found
        faces = []
        now = datetime.now()
        str_ms = now.strftime('%Y%m%d_%H%M%S.%f')[:-3] + '-'
        encodings = face_recognition.face_encodings(frame, boxes)
        for i, box in enumerate(boxes):
            face_image = self.get_face_image(frame, box)
            face = Face(str_ms + str(i) + ".png", face_image, encodings[i])
            face.location = box
            faces.append(face)
        return faces

    def compare_with_known_persons(self, face, persons):
        if len(persons) == 0:
            return None

        # see if the face is a match for the faces of known person
        encodings = [person.encoding for person in persons]
        distances = face_recognition.face_distance(encodings, face.encoding)
        index = np.argmin(distances)
        min_value = distances[index]
        if min_value < self.similarity_threshold:
            # face of known person
            persons[index].add_face(face)
            # re-calculate encoding
            persons[index].calculate_average_encoding()
            face.name = persons[index].name
            return persons[index]

    def compare_with_unknown_faces(self, face, unknown_faces):
        if len(unknown_faces) == 0:
            # this is the first face
            unknown_faces.append(face)
            face.name = "unknown"
            return

        encodings = [face.encoding for face in unknown_faces]
        distances = face_recognition.face_distance(encodings, face.encoding)
        index = np.argmin(distances)
        min_value = distances[index]
        if min_value < self.similarity_threshold:
            # two faces are similar - create new person with two faces
            person = Person()
            newly_known_face = unknown_faces.pop(index)
            person.add_face(newly_known_face)
            person.add_face(face)
            person.calculate_average_encoding()
            face.name = person.name
            newly_known_face.name = person.name
            return person
        else:
            # unknown face
            unknown_faces.append(face)
            face.name = "unknown"
            return None

    def draw_name(self, frame, face):
        color = (0, 0, 255)
        thickness = 2
        (top, right, bottom, left) = face.location

        # draw box
        width = 20
        if width > (right - left) // 3:
            width = (right - left) // 3
        height = 20
        if height > (bottom - top) // 3:
            height = (bottom - top) // 3
        cv2.line(frame, (left, top), (left+width, top), color, thickness)
        cv2.line(frame, (right, top), (right-width, top), color, thickness)
        cv2.line(frame, (left, bottom), (left+width, bottom), color, thickness)
        cv2.line(frame, (right, bottom),
                 (right-width, bottom), color, thickness)
        cv2.line(frame, (left, top), (left, top+height), color, thickness)
        cv2.line(frame, (right, top), (right, top+height), color, thickness)
        cv2.line(frame, (left, bottom),
                 (left, bottom-height), color, thickness)
        cv2.line(frame, (right, bottom),
                 (right, bottom-height), color, thickness)

        # draw name
        # cv2.rectangle(frame, (left, bottom + 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, face.name, (left + 6, bottom + 30), font, 1.0,
                    (255, 255, 255), 1)


new_order = 1
app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# main
while (True):
    # global new_order

    # print(sensor.distance)
    # dist of user to kiosk
    if (sensor.distance > 0.5):
        sleep(1)
        continue  # wait for dist <=5

    if (new_order):
        # kiosk mode num / 1:normal 2:easy
        mode = 0

        # user's face ID
        ID = 0

        print("WELCOME!!")

        # when man leave the kiosk
        reset = 0
        while (sensor.distance > 0.5 and reset < 10):
            reset += 1
            print("I'M WAITING FOR %d SEC" % reset)
            sleep(1000)

        if (reset == 10):
            print("NOBODY HERE I'M BACK")
            new_order = 1
            break

        # camera ON (ORDER START!)
        src = cv2.VideoCapture(0)
        ret2, frame2 = src.read()
        while frame2 is None:
            print("NOT FRAME")
            src.release()
            src = cv2.VideoCapture(0)
            ret2, frame2 = src.read()

        # check FACE ID
        import argparse
        import signal
        import time
        import os

        ap = argparse.ArgumentParser()
        ap.add_argument("inputfile",
                        help="video file to detect or '0' to detect from web cam")
        ap.add_argument("-t", "--threshold", default=0.44, type=float,
                        help="threshold of the similarity (default=0.44)")
        ap.add_argument("-S", "--seconds", default=1, type=float,
                        help="seconds between capture")
        ap.add_argument("-s", "--stop", default=0, type=int,
                        help="stop detecting after # seconds")
        ap.add_argument("-k", "--skip", default=0, type=int,
                        help="skip detecting for # seconds from the start")
        ap.add_argument("-d", "--display", action='store_true',
                        help="display the frame in real time")
        ap.add_argument("-c", "--capture", type=str,
                        help="save the frames with face in the CAPTURE directory")
        ap.add_argument("-r", "--resize-ratio", default=1.0, type=float,
                        help="resize the frame to process (less time, less accuracy)")
        args = ap.parse_args()

        src_file = args.inputfile
        if src_file == "0":
            src_file = 0

        # src = cv2.VideoCapture(0)
        if not src.isOpened():
            print("cannot open inputfile", src_file)
            src.release()
            exit(1)

        frame_width = src.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = src.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_rate = src.get(5)
        frames_between_capture = int(round(frame_rate * args.seconds))

        # print("source", args.inputfile)
        # print("original: %dx%d, %f frame/sec" % (src.get(3), src.get(4), frame_rate))
        ratio = float(args.resize_ratio)
        if ratio != 1.0:
            s = "RESIZE_RATIO: " + args.resize_ratio
            s += " -> %dx%d" % (int(src.get(3) * ratio),
                                int(src.get(4) * ratio))
            # print(s)
            # print("process every %d frame" % frames_between_capture)
            # print("similarity shreshold:", args.threshold)
            # if args.stop > 0:
            # print("Detecting will be stopped after %d second." % args.stop)

        # load person DB
        result_dir = "result"
        pdb = PersonDB()
        pdb.load_db(result_dir)
        pdb.print_persons()

        # prepare capture directory
        num_capture = 0
        if args.capture:
            # print("Captured frames are saved in '%s' directory." % args.capture)
            if not os.path.isdir(args.capture):
                os.mkdir(args.capture)

        # set SIGINT (^C) handler
        def signal_handler(sig, frame):
            global running
            running = False
        prev_handler = signal.signal(signal.SIGINT, signal_handler)
        # if args.display:
        # print("Press q to stop detecting...")
        # else:
        # print("Press ^C to stop detecting...")

        fc = FaceClassifier(args.threshold, ratio)
        frame_id = 0
        running = True

        total_start_time = time.time()
        USRID = ''
        while running:

            ret, frame = src.read()
            print("TAKE PICTURE")

            # if frame is None:
            #     print("NOT FRAME")
            #     src.release()
            #     src = cv2.VideoCapture(0)
            #     continue

            frame_id += 1
            if frames_between_capture != 0 and frame_id % frames_between_capture != 0:
                continue
            if frame_rate == 0:
                frame_rate += 1
            seconds = round(frame_id / frame_rate, 3)
            if args.stop > 0 and seconds > args.stop:
                src.release()
                break
            if seconds < args.skip:
                continue

            start_time = time.time()

            # this is core
            faces = fc.detect_faces(frame)
            for face in faces:
                person = fc.compare_with_known_persons(face, pdb.persons)
                if person:
                    continue
                person = fc.compare_with_unknown_faces(face, pdb.unknown.faces)
                if person:
                    pdb.persons.append(person)

            if args.display or args.capture:
                for face in faces:
                    fc.draw_name(frame, face)
                if args.capture and len(faces) > 0:
                    now = datetime.now()
                    filename = now.strftime('%Y%m%d_%H%M%S.%f')[:-3] + '.png'
                    pathname = os.path.join(args.capture, filename)
                    cv2.imwrite(pathname, frame)
                    num_capture += 1
                if args.display:
                    cv2.imshow("Frame", frame)
                    # imshow always works with waitKey
                    key = cv2.waitKey(1) & 0xFF
                    # if the `q` key was pressed, break from the loop
                    if key == ord("q"):
                        running = False

            elapsed_time = time.time() - start_time

            s = "\rframe " + str(frame_id)
            s += " @ time %.3f" % seconds
            s += " takes %.3f second" % elapsed_time
            s += ", %d new faces" % len(faces)
            s += " -> " + repr(pdb)
            if num_capture > 0:
                s += ", %d captures" % num_capture
            # print(s, end="    ")

            ##############################################################################
            # guess face age when (taging complete)
            if (len(faces) != 0):
                if (faces[0].name != 'unknown'):
                    USRID = faces[0].name
                    print("TAG COMPLETE")
                    age = 0
                    for i in range(3):
                        img = frame
                        faces = app.get(img)
                        # rimg = app.draw_on(img, faces)
                        if faces != []:
                            age += faces[0]['age']
                            print("AGE:", age)
                        else:
                            print("CAN NOT GUESS AGE")
                        ret, frame = src.read()
                        while ret == False:
                            ret, frame = src.read()
                    if age > 180:
                        mode = 2
                    else:
                        mode = 1
                    src.release()
                    break
            else:
                print("check")

            #####################################################################################

        # restore SIGINT (^C) handler
        signal.signal(signal.SIGINT, prev_handler)
        running = False
        src.release()
        total_elapsed_time = time.time() - total_start_time
        # print()
        # print("total elapsed time: %.3f second" % total_elapsed_time)

        pdb.save_db(result_dir)
        pdb.print_persons()

        # guess height
        height = 170

        # send data
        print("SENDING DATA MODE:%d , HEIGHT: %d, ID:%s" %
              (mode, height, USRID))

        # camera OFF
        src.release()
        new_order = 0

    # check recive message
    message = 0

    # check is ordering (wait 10 sec)
    if (message == 'END'):
        print("THE ORDER IS END")
        new_order = 1
        continue

    sleep(1)
    reset = 0
    while (sensor.distance > 0.5 and reset < 10):
        reset += 1
        print("I'M WAITING FOR %d SEC" % reset)
        sleep(1)

    if (reset == 10):
        print("NOBODY HERE I'M BACK")
        new_order = 1
        continue
