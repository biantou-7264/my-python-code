import tkinter as tk
import pyautogui, sys
from time import time
from AppKit import NSCursor

a = 0
b = 0
zxcvb = True
root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
cx = w // 2
cy = h // 2


def aaaaa(debug=0):
    global w, h, zxcvb
    try:
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(cx, cy, duration=0)
        if zxcvb:
            NSCursor.hide()
    except:
        pass
    root.configure(bg='#000000')
    root.focus_force()
    root.attributes('-fullscreen', True)
    root.after(100, aaaaa)


def qwerty(debug=0):
    global a, b
    if b < 5 - 1:
        if time() - 1 <= 1:
            b = 0
        a = time()
        b += 1
    else:
        global zxcvb
        zxcvb = False
        NSCursor.unhide()
        root.destroy()
        sys.exit()


aaaaa()
root.bind('<Escape>', qwerty)
root.mainloop()
