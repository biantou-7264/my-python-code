import pyautogui as pg
from random import randint
from time import sleep
import tkinter as tk

try:
    root = tk.Tk()
    root.title('鼠标自动移动状态显示')
    root.attributes('-topmost', True)
    root.geometry('300x50')
    label = tk.Label(root, text='正在自动移动', bg=None)
    label.pack(side='left')


    def readyquit(debug=0):
        button.config(bg='#000000')
        root.update()


    def safequit(debug=0):
        if start == 0:
            button.config(bg='#00CC00')
            root.update()
        else:
            button.config(bg='#CC0000')
            root.update()
        global run
        run = 0


    button = tk.Label(root, text='退出')
    button.pack(side='left')
    button.bind('<ButtonPress-1>', readyquit)
    button.bind('<ButtonRelease-1>', safequit)
    start = 0
    pg.PAUSE = 0
    pg.FAILSAFE = True
    bx, by = 0, 0
    run = 1
    while run == 1:
        x, y = pg.position()
        a = bx - x
        b = bx - x
        if a + b < 0.00000000000000001:
            if start == 0:
                start = 1
                root.configure(bg='#FF0000')
                label.config(text='正在自动移动')
                label.config(bg='#FF0000')
                button.config(bg='#CC0000')
            root.update()
            t = 2
            nx = x + randint(t * -1, t)
            ny = y + randint(t * -1, t)
            pg.moveTo(nx, ny)
            bx, by = pg.position()
            sleep(0.02)
        else:
            bx, by = pg.position()
            wait = True
            if start == 1:
                start = 0
                root.configure(bg='#00FF00')
                label.config(text='不在自动移动')
                label.config(bg='#00FF00')
                button.config(bg='#00CC00')
            root.update()
            while wait:
                bx, by = pg.position()
                root.update()
                for i in range(100):
                    sleep(0.01)
                    root.update()
                    if run == 0:
                        wait = False
                root.update()
                x, y = pg.position()
                if run == 0:
                    wait = False
                if abs(bx - x) + abs(by - y) < 0.01:
                    wait = False
                else:
                    bx, by = pg.position()
                root.update()
except pg.FailSafeException:
    print('已退出程序')
except KeyboardInterrupt:
    print('已退出程序')
except BaseException as e:
    root.destroy()
    raise e
else:
    print('已退出程序')
    root.destroy()
