# 임베디드 파트 주요 설정

## InsightFace

### face_analysis.py 파일 수정

    ```python
    def get(self, img, max_num=0):
    ```
    ↓
    ```python
    def get(self, img, max_num=1):
    ```
