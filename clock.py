import tkinter as tk
from datetime import datetime
from easygui import msgbox
from tkinter import simpledialog
import pyttsx3
import threading

yibaoshi = True
jiange = 10


def speak(text):
    def task():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=task)
    thread.start()


def update():
    global yibaoshi, jiange
    now = datetime.now()
    label.config(text=now.strftime('%Y年%m月%d日 %H:%M:%S'))
    if int(now.strftime('%M')) == 0:
        if not yibaoshi:
            speak('现在是%s点整!' % now.strftime('%H'))
            msgbox('现在是%s点整!' % now.strftime('%H'), title='报时', ok_button='好的')
            yibaoshi = True
    else:
        yibaoshi = False
    root.after(jiange, update)


def setjiange(event):
    global jiange
    i = simpledialog.askfloat('设置刷新间隔', '请输入要设置的刷新间隔(秒)')
    if i is not None:
        if i > 0:
            jiange = round(i * 1000)
        else:
            jiange = 1


root = tk.Tk()
root.title('时钟')
label = tk.Label(root, text='1970年1月1日 00:00:00', font=('PingFang SC', 100))
label.pack()
root.bind('<Key-equal>', setjiange)
update()
root.mainloop()
