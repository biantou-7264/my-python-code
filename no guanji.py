import pyautogui as pg
pg.FAILSAFE=False
while True:
    x,y=pg.position()
    if x<40 and y<40:
        pg.moveTo(50,50)
    pg.sleep(0.1)