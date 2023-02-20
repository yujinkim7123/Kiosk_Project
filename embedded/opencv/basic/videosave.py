import cv2 as cv

cap = cv.VideoCapture(0)

# 카메라와 성공적으로 연결되어있느지 체크한다
if cap.isOpened() == False:
    print("카메라를 열 수 없다.")
    exit(1)

# 캡처된 이미지의 크기를 확인하기 위해 이미지 1장을 캡처한다
ret, img_frame = cap.read()

if ret == False:
    print("캡처 실패")
    exit(1)

# 동영상 파일을 위한 코덱을 설정한다
codec = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')

# 프레임 레이드(Frame rate)를 설정한다
fps = 30.0

# 이미지 크기를 가져온다
h, w = img_frame.shape[:2]

# 동영상 파일을 저장하려면 VideioWriter 객체를 생성해야 한다
# VideoWriter 객체를 초기화하기 위해 저장할 동영상 파일 이름,
# 코덱, 프레임 라이트, 이미지 크기를 지정합니다.
writer = cv.VideoWriter("output.avi", codec, fps, (w, h))

# VideioWriter 객체를 성공적으로 초기화했는지 체크한다
if writer.isOpened() == False:
    print("no video")
    exit(1)

# ESC 키 입력전까지 카메라가 찍은 이미지가 동영상으로 저장된다
while (True):
    ret, img_frame = cap.read()

    if ret == False:
        print("캡처 실패")
        break

    writer.write(img_frame)

    cv.imshow('Color', img_frame)

    key = cv.waitKey(1)

    # ESC 키가 입력되었다면 반복을 중지한다.
    if key == 27:
        break

# 사용이 끝난 카메라와 연결을 종료한다.
cap.release()

# 동영상 저장을 완료하기 위해 VideoWriter 객체를 릴리즈 한다.
writer.release()

cv.destroyAllWindow()
