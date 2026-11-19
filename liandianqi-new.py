import threading
from time import sleep
import pyautogui as pag
from pynput import keyboard
import pyttsx3

r, nlt, nrt = False, False, False
speed = 0.05
pag.FAILSAFE = False
pag.PAUSE = 0


def speak(text):
    def task():
        engine = pyttsx3.init()
        engine.setProperty('rate', 500)
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=task, daemon=True)
    thread.start()


def s(k):
    global r, nlt, nrt
    if k == keyboard.Key.alt:
        if not r:
            r = True
        else:
            r = False
    if k == keyboard.Key.esc:
        r = False
    if k == keyboard.Key.left:
        nlt = True
    if k == keyboard.Key.right:
        nrt = True


l = keyboard.Listener(on_press=s)
l.start()

while True:
    if r:
        pag.click()
    if nlt:
        speed -= 0.01
        speed = round(speed, 2)
        nlt = False
        print('speed:', speed)
        speak('speed: %.2f' % speed)
    if nrt:
        speed += 0.01
        speed = round(speed, 2)
        nrt = False
        print('speed:', speed)
        speak('speed: %.2f' % speed)
    if speed > 0:
        sleep(speed)
    if not r:
        sleep(0.2)
