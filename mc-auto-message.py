import pyautogui as pg
from time import sleep
sleep(5)
while True:
    for i in range(1,10+1):
        pg.write(str(i))