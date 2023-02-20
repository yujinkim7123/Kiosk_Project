# mqtt 불러오기
import paho.mqtt.client as mqtt
import json

# insightface 불러오기
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# mqtt 콜백 함수 설정
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

# 새로운 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지 발행)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# address : localhost, port: 1883 에 연결
client.connect('localhost', 1883)
client.loop_start()

app = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
img = ins_get_image('t1')
faces = app.get(img)

client.publish('common', json.dumps({"connect" : "start"}), 1)

for i in range(len(faces)):
    face = faces[i]
    client.publish('common', json.dumps({
        "gender" : face.sex,
        "age" : face.age
    }), 1)

client.publish('common', json.dumps({"connect" : "end"}), 1)

client.loop_stop()
client.disconnect()