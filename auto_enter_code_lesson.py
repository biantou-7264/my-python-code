import pyautogui as pg
import tkinter as tk
from datetime import datetime


def start_bcm():
    pg.click(575, 922)


def wait():
    now = datetime.now()
    hour, minute, second = now.hour, now.minute, now.second
    running.set('当前运行中,time=%d:%d:%d' % (hour, minute, second))
    if hour == 19 and minute == 00 and second > 7 and second < 10:
        pg.click(812, 214)
        pg.sleep(2)
        pg.click(718, 703)
        pg.sleep(1)
        pg.click(507, 293)
    root.after(100, wait)


root = tk.Tk()
root.title('自动上编程课')
run = 0
running = tk.StringVar(value='当前正在等待进程')

tk.Label(root, text='程序已初始化完成,将在19:00时进入编程课!', font=('Arial', 40)).pack(padx=10, pady=10)
tk.Label(root, textvariable=running, font=('Arial', 30)).pack(padx=10, pady=10)
tk.Button(root, text='我知道了,最小化窗口', font=('Arial', 40), command=root.iconify).pack(padx=10, pady=10)

root.protocol('WM_DELETE_WINDOW', root.iconify)
root.focus_force()
root.after(500, start_bcm)
root.after(3000, wait)
root.mainloop()
