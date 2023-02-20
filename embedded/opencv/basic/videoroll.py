import cv2 as cv

# VideoCapture의 아규먼트로 불러올 동영상 파일 이름을 사용한다
cap = cv.VideoCapture("output.avi")

if cap.isOpened() == False:
    print("can't open the video")
    exit(1)

while (True):
    ret, img_frame = cap.read()

    # 동영상 끝까지 재생하면 read 함수는 False를 리턴한다
    if ret == False:
        print("done")
        break

    cv.imshow('Color', img_frame)

    # 동영상 재생 속도를 조정하기 위해 waitKey 함수의 아규먼트로 25ms 설정
    key = cv.waitKey(25)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
