import cv2  
import os
  
# 创建保存照片的文件夹  
if not os.path.exists('photos'):  
    os.makedirs('photos')  
  
cap = cv2.VideoCapture(0)  
photo_count = 0  
  
while True:  
    ret, frame = cap.read()  
    if not ret:
        print('开启失败')
        break  
      
    # 显示画面  
    cv2.imshow('摄像头', frame)  
      
    key = cv2.waitKey(1) & 0xFF  
      
    if key == ord('z'):  # 按z退出  
        break  
    elif key == ord('x'):  # 按x拍照  
        photo_count += 1  
        filename = f'photos/photo_{photo_count}.jpg'  
        cv2.imwrite(filename, frame)  
        print(f'照片已保存: {filename}')
cap.release()  
cv2.destroyAllWindows()  
