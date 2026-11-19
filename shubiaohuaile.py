import pyautogui as pg
pg.sleep(1)
pg.PAUSE=0
try:
    while True:
        pg.click()
        pg.sleep(0.02)
except pg.FailSafeException:
    print('已终止程序')
