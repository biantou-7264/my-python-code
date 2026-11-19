import math
import sys
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

import pyautogui as pag

now_stop = False
color = ['pink', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan'] * 1000
lines = []
sys.setrecursionlimit(10000)


def cal_line(size_now, angle, x, y, step=0):
    try:
        step += 1
        if step > max_step.get():
            if not any([step <= max_step.get(), not now_stop]):
                root.after(200, finish)
            return
        if now_stop:
            root.after(200, finish)
            return
        if step % 50 == 0:
            root.update()
        nx, ny = cal_angle_xy(angle, x, y, size_now)
        lines.append((x, y, nx, ny, color[step - 1]))
        size_now *= 0.7
        cal_line(size_now, angle - 30, nx, ny, step)
        cal_line(size_now, angle + 30, nx, ny, step)
        if step == 1:
            root.after(200, finish)
    except Exception as e:
        mb.showerror('error', e)


def cal_angle_xy(angle, start_x, start_y, length):
    angle_rad = math.radians(angle - 90)
    end_x = start_x + length * math.cos(angle_rad)
    end_y = start_y + length * math.sin(angle_rad)
    return end_x, end_y


def start():
    global now_stop
    now_stop = False
    canvas.delete(tk.ALL)
    if max_step.get() >= 20:
        res = mb.askokcancel('oh!', '%d is too big.Whether to continue?' % max_step.get())
        if not res:
            return
    tips.config(text='calculating...')
    lines.clear()
    root.after(100, cal_line, size.get(), 0, 400, 600)
    stop_btn.config(state=tk.NORMAL)
    draw_btn.config(state=tk.DISABLED)


def stop():
    global now_stop
    now_stop = True
    stop_btn.config(state=tk.DISABLED)
    draw_btn.config(state=tk.NORMAL)


def finish():
    global now_stop
    stop_btn.config(state=tk.DISABLED)
    draw_btn.config(state=tk.NORMAL)
    now_stop = False
    print('finish')
    print(lines)
    tips.config(text='drawing...')
    root.update()
    interval = max_step.get() * 5000
    for index, line in enumerate(lines):
        x, y, nx, ny, colour = line
        canvas.create_line(x, y, nx, ny, fill=colour, width=5)
        if index % interval == 0:
            root.update()
    tips.config(text='done')


def get_canvas_coords():
    left_top_x = canvas.winfo_rootx()
    left_top_y = canvas.winfo_rooty()
    right_bottom_x = left_top_x + canvas.winfo_width()
    right_bottom_y = left_top_y + canvas.winfo_height()
    return left_top_x, left_top_y, right_bottom_x, right_bottom_y


def save():
    left_top_x, left_top_y, right_bottom_x, right_bottom_y = get_canvas_coords()
    screen_shot = pag.screenshot(region=(left_top_x, left_top_y, canvas.winfo_width(), canvas.winfo_height()))
    path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png')])
    if path:
        screen_shot.save(path)


root = tk.Tk()
root.title('分形树')
max_step = tk.IntVar(value=4)
size = tk.IntVar(value=150)
fast = tk.BooleanVar(value=False)

canvas = tk.Canvas(root, width=800, height=600, bg='skyblue')
canvas.pack()

set_frame = tk.Frame(root, bg='skyblue')
tk.Label(set_frame, text='size:', font=('Arial', 30), fg='black', bg='skyblue').grid(row=0, column=0)
tk.Entry(set_frame, textvariable=size, font=('Arial', 30), fg='white', bg='#646464', width=30, highlightbackground='white').grid(row=0, column=1)
tk.Label(set_frame, text='step:', font=('Arial', 30), fg='black', bg='skyblue').grid(row=1, column=0)
tk.Entry(set_frame, textvariable=max_step, font=('Arial', 30), fg='white', bg='#646464', width=30, highlightbackground='white').grid(row=1, column=1)
set_frame.pack(fill=tk.BOTH, expand=True)
start_frame = tk.Frame(root, bg='skyblue')
draw_btn = tk.Button(start_frame, text='draw', font=('Arial', 30), command=start)
draw_btn.grid(row=0, column=0, ipadx=50)
stop_btn = tk.Button(start_frame, text='stop', font=('Arial', 30), command=stop, state=tk.DISABLED)
stop_btn.grid(row=0, column=1, ipadx=50)
tk.Button(start_frame, text='save', font=('Arial', 30), command=save).grid(row=0, column=2, ipadx=50)
start_frame.pack(fill=tk.BOTH, expand=True)
tips = tk.Label(root, text='waiting', font=('Arial', 30), fg='black', bg='skyblue')
tips.pack(fill=tk.X)

root.focus_force()
root.mainloop()