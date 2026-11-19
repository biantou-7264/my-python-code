import subprocess as sp
from random import randint
from time import sleep

import pyautogui as pag

while True:
    for _ in range(2):
        sp.run("""osascript -e 'tell application "System Events" to tell appearance preferences to set dark mode to not dark mode'""", shell=True)
    for _ in range(10):
        pag.move(randint(-5, 5), randint(-5, 5))
