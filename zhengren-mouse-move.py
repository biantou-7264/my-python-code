try:
    import pyautogui as pag
except ImportError:
    import subprocess as sp
    import sys

    print('正在为您安装pyautogui...')
    name = 'pyautogui'
    command = [sys.executable, '-m', 'pip', 'install', name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple']
    sp.run(command)
    import pyautogui as pag

    del sp
    del name
    del command
    del sys
from random import randint

pag.PAUSE = 0
pag.FAILSAFE = False
w, h = pag.size()

print('程序已启动')
try:
    while True:
        print('开始')
        for i in range(200):
            pag.move(randint(-1, 1), randint(-1, 1))
        for i in range(30, -1, -1):
            print(i)
            pag.sleep(1)
except KeyboardInterrupt:
    print('已退出')
except BaseException as e:
    print(type(e).__name__)
    print(e)
