import cv2

img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
	print("cannot read image file")
	exit(1)

cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()