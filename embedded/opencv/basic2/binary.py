import cv2 as cv

img_gray = cv.imread("test.jpg", cv.IMREAD_GRAYSCALE)

# 대입 연산자
img_copy = img_gray

# img_gray와 img_copy는 같은 넘파이 배열을 가리킨다
# 같은 객체이므로 id 함수의 리턴 값이 같다
print(id(img_gray), id(img_copy))

# 아직은 똑같은 넘파이 배열을 가리키기 때문에
# img_gray에 선을 그으면 img_copy 에도 선이 그어진다
cv.line(img_gray, (10, 10), (100, 100), 0, 10)

# img_gray에 이진화를 적용하여 결과를 img_gray에 저장하면
# img_gray와 img_copy는 별개의 넘파이 배열을 가리키게 된다
ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# 다른 객체가 되므로 id 함수의 리턴값이 달라진다
print(id(img_gray), id(img_copy))

cv.line(img_gray, (0, 0), (200, 200), 0, 10)

# img_copy에는 영향을 주기 못하고 img_gray만 이진화 된다
cv.imshow("img_gray", img_gray)
cv.imshow("img_copy", img_copy)
cv.imwrite("newgray.jpg", img_gray)

cv.waitKey(0)
