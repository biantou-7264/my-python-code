import tkinter as tk
from time import sleep


def start():
    try:
        global fat
        fat.destroy()
    except Exception:
        pass
    load.config(fg='white')
    for i in range(1, 11):
        load.config(text='正在尝试第%d次' % i)
        root.update()
        sleep(1)
    load.config(text='启动失败:太胖了')
    load.config(fg='red')
    global photo
    photo = tk.PhotoImage(file='fatduzi.gif')
    fat = tk.Label(root, image=photo)
    fat.pack()


root = tk.Tk()
root.title('mumget')

title = tk.Label(root, text='MUMGET', font=(None, 50), fg='white')
title.pack()
startbtn = tk.Button(root, text='启动', command=start, font=(None, 30))
startbtn.pack()
load = tk.Label(root, text='等待启动', font=(None, 20))
load.pack()

root.focus_force()
root.mainloop()
