# PJT1-2

😵‍💫무과금을 위한 발버둥

---

[PJT1](https://www.notion.so/PJT1-8870f170ce39452f8e804bb186ba34df)

[프론트엔드](https://www.notion.so/eff5457a228942f88e2b2987672a2d4d)

[임베디드](https://www.notion.so/db917ad3a1894427aea6d3b5bb7577b1)

[회의](https://www.notion.so/e7f26811bf0949f08f451be85422b26c) 

[얼굴인식 키오스크 명세서](https://www.notion.so/cce0bec8f73140448c73758246a2d00a)

[](https://www.notion.so/b55e7ec9dd6142159917f711d12cf295) 

---

# 라즈베리 파이

### 라즈베리파이1 정보

- 와이파이
    - ID : SSAFY_802
    - PW : ssafy1357
    - IP : 70.12.246.141

### 라즈베리파이2 정보

## 라즈베리파이 설치 & 초기 설정

### SD카드에 OS 설치

- SD Card Formatter 실행
    - E 드라이브 포맷
- Raspberry Pi Imager
    - Raspberry Pi OS (32-bit) 선택
    - 설정
        - SSH 사용
            - 비밀번호 인증 사용
        - 사용자 이름 및 비밀번호 사용
            - 사용자 이름 : pi
            - 비밀번호 : raspberry
        - 무선 LAN 설정
        - 로케일 설정 지정
            - 시간대 : Asia/Seoul
            - 키보드 레이아웃 : us

### 초기 설정

- 시간대 설정
    - raspi-config 설정 방법
        
        ```bash
        sudo raspi-config
        ```
        
        <aside>
        💡 5 Localisation Options 선택
        L2 Timezone 선택
        Asia
        Seoul
        
        </aside>
        
    - 심볼릭 링크 재설정
        
        ```bash
        ls /usr/share/zoneinfo/Asia
        ```
        
        ```bash
        sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
        ```
        
        ```bash
        date
        ```
        
    - 수동 설정 명령어
        
        ```bash
        sudo date -s "Mon Sep 30 04:00:00 KST 2019"
        ```
        
- vim 설치
    - vim huge 버전 설치
        
        ```bash
        sudo apt-get install vim -y
        ```
        
    - .vimrc 설정
        
        ```bash
        vi ~/.vimrc
        ```
        
        ```bash
        if has("syntax")
            syntax on
        endif
        
        filetype plugin indent on
        
        set nu
        set title
        set ai
        set si
        set ts=4
        set shiftwidth=4
        set showmatch
        ```
        

### 원격 접속

- config 설정
    - Preference → Raspberry Pi Configuration → Interfaces
        - SSH
        - VNC
        - SPI
        - I2C
        - Serial Port
    - 위 토글 열고 OK
    - reboot

### OpenCV 설치

- OpenCV 설치 명령어
    
    ```bash
    sudo apt-get update
    ```
    
    ```bash
    sudo apt-get upgrade -y
    ```
    
    ```bash
    sudo apt-get install build-essential cmake pkg-config -y
    ```
    
    ```bash
    sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev -y
    ```
    
    ```bash
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
    ```
    
    ```bash
    sudo apt-get install libxvidcore-dev libx264-dev -y
    ```
    
    ```bash
    sudo apt-get install libfontconfig1-dev libcairo2-dev -y
    ```
    
    ```bash
    sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev -y
    ```
    
    ```bash
    sudo apt-get install libgtk2.0-dev libgtk-3-dev -y
    ```
    
    ```bash
    sudo apt-get install libatlas-base-dev gfortran -y
    ```
    
    ```bash
    sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103 -y
    ```
    
    ```bash
    sudo apt-get install python3-pyqt5 -y
    ```
    
    ```bash
    pip3 install imutils
    ```
    
    ```bash
    pip3 install opencv-contrib-python
    ```
    

### 파이 카메라 연결

- 카메라 설정 명령어
    
    파이 카메라를 연결한 후 라즈베리 파이를 부팅하여 명령어 실행
    
    ```bash
    sudo apt-get update
    ```
    
    ```bash
    sudo apt-get upgrade
    ```
    
    ```bash
    sudo raspi-config
    ```
    
    <aside>
    💡 3. Interface Options 선택
    I1 Legacy Camera 선택
    <예>
    <Finish>
    
    </aside>
    
    ```bash
    sudo reboot
    ```
    
- 카메라 테스트 명령어
    
    카메라 상단 sunny connector를 가리고 명령어 실행
    
    ```bash
    raspistill -o /home/pi/Desktop/image.jpg
    ```
    

### LiteFace - InsightFace with TensorFlow Lite

- InsightFace clone
    
    ```bash
    cd ~
    ```
    
    ```bash
    git clone https://github.com/deepinsight/insightface.git
    ```
    
    ```bash
    cd ./insightface/python-package/
    ```
    
    ```bash
    
    ```
    
- 학습 참고 자료
    - 파이썬을 이용한 라즈베리 파이 소켓 통신 :
        
        [라즈베리파이, PC로 소켓 통신을 해보자, 파이썬 버전](https://m.blog.naver.com/PostView.naver?blogId=zeta0807&logNo=222144886241&proxyReferer=https:%2F%2Fwww.google.com%2F)
        
    - 라즈베리 파이에서의 얼굴 인식
        
        [Face-Recognition-Raspberry-Pi-64-bits/README.md at main · Qengineering/Face-Recognition-Raspberry-Pi-64-bits](https://github.com/Qengineering/Face-Recognition-Raspberry-Pi-64-bits/blob/main/README.md)
        

[라즈베리파이_서브](https://www.notion.so/_-16a96bf98c93455a893ade762f605b65)

# **InsightFace**

## 참고 자료

### 공식 웹페이지

- 홈페이지
    
    [InsightFace](https://insightface.ai/)
    
- 깃허브
    
    https://github.com/deepinsight/insightface
    

### 비공식 자료

- 논문 리뷰
    
    [[논문리뷰] 내 마음대로 ArcFace 논문 리뷰](https://butter-shower.tistory.com/237)
    
- 샘플 코드
- 유사 프로젝트
    
    [https://github.com/SharpAI/DeepCamera](https://github.com/SharpAI/DeepCamera)
    

## InsightFace 설치 & 초기 설정

### InsightFace 설치

- 파이썬 버전 3.10 이하 설치
- numpy 버전 1.23 이하 설치
- 설치 명령어
    
    ```bash
    pip install -U insightface
    ```
    
- 오류
    - No module named 'onnxruntime’
        
        ```bash
        pip install onnxruntime
        ```
        
    - module 'numpy' has no attribute 'int'. Did you mean: 'inf'?
        
        ```bash
        pip list
        ```
        
        ```bash
        pip install numpy==1.23.5
        ```
        
    - ‘version_info’ object has no attribute ‘__version__’
        
        ```cpp
        pip show pyparsing
        ```
        
        ```cpp
        pip install pyparsing==2.4.7
        ```
        

### InsightFacePaddle 설치

- 공식 깃허브
    
    [https://github.com/littletomatodonkey/insight-face-paddle](https://github.com/littletomatodonkey/insight-face-paddle)
    
- 설치 명령어
    
    ```bash
    pip3 install paddlepaddle-gpu
    pip3 install paddlepaddle
    ```
    

### Paddle-lite

[](https://qengineering.eu/install-paddle-lite-on-raspberry-pi-4.html)

[built-onnxruntime-for-raspberrypi-linux/BUILD.md at master · nknytk/built-onnxruntime-for-raspberrypi-linux](https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux/blob/master/BUILD.md)

[MQTT (1)](https://www.notion.so/MQTT-1-9e64f51e1976481a9c3a746dd4f9c8a1)

[HTTP (1)](https://www.notion.so/HTTP-1-82de3205618a4941ace5d25704825bef)

[DATA (1)](https://www.notion.so/DATA-1-8e454b64d65a4acba9fa2ff76c569369)

[Tensorflow Lite (1)](https://www.notion.so/Tensorflow-Lite-1-8bb959beaa474b8e8360cc269c41f74e)

[라즈베리파이_서브 (1)](https://www.notion.so/_-1-d67b87ded6774ea8a2619205c93a3a03)

[웹앱 (1)](https://www.notion.so/1-197522cd90fe4d3c9bf75cb6d35660b7)

[Docker (1)](https://www.notion.so/Docker-1-31208d3e50d245f29edc59764bbf86f1)

---

[Socket](https://www.notion.so/Socket-efb22ac54565474495536948fc33976a)

[초음파 센서 케이스](https://www.notion.so/058139bcee8b41b28a33b40349ed765d)

[포팅 메뉴얼](https://www.notion.so/67f3d8589b8e43278c07a9c5612d4864)

[발표 대본](https://www.notion.so/b0723e7d5b6f4e43a7fc76e7ce3f4b48)