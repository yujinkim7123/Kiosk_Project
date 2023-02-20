import cv2 as cv

# 사람이 없을 때 이미지 background.png와
# 사람이 있을 때 이미지 object.png를 불러온다.
img_background = cv.imread('background.jpg', cv.IMREAD_GRAYSCALE)
img_object = cv.imread('object.jpg', cv.IMREAD_GRAYSCALE)

# 사람이 있는 이미지 img_object에서
# 사람이 없는 이미지 img_background를 빼서 차영상을 얻는다
# 빼는 순서는 바꾸면 안된다
img_sub = cv.subtract(img_object, img_background)

# 차영상을 이진화한다
retval, img_binary = cv.threshold(img_sub, 50, 255, cv.THRESH_BINARY)

cv.imshow('background', img_background)
cv.imshow('object', img_object)
cv.imshow('sub', img_sub)
cv.imshow('binary', img_binary)
cv.waitKey(0)
