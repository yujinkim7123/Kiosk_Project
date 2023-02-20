# 필요한 OpenCV 패키지 임포트
import cv2

# 첫 번째 아규먼트로 지정한 파일을 컬러 포맥으로 불러온다.
# IMREAD_COLOR는 컬러 포맷으로 영상을 읽겠다는 의미
# 이미지를 img_color 변수에 넘파이 배열로 대입한다.
img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

# 이미지를 불러올 수 없으면 img_color 변수는 None(값없음)이 된다.
# 이미지를 불러올 수 없는 경우를 체크하기 위해 사용한다.
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다")
    exit(1)

# 이미지를 보여줄 윈도우 생성
# 첫 번째 아규먼트로 윈도우 식별자로 사용할 문자열을 지정해준다.
# 지정한 문자열이 윈도우의 타이틀바에 보이게 된다.
cv2.namedWindow('Color')

# 윈도우 식별자가 "Color" 인 윈도우에 변수 img_color가 가리키는
# 넘파이 배열에 저장된 이미지를 보여준다
# 대부분의 경우 namedWindows를 생략하고 imshow 만 사용해도
# 윈도우에 이미지를 보여준다
# -> namedWindow를 사용하지 않을 경우 'Color' 생략
cv2.imshow('Color', img_color)

# ms 단위로 지정한 시간만큼 대기한다
# 0이면 OpenCV로 생성한 윈도우 창이 선택된 상태에서
# 키보드 입력이 있을 때까지 대기 한다
cv2.waitKey(0)

# 사용이 끝난 윈도우를 종료해준다
cv2.destroyAllWindow()
