# 这个不是真的游戏,是整蛊假游戏

import tkinter as tk
from time import sleep
import pyautogui as pag

game_name = '游戏'  # 换成游戏名
pag.FAILSAFE = False  # 关闭安全功能


def start():
    global canvas
    title.destroy()
    start_btn.destroy()
    canvas = tk.Canvas(root, bg='black', width=400, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)
    root.attributes('-fullscreen', True)  # 游戏一般都是全屏的
    root.update()
    canvas.create_text(200, 200, text=game_name, font=('Arial', 100), anchor=tk.NW)  # 假装启动了游戏
    new_start = canvas.create_text(200, 400, text='开始', font=('Arial', 50), anchor=tk.NW)
    canvas.tag_bind(new_start, '<Button-1>', start_2)


def start_2(event):
    global canvas
    canvas.delete(tk.ALL)
    root.update()
    root.after(50, hide_pointing)
    while True:
        # 假蓝屏
        canvas.config(bg='#0000ff')
        safe_sleep(0.3)
        # 显示眼睛
        canvas.create_oval(100, 100, 150, 150, fill='white', outline='white')
        canvas.create_oval(100, 200, 150, 250, fill='white', outline='white')
        root.update()
        safe_sleep(0.05)
        # 显示嘴巴
        canvas.create_arc(200, 100, 300, 250, start=90, extent=180, fill='white', style=tk.ARC, width=30)
        root.update()
        safe_sleep(0.3)
        # 显示提示文字
        canvas.create_text(300, 175, text='Your computer has encountered a problem \nand needs to be restarted.', font=('Arial', 50, 'bold'), fill='white', anchor=tk.NW)
        canvas.create_text(150, 350, text='We will collect some error information and restart it for you.', font=('Arial', 30), fill='white', anchor=tk.NW)
        root.update()
        safe_sleep(0.2)
        progress = canvas.create_text(150, 500, text='0% Completed.', font=('Arial', 30), fill='white', anchor=tk.NW)
        root.update()
        for i in range(0, 101):
            canvas.itemconfig(progress, text='%d%% Completed.' % i)
            root.update()
            safe_sleep(0.2)
        safe_sleep(1)
        # 自动重启
        canvas.delete(tk.ALL)
        canvas.config(bg='black')
        root.update()
        safe_sleep(2)
        # 显示windows 11标志
        canvas.create_rectangle(500, 250, 600, 350, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(650, 250, 750, 350, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(500, 400, 600, 500, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(650, 400, 750, 500, fill='#00b9ff', outline='#00b9ff')
        root.update()
        safe_sleep(1)
        # 显示加载动画
        angle = 0
        loading_arc = canvas.create_arc(600, 600, 650, 650, start=angle, extent=270, fill='white', outline='white', style=tk.ARC, width=10)
        for _ in range(400):
            angle += 3
            canvas.delete(loading_arc)
            loading_arc = canvas.create_arc(600, 600, 650, 650, start=angle, extent=270, fill='white', outline='white', style=tk.ARC, width=10)
            root.update()
        canvas.delete(tk.ALL)
        root.update()


def hide_pointing(event=None):
    pag.moveTo(10000, 10000)
    root.after(50, hide_pointing)


def safe_sleep(sec):
    for _ in range(int(round(sec * 5))):
        sleep(0.05)
        root.update()

root = tk.Tk()
root.title(game_name)

title = tk.Label(root, text=game_name, font=('Arial', 50))
title.pack(padx=40, pady=10)
start_btn = tk.Button(root, text='启动', font=('Arial', 30), command=start)
start_btn.pack(padx=20, pady=20)

root.focus_force()
root.mainloop()
