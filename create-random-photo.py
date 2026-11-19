import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from PIL import Image
from random import randint
import time


def create():
    w, h = size.get().split('x')
    try:
        w = int(w)
    except ValueError:
        show_info('请输入整数大小!')
        return
    try:
        h = int(h)
    except ValueError:
        show_info('请输入整数大小!')
        return
    img = Image.new('RGB', (w, h), color=(255, 255, 255))
    pixes = img.load()
    jindu['value'] = 0
    maximum = w * h
    speed = 0
    t1 = time.time()
    count1 = 0
    for x in range(w):
        for y in range(h):
            pixes[x, y] = (randint(0, 255), randint(0, 255), randint(0, 255))
            steps = x * y
            jindu['value'] = (steps / maximum) * 100
            if time.time() - t1 > 0.2:
                t1 = time.time()
                speed = count1 * 5
                count1 = 0
            else:
                count1 += 1
            if speed == 0:
                left_time = 0
            else:
                left_time = (maximum - steps) / speed
        if x % 20 == 0:
            jindu_tip.set('%.2f%%  %dp/s  %.2fs' % (jindu['value'], speed, left_time))
            root.update()
    img.save(file_path.get())
    jindu['value'] = 100
    jindu_tip.set('Done')
    show_info('图片创建完成\n已保存至%s' % file_path.get())


def choose():
    path = fd.asksaveasfilename(title='选择保存位置', defaultextension='.jpg', filetypes=[('JPG', '*.jpg'), ('PNG', '*.png'), ('BMP', '*.bmp'), ('All Files', '*.*')])
    if path:
        file_path.set(path)


def show_info(a):
    msg = tk.Toplevel(root)
    msg.title('提示')
    text = tk.Text(msg, height=10, width=50, font=('Arial', 15))
    text.pack(fill=tk.BOTH, expand=True)
    text.insert('1.0', a)
    tk.Button(msg, text='关闭', command=msg.destroy, font=('Arial', 30)).pack(fill=tk.X, expand=True)
    msg.focus_force()


root = tk.Tk()
root.title('生成随机图片')

file_path = tk.StringVar(value='请选择保存位置')
size = tk.StringVar(value='500x500')
jindu_tip = tk.StringVar(value='waiting')

tk.Label(root, textvariable=file_path, font=('Arial', 30)).pack(padx=40, pady=10)
tk.Entry(root, textvariable=size, font=('Arial', 30), highlightbackground='white').pack(padx=40, pady=10)
tk.Button(root, text='选择保存位置', command=choose, font=('Arial', 30)).pack(padx=40, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='创建图片', command=create, font=('Arial', 30)).pack(padx=40, pady=10, fill=tk.X, expand=True)
jindu = ttk.Progressbar(root, value=0, maximum=100, mode='determinate')
jindu.pack(padx=20, pady=10, fill=tk.X, expand=True)
tk.Label(root, textvariable=jindu_tip, font=('Arial', 20)).pack(padx=40, pady=10)

root.focus_force()
root.mainloop()
