import pyautogui as pg

pg.PAUSE = 0
pg.sleep(0.5)

for i in range(2):
    pg.press('right')
    pg.press('right')
    pg.press('left')