import tkinter as tk
import math
from time import sleep

is_start = False
angle = 280


class Button:
    def __init__(self, x, y, w, h, text='', color='black', press_color='white', command=None, key=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.press_color = press_color
        self.btn = canvas.create_rectangle(self.x, self.y, self.x + w, self.y + h, fill=color, outline='white', width=0)
        self.btn_text = canvas.create_text(self.x + w // 2, self.y + h // 2, text=self.text, font=('Arial', w // 3), fill='white', anchor=tk.CENTER)
        self.command = command
        canvas.tag_bind(self.btn, '<Button-1>', self.press)
        canvas.tag_bind(self.btn, '<ButtonRelease-1>', self.release)
        canvas.tag_bind(self.btn_text, '<Button-1>', self.press)
        canvas.tag_bind(self.btn_text, '<ButtonRelease-1>', self.release)
        canvas.tag_bind(self.btn, '<Enter>', self.enter)
        canvas.tag_bind(self.btn, '<Leave>', self.leave)
        canvas.tag_bind(self.btn_text, '<Enter>', self.enter)
        canvas.tag_bind(self.btn_text, '<Leave>', self.leave)
        if key is not None:
            root.bind(key, lambda e: self.command())

    def press(self, event):
        canvas.itemconfig(self.btn, fill=self.press_color)

    def release(self, event):
        canvas.itemconfig(self.btn, fill=self.color)
        if self.command is not None:
            self.command()

    def enter(self, event):
        canvas.itemconfig(self.btn, width=3)
        canvas.config(cursor='pointinghand')

    def leave(self, event):
        canvas.itemconfig(self.btn, width=0)
        canvas.config(cursor='arrow')

    def config_text(self, text):
        canvas.itemconfig(self.btn_text, text=text)
        self.text = text

    def config_command(self, command):
        self.command = command


def start():
    global is_start
    start_btn.config_text('停止')
    start_btn.config_command(stop)
    is_start = True
    tip.config(text='稍后请点击停止按钮')


def stop():
    global is_start
    start_btn.config_text('开始')
    start_btn.config_command(start)
    is_start = False
    tip.config(text='很可惜,没中')


def cal_angle_xy(angle, start_x, start_y, length):
    angle_rad = math.radians(angle - 90)
    end_x = start_x + length * math.cos(angle_rad)
    end_y = start_y + length * math.sin(angle_rad)
    return end_x, end_y


def rotate():
    global angle, needle
    if is_start:
        if angle < 360:
            angle += 20
        else:
            angle = 0
        canvas.delete(needle)
        x, y = cal_angle_xy(angle, 175, 175, 105)
        needle = canvas.create_line(175, 175, x, y, fill='#0000ff', width=5, smooth=True, capstyle=tk.ROUND)
        root.after(10, rotate)
    else:
        angle = 280
        canvas.delete(needle)
        x, y = cal_angle_xy(angle, 175, 175, 105)
        needle = canvas.create_line(175, 175, x, y, fill='#0000ff', width=5, smooth=True, capstyle=tk.ROUND)
        if angle == 280:
            root.after(100, rotate)
        else:
            root.after(10, rotate)


root = tk.Tk()
root.title('幸运大转盘')
root.config(bg='#121826')
root.focus_force()
root.update()
sleep(0.3)

title = tk.Label(root, text='幸运大转盘', bg='#121826', fg='white', font=('Arial', 50))
title.pack(padx=10, pady=10)
root.update()
sleep(0.05)

canvas = tk.Canvas(root, width=350, height=450, bg='#121826')
canvas.pack()
root.update()
sleep(0.05)

canvas.create_arc(50, 50, 300, 300, start=180, extent=-30, outline='white', width=2, fill='#ff2a00')
canvas.create_text(90, 150, text='没中', fill='black', font=('Arial', 15))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=150, extent=-80, outline='white', width=2, fill='#00ffc6')
canvas.create_text(150, 110, text='小奖', fill='black', font=('Arial', 30))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=70, extent=-70, outline='white', width=2, fill='#ffaa00')
canvas.create_text(240, 130, text='普通奖', fill='black', font=('Arial', 20))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=0, extent=-60, outline='white', width=2, fill='#14f1ff')
canvas.create_text(250, 220, text='大奖', fill='black', font=('Arial', 20))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=-60, extent=-40, outline='white', width=2, fill='#9D00ff')
canvas.create_text(190, 250, text='特大奖', fill='black', font=('Arial', 13))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=-100, extent=-50, outline='white', width=2, fill='#ff0080')
canvas.create_text(120, 250, text='随机奖', fill='black', font=('Arial', 15))
root.update()
sleep(0.05)
canvas.create_arc(50, 50, 300, 300, start=-150, extent=-30, outline='white', width=2, fill='#3c096c')
canvas.create_text(90, 195, text='欢乐奖', fill='white', font=('Arial', 12))
root.update()
sleep(0.05)
needle = canvas.create_line(175, 175, 175, 70, fill='#0000ff', width=5, smooth=True, capstyle=tk.ROUND)
root.update()
sleep(0.05)
start_btn = Button(95, 340, 160, 80, text='开始', color='#3a86ff', press_color='#14F1FF', command=start, key='<space>')
root.update()
sleep(0.05)
tip = tk.Label(root, text='请点击开始按钮', bg='#121826', fg='white', font=('Arial', 30))
tip.pack(padx=10, pady=10)
root.update()
sleep(0.05)

root.resizable(False, False)
root.after(10, rotate)
root.focus_force()
root.mainloop()
