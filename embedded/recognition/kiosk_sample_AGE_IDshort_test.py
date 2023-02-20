# COMMON lib
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
import math

# GPIO sensor lib
from gpiozero import DistanceSensor
from time import sleep
sensor = DistanceSensor(21,20) # Echo, Trig

# SYSTEMCALL lib
import os
import sys

# socketio
import socketio
sio = socketio.Client()
sio.connect('http://3.36.49.220:4001')

order_end = 0

# listen message from front
@sio.on('react')
def on_message(data):
    global order_end
    order_end = data
    print(data)

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
        #start_time = time.time()
        if self.ratio == 1.0:
            rgb = frame[:, :, ::-1]
        else:
            small_frame = cv2.resize(frame, (0, 0), fx=self.ratio, fy=self.ratio)
            rgb = small_frame[:, :, ::-1]
        boxes = face_recognition.face_locations(rgb)
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

new_order = 1
app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
h_cap = 140  # 카메라 높이
theta_cap = 0  # 카메라 설치 각도 (정면이 0도)
angle_cap = 90  # 카메라 화각 (위아래로 촬영 가능한 총 각도)
# main
while(True):

    # dist of user to kiosk
    if(sensor.distance>0.5): 
        sleep(1)
        continue  # wait for dist <=5

    if(new_order):
        #new order start
        order_end = 0

        # kiosk mode num / 1:normal 2:easy
        mode = 0

        # user's face ID
        ID = 0

        print("WELCOME!!")
        
        # when man leave the kiosk
        reset = 0
        while(sensor.distance>0.5 and reset<10):
            reset += 1
            print("I'M WAITING FOR %d SEC" %reset)
            sleep(1000)
        
        if(reset==10):
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

        #src = cv2.VideoCapture(0)
        if not src.isOpened():
            print("cannot open inputfile", src_file)
            src.release()
            exit(1)

        frame_width = src.get(cv2.CAP_PROP_FRAME_WIDTH)
        frame_height = src.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_rate = src.get(5)
        frames_between_capture = int(round(frame_rate * args.seconds))

        ratio = float(args.resize_ratio)
        if ratio != 1.0:
            s = "RESIZE_RATIO: " + args.resize_ratio
            s += " -> %dx%d" % (int(src.get(3) * ratio), int(src.get(4) * ratio))

        # load person DB
        result_dir = "result"
        pdb = PersonDB()
        print('hi')
        pdb.load_db(result_dir)
        # pdb.print_persons()
        print('hey')
        # prepare capture directory
        num_capture = 0
        if args.capture:
            #print("Captured frames are saved in '%s' directory." % args.capture)
            if not os.path.isdir(args.capture):
                os.mkdir(args.capture)

        # set SIGINT (^C) handler
        def signal_handler(sig, frame):
            global running
            running = False
        prev_handler = signal.signal(signal.SIGINT, signal_handler)
    
        fc = FaceClassifier(args.threshold, ratio)
        frame_id = 0
        running = True

        total_start_time = time.time()
        USRID =''
        while running:

            ret, frame = src.read()
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            print("TAKE PICTURE")

            frame_id += 1
            if frames_between_capture!=0 and frame_id % frames_between_capture != 0:
                continue
            if frame_rate == 0:
                frame_rate+=1
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
                if args.capture and len(faces) > 0:
                    now = datetime.now()
                    filename = now.strftime('%Y%m%d_%H%M%S.%f')[:-3] + '.png'
                    pathname = os.path.join(args.capture, filename)
                    cv2.imwrite(pathname, frame)
                    num_capture += 1

            elapsed_time = time.time() - start_time

            ##############################################################################
            # guess face age when (taging complete)
            if(len(faces)!=0):
                if(faces[0].name != 'unknown'):
                    USRID = faces[0].name
                    print("TAG COMPLETE")
                    age = 0
                    for i in range(1):
                        img = frame
                        faces = app.get(img)
                        #rimg = app.draw_on(img, faces)
                        if faces != []:
                            age += faces[0]['age']
                            print("AGE:",age)
                        else: print("CAN NOT GUESS AGE")
                        ret, frame = src.read()
                        while ret==False:
                            ret, frame = src.read()
                    if age>180:
                        mode = 2
                    else:
                        mode = 1
                    # 임의의 각도와 높이를 입력한 키 계산 프로그램
                    # 얼굴 인식 후 화면상의 얼굴 위치 계산 (단위 : %)
                    # 얼굴 위치를 바탕으로 키 계산
                    # 동영상에 키 출력
                    d = sensor.distance * 100  # 카메라와 피사체의 거리 (초음파 센서 값)

                    y_max, x_max, channel = img.shape

                    face = faces[0]
                    box = face.bbox.astype(np.int)
                    y_top = box[1]
                    y_btm = box[3]
                    y_mid = (y_btm + y_top)/2

                    theta = angle_cap*(0.5 - (float(y_mid)/float(y_max))) + theta_cap
                    h = h_cap + d*math.tan(math.radians(theta))
                    print("height :", h, "tan :", math.tan(math.radians(theta)))

                    break

            else : print("check")

            #####################################################################################

        # restore SIGINT (^C) handler
        signal.signal(signal.SIGINT, prev_handler)
        running = False
        total_elapsed_time = time.time() - total_start_time
        #print()
        #print("total elapsed time: %.3f second" % total_elapsed_time)

        pdb.save_db(result_dir)
        pdb.print_persons()

        # guess height
        height = 170

        # booting web with mode

        #send data
        sio.emit('pi',mode)
        print("SEND COMPLETE")
        
        # camera OFF
        src.release()
        new_order = 0

    # check is ordering (wait 5 sec)
    if(order_end):
        print("THE ORDER IS END")
        order_end = 0
        new_order = 1
        continue
    
    sleep(1)
    reset = 0
    while(sensor.distance>0.5 and reset<10):
        reset += 1
        print("I'M WAITING FOR %d SEC" %reset)
        sleep(1)
    
    if(reset==5):
        print("NOBODY HERE I'M BACK")
        new_order = 1
        continue
sio.disconnect()