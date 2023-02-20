import cv2 as cv

# 카메라에서 이미지를 캡처하기 위해서는 VideoCapture 객체를 생성하여
# 카메라와 연결해야 한다. 카메라 인덱스를 아규먼트로 사용한다.
# PC 에 처음 연결한 카메라 인덱스는 0,
# 2번째로 연결한 카메라 인덱스는 1...
# 이런 식으로 PC에 카메라를 연결한 순서에 맞추어
# 카메라에 접근할 때 사용하는 인덱스가 부여된다.
cap = cv.VideoCapture(0)

# 카메라와 성공적으로 연결되어있느지 체크한다
if cap.isOpened() == False:
    print("카메라를 열 수 없다.")
    exit(1)

# 카메라에서 이미지 캡쳐와 윈도우에 이미지 보여주는 것을 반복하면
# 동영상처럼 보이게 된다
while (True):

    # 카메라에서 이미지를 읽어옵니다.
    ret, img_frame = cap.read()

    # ret 리턴값이 False이면 캡처가 실패한 것이다.
    if ret == False:
        print("캡처 실패")
        break

    # 캡처된 이미지를 윈도우에 보여준다.
    cv.imshow('Color', img_frame)

    # 사용자의 키보드 입력을 1ms 동안 기다렸다가
    # 다음 줄에 실행한다.
    key = cv.waitKey(1)

    # ESC 키가 입력되었다면 반복을 중지한다.
    if key == 27:
        break

# 사용이 끝난 카메라와 연결을 종료한다.
cap.release()
cv.destroyAllWindow()
