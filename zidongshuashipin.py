from pyautogui import press
from time import sleep

try:
    while True:
        press('down')
        sleep(0.1)
except KeyboardInterrupt:
    print('已退出程序')
