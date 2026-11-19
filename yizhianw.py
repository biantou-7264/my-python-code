import pyautogui as pg
from time import sleep
pg.PAUSE=0.1
try:
    sleep(3)
    pg.keyDown('w')
    while True:
        pg.keyDown('w')
except:
    pg.keyUp('w')
    print('keyup')
