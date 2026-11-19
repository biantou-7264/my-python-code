import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import pyautogui as pag
import math

colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'] * 1000


def create_zhuzhuang():
    try:
        canvas.delete(tk.ALL)
        datas_dict = eval('{%s}' % datas.get())
        x = 0
        nx = 0
        temp = []
        for i in datas_dict.values():
            temp.append(int(i))
        datas_list = temp.copy()
        datas_len = len(datas_list)
        w = 700 / datas_len
        temp = []
        name_list = []
        for i in datas_dict.keys():
            name_list.append(i)
        max_num = max(datas_list)
        for count, num in enumerate(datas_list):
            h = (500 / max_num) * num
            color = colors[count]
            canvas.lower(canvas.create_rectangle(x + 50, 550, x + w + 50, 550 - h, fill=color, width=0))
            canvas.create_text((x + w + 50 + x + 50) / 2, 550 - h - 20, text=num, font=('Arial', 20), fill='red', anchor=tk.CENTER)
            canvas.create_line(x + w + 50, 550, x + w + 50, 0 - h, fill='white', width=2)
            x += w
        x = 0
        for count, name in enumerate(name_list):
            color = colors[count]
            nx = (x + w + 50 + x + 50) / 2
            canvas.create_text(nx, 570, text=name, font=('Arial', 30), fill='red', anchor=tk.CENTER)
            x += w
        for i in range(0, max_num + 1):
            h = (500 / max_num) * i
            canvas.create_text(10, 550 - h, text=str(i), font=('Arial', 30), fill='red', anchor=tk.W)
            canvas.create_line(0, 550 - h, 750, 550 - h, fill='white', width=2)
    except BaseException as e:
        mb.showerror('错误', e)


def create_zhexian():
    try:
        canvas.delete(tk.ALL)
        datas_dict = eval('{%s}' % datas.get())
        x = 0
        nx = 0
        temp = []
        for i in datas_dict.values():
            temp.append(int(i))
        datas_list = temp.copy()
        datas_len = len(datas_list)
        w = 700 / datas_len
        temp = []
        name_list = []
        for i in datas_dict.keys():
            name_list.append(i)
        max_num = max(datas_list)
        h = (500 / max_num) * datas_list[0]
        for count, num in enumerate(datas_list):
            nh = (500 / max_num) * num
            color = colors[count]
            nx += w
            canvas.create_line(x, 550 - h, nx, 550 - nh, fill=color, width=5)
            canvas.lower(canvas.create_line(x, 550, x, 0, fill='white', width=2))
            canvas.lower(canvas.create_line(nx, 550, nx, 0, fill='white', width=2))
            canvas.create_text(nx, 550 - nh - 20, text=num, font=('Arial', 20), fill='red', anchor=tk.CENTER)
            x += w
            h = nh
        nx = 0
        for count, name in enumerate(name_list):
            nh = (500 / max_num) * datas_list[count]
            color = colors[count]
            nx += w
            canvas.create_text(nx, 570, text=name, font=('Arial', 30), fill='red', anchor=tk.CENTER)
            x += w
            h = nh
        for i in range(0, max_num + 1):
            h = (500 / max_num) * i
            canvas.create_text(10, 550 - h, text=str(i), font=('Arial', 30), fill='red', anchor=tk.W)
            canvas.lower(canvas.create_line(0, 550 - h, 750, 550 - h, fill='white', width=2))
    except BaseException as e:
        raise e


def create_bingtu():
    try:
        canvas.delete(tk.ALL)
        datas_dict = eval('{%s}' % datas.get())
        x = 0
        nx = 0
        temp = []
        for i in datas_dict.values():
            temp.append(int(i))
        datas_list = temp.copy()
        sum_num = sum(datas_list)
        w = 360 / sum_num
        angle = 0
        for count, num in enumerate(datas_list):
            color = colors[count]
            canvas.lower(canvas.create_arc(200, 100, 600, 500, start=90 - angle, extent=w * num * -1, fill=color, width=3, outline='white'))
            angle += w * num
            x, y = 400, 300
            nx, ny = cal_angle_and_xy(angle - (w * num / 2), 100)
            x += nx
            y += ny
            canvas.create_text(x, y, text=num, font=('Arial', 20), fill='black', anchor=tk.W)
    except BaseException as e:
        mb.showerror('错误', e)


def create():
    if '柱状' in mode.get():
        create_zhuzhuang()
    if '折线' in mode.get():
        create_zhexian()
    if '饼' in mode.get():
        create_bingtu()


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


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


root = tk.Tk()
root.title('数据可视化')
datas = tk.StringVar(value='输入数据,格式key:value,key:value')
mode = tk.StringVar(value='柱状图')

canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()
entry = tk.Entry(root, textvariable=datas, bg='black', fg='white', highlightbackground='#c8c8c8', font=('Arial', 20))
entry.pack(fill=tk.X, expand=True, pady=10)
box = tk.OptionMenu(root, mode, '柱状图', '折线图', '饼图')
box.pack(fill=tk.X, expand=True, pady=10)
start_btn = tk.Button(root, text='启动', command=create, font=('Arial', 20))
start_btn.pack(fill=tk.X, expand=True, pady=10)
save_btn = tk.Button(root, text='保存', command=save, font=('Arial', 20))
save_btn.pack(fill=tk.X, expand=True, pady=10)

root.focus_force()
root.mainloop()
