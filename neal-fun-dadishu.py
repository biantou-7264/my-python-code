from time import sleep

import pyautogui as pag

while True:
    try:
        x, y = pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/frameworks/1.png')
        pag.click(x, y)
        print('Clicked %s, %s' % (x, y))
    except pag.ImageNotFoundException:
        print('None')
    except KeyboardInterrupt:
        break

print('Quited')