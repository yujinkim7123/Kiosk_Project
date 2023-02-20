# 임의의 각도와 높이를 입력한 키 계산 프로그램
# 얼굴 인식 후 화면상의 얼굴 위치 계산 (단위 : %)
# 얼굴 위치를 바탕으로 키 계산
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

app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

cap = cv2.VideoCapture(0)

h_cap = 140  # 카메라 높이
theta_cap = 0  # 카메라 설치 각도 (정면이 0도)
angle_cap = 90  # 카메라 화각 (위아래로 촬영 가능한 총 각도)
d = 50  # 카메라와 피사체의 거리 (초음파 센서 값)

if cap.isOpened() == False:
    print("Can't open camera")
    exit(1)

while True:
    ret, img = cap.read()
    if ret is None:
        print("Can't read camera")
        break

    y_max, x_max, channel = img.shape
    # print("y_max :", y_max)

    faces = app.get(img)
    if len(faces) == 0:
        print("Can't find faces")
        continue

    rimg = app.draw_on(img, faces)

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
