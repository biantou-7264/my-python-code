from traceback import format_exc

import cv2
import pyttsx3 as tts
from deepface import DeepFace

# 启动 TTS 引擎
tts_engine = tts.init()

# 打开 Mac 摄像头
print('正在打开摄像头...')
cap = cv2.VideoCapture(0)

test_count = 0
weight = '未知'

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        if test_count % 50 == 0:
            # 分析当前帧画面
            print('分析画面中...')

            results = DeepFace.analyze(frame, actions=['gender'], enforce_detection=False, expand_percentage=20, align=True)

            for face in results:
                # 获取坐标
                x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
                gender = face['dominant_gender']
                prob = face['gender'][gender]
                if prob < 74:
                    gender = 'Woman'
                print('dominant_gender:', gender)
                print('prob:', prob)

                # 显示体重
                if gender == 'Man':
                    weight = '59斤'
                else:
                    weight = '200斤'

                print('已更新')
        test_count += 1
        cv2.rectangle(frame, (80, 60), (200, 130), (0, 0, 0), -1)
        cv2.putText(frame, weight, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        # 没检测到脸的时候 DeepFace 会抛异常，直接跳过
        print(format_exc())
        cv2.rectangle(frame, (80, 60), (200, 130), (0, 0, 0), -1)
        cv2.putText(frame, '未知', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('体重检测器', frame)

    key = cv2.waitKey(1)
    # 按 q 退出
    if key & 0xFF == ord('q'):
        print('exiting...')
        break
    # 按 ESC 退出
    if key & 0xFF == 27:
        print('exiting...')
        break
    # 按 s 朗读
    if key & 0xFF == ord('s'):
        print('saying...')
        try:
            tts_engine.say(weight)
            tts_engine.runAndWait()
        except NameError:
            pass

cap.release()
cv2.destroyAllWindows()
print('退出成功')