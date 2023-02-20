# 임의의 각도와 높이를 입력한 키 계산 프로그램
# 얼굴 인식 후 화면상의 얼굴 위치 계산 (단위 : %)
# 초음파 센터로 거리 계산
# 얼굴 위치와 거리를 바탕으로 키 계산
# 동영상에 키 출력

# COMMON lib
import numpy as np
import cv2
import math

# FaceAge lib
import logging
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# GPIO sensor lib
from gpiozero import DistanceSensor
from time import sleep
sensor = DistanceSensor(21, 20)  # Echo, Trig

app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

cap = cv2.VideoCapture(0)

h_cap = 162  # 카메라 높이
theta_cap = 0  # 카메라 설치 각도 (정면이 0도)
angle_cap = 120  # 카메라 화각 (위아래로 촬영 가능한 총 각도)

if cap.isOpened() == False:
    print("Can't open camera")
    exit(1)

while True:

    d = sensor.distance * 100  # cm 단위
    if d > 75:
        sleep(10)
        continue

    ret, img = cap.read()
    if ret is None:
        print("Can't read camera")
        break

    img90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    y_max, x_max, channel = img90.shape
    # print("y_max :", y_max)

    faces = app.get(img90)
    if len(faces) == 0:
        print("Can't find faces")
        continue

    rimg = app.draw_on(img90, faces)

    for i in range(len(faces)):
        face = faces[i]
        box = face.bbox.astype(np.int)
        y_top = box[1]
        y_btm = box[3]
        y_mid = (y_btm + y_top)/2
        # print("top :", y_top, "bottom :", y_btm, "middle :", y_mid)
        # cv2.putText(rimg, '%d %s' % (y_mid, "px"), (box[0]+70, box[1]-4), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 1)

        theta = angle_cap*(0.5 - (float(y_mid)/float(y_max))) + theta_cap
        h = h_cap + d*math.tan(math.radians(theta))
        print("theta :", theta, "tan :", math.tan(math.radians(theta)))
        cv2.putText(rimg, '%d %s' % (
            h, "cm"), (box[0] + 70, box[1]-4), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 1)

    cv2.imshow("rimg", rimg)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindow()
