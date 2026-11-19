print('欢迎使用Loop刷环绕次数工具! ^_^')
print('初始化中...', end='', flush=True)

import pyautogui as pag
import traceback as tb

pag.PAUSE = 0.01
pag.FAILSAFE = True

print('\r初始化完成!', end='', flush=True)
print('')

try:
    print('请在3秒内切换至Loop')
    print('鼠标甩到边缘即可停止')
    pag.sleep(3)
    print('开始!')

    while True:
        pag.hotkey('command', 'space')
except KeyboardInterrupt:
    print('已停止!')
except pag.FailSafeException:
    print('已停止!')
except Exception:
    print('出错了')
    print(tb.format_exc())
