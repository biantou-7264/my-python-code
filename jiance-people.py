import cv2
import pyautogui as pag

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    boxes, _ = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.05)

    if len(boxes) > 1:
        pag.hotkey('command', 'h', interval=0.2)
    print(len(boxes))
    if cv2.waitKey(1) & 0xFF == 27: break

cv2.destroyAllWindows()
cap.release()
