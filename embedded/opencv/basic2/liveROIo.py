import cv2 as cv

mouse_is_pressing = False
start_x, start_y, end_x, end_y = 0, 0, 0, 0
step = 0


def swap(v1, v2):
    temp = v1
    v1 = v2
    v2 = temp

# 마우스 왼쪽 버튼을 누르면 ROI 시작점이 되고
# 마우스 왼쪽 버튼을 떼면 ROI 끝점이 된다
# 마우스 이동 시 ROI 영역을 초록색 사각형으로 보여준다


def mouse_callback(event, x, y, flags, param):

    global step, start_x, start_y, end_x, end_y, mouse_is_pressing
    if event == cv.EVENT_LBUTTONDOWN:
        step = 1

        mouse_is_pressing = True
        start_x = x
        start_y = y

    elif event == cv.EVENT_MOUSEMOVE:

        # 마우스를 누른 상태이면 현재 마우스 커서 위치를
        # ROI 끝점을 저장하여 현재 선택된 ROI 영역을 보여주도록 한다
        if mouse_is_pressing:
            end_x = x
            end_y = y
            step = 2
    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing = False
        end_x = x
        end_y = y
        step = 3


cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("can't open camera")
    exit(-1)

cv.namedWindow("Color")
cv.setMouseCallback("Color", mouse_callback)

while True:
    ret, img_color = cap.read()
    if ret == False:
        print("capture failed")
        break

    if step == 1:
        cv.circle(img_color, (start_x, start_y), 10, (0, 255, 0), -1)

    elif step == 2:
        # 왼쪽 버튼을 누른 채 움직이고 있는 영역을 초록색 사각형으로 보여준다
        cv.rectangle(img_color, (start_x, start_y),
                     (end_x, end_y), (0, 255, 0), 3)

    elif step == 3:
        if start_x >= end_x:
            start_x, end_x = end_x, start_x

        if start_y >= end_y:
            start_y, end_y = end_y, start_y

        # 마우스 왼쪽 버튼에서 손을 떼고 나서 ROI를 지정한다
        # ROI 는 다음처럼 지정한다
        # 시작점 y좌표:끝점 y좌표, 시작점 x좌표:끝점 x좌표
        ROI = img_color[start_y:end_y, start_x:end_x]
        # 그레이 스케일로 변환하여 에지를 검출한 후, 다시 컬러 이미지로 변환한다
        # 원본 이미지가 컬러 영상이라 복사하려면 컬러로 변환해줘야 한다
        ROI = cv.cvtColor(ROI, cv.COLOR_BGR2GRAY)
        ROI = cv.Canny(ROI, 150, 50)
        ROI = cv.cvtColor(ROI, cv.COLOR_GRAY2BGR)

        # 원본 영상에 ROI 영역을 복사한다
        img_color[start_y:end_y, start_x:end_x] = ROI

    cv.imshow("Color", img_color)

    if cv.waitKey(25) > 0:
        break
