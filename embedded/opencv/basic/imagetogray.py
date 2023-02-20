# 필요한 OpenCV 패키지 임포트
import cv2

# 이미지 불러오기
img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다")
    exit(1)

cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

# 대기하다가 키보드 입력이 있으면 다음 줄 실행
cv2.waitKey(0)

# 그레이 스케일

# img_color 에 저장된 컬러 이미지를 그레이 스케일 이미지로 변환 후
# img_gray 에 대입
# COLOR_BGR2GRAY 는 BGR 채널을 가진 컬러 이미지를 그레이 스케일로
# 변환하겠다고 지정한다
img_gray = cv2.cvtcolor(img_color, cv2.COLOR_BGR2GRAY)

# namedWindow 함수 생략 가능
# img_gray 에 저장된 그레이 스케일 이미지를 식별자가 "Grayscale"인
# 창에 보여준다
# 첫 번째 아규먼트를 앞에서 컬러 이미지 보여줄 때 사용한 "Color"를
# 사용하도록 수정하면 그레이 스케일 이미지가 "Color"창에 보이게 된다
cv2.imshow('Grayscale', img_gray)

# img_gray 에 저장된 이미지를 첫 아규먼트로 지정한 파일로 저장
# 이미지 포맷은 지정한 파일의 확장자에 따라 결정된다
cv2.imwrite("grayscale.jpg", img_gray)

# 사용이 끝난 윈도우를 종료해준다
# 아무 키나 누르면 프로그램이 종료된다.
cv2.waitKey(0)
cv2.destroyAllWindow()
