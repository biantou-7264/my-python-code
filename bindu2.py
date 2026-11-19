import pyautogui as pg
import tkinter as tk

root = tk.Tk()
root.geometry('0x0')
pg.FAILSAFE = False
pg.PAUSE = 0
w, h = pg.size()
cx, cy = w / 2, h / 2


def move(event):
    root.unbind('<Motion>')
    pg.moveTo(cx, cy)
    root.bind('<Motion>', move)


def focus():
    root.focus_force()
    root.after(20, focus)


root.bind('<Motion>', move)
root.focus_force()
focus()
root.mainloop()
