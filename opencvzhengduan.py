import cv2  
  
def check_camera():  
    print("=== 开始摄像头诊断 ===")  
      
    # 1. 检查OpenCV是否正常导入  
    print(f"1. OpenCV版本: {cv2.__version__}")  
      
    # 2. 尝试检测可用的摄像头索引  
    print("2. 扫描可用的摄像头...")  
    available_cameras = []  
    for i in range(5):  # 检查前5个摄像头索引  
        cap = cv2.VideoCapture(i)  
        if cap.isOpened():  
            available_cameras.append(i)  
            # 获取摄像头信息  
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  
            print(f"   - 摄像头 {i}: 可用 ({int(width)}x{int(height)})")  
            cap.release()  
        else:  
            print(f"   - 摄像头 {i}: 不可用")  
      
    if not available_cameras:  
        print("❌ 未找到任何可用的摄像头")  
        return False  
    else:  
        print(f"✅ 找到可用的摄像头: {available_cameras}")  
        return True  
  
# 运行诊断  
if check_camera():  
    print("\n摄像头硬件被检测到，现在测试画面获取...")  
      
    # 尝试打开第一个可用的摄像头  
    cap = cv2.VideoCapture(0)  
      
    if cap.isOpened():  
        print("正在尝试显示画面（按 'q' 键退出）...")  
          
        while True:  
            ret, frame = cap.read()  
              
            if not ret:  
                print("❌ 可以打开摄像头，但无法读取画面")  
                break  
                  
            # 显示画面  
            cv2.imshow('摄像头测试 - 按 q 退出', frame)  
              
            # 按q退出  
            if cv2.waitKey(1) & 0xFF == ord('q'):  
                break  
                  
        cap.release()  
        cv2.destroyAllWindows()  
    else:  
        print("❌ 摄像头打开失败")  
  
print("=== 诊断结束 ===")  
