from pynput import keyboard
from time import sleep
def r(k):
    print(k)
with keyboard.Listener(on_press=r) as l:
    l.join()