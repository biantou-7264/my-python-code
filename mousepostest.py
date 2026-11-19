import pyautogui as pg

while True:
    x, y = pg.position()
    print('\r x:%.2f  y:%.2f            ' % (x, y), end='')
