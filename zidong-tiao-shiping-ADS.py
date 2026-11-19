# 发明者:biantou
#发明项目:自动跳广告
# 发明时间:2026年6月11日

import pyautogui as pag

print('程序已启动!')

try:
    while True:
        try:
            pos = pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/frameworks/视频号广告按钮.png', confidence=0.7)  # 获取是否有广告按钮
            print('检测到广告,即将跳过')
            pag.press('down')  # 跳过广告
            print('已跳过')
        except pag.ImageNotFoundException:  # 没有找到时会报这个错误
            pass  # 不用理会没有广告
        except Exception as e:
            print(e)
        pag.sleep(0.2)  # 防止cpu坏掉
except KeyboardInterrupt:
    print('程序已退出')