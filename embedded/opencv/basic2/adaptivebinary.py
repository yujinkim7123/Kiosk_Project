import cv2 as cv
import sys

# 이미지를 읽어옵니다
img_color = cv.imread("test.jpg", cv.IMREAD_COLOR)
if img_color is None:
    print("no image file")
    sys.exit(1)

# 그레이 스케일 이미지로 변환한다
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

# 그레이 스케일 이미지에 적응형 이진화를 적용한다
img_binary = cv.adaptiveThreshold(
    img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 4)

# 결과 이미지를 보여준다
cv.imshow('Grayscale', img_gray)
cv.imshow('Binary', img_binary)
cv.waitKey(0)
