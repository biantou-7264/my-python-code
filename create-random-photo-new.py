import os
import time
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

import numpy as np
from PIL import Image


def start():
    if len(size.get().split('x')) != 2:
        mb.showerror('错误', '请输入正确的大小(宽度x高度, 是小写字母x)')
        return

    progess_info.set('正在初始化...')
    root.update()
    w, h = size.get().split('x')
    w = int(w)
    h = int(h)
    total_pixes = w * h
    rng = np.random.default_rng(seed=round(time.time()))

    a = time.time()
    time_per_pixel = 1.3216562271 / 800000000  # ≈ 1.4685e-9
    need_time = total_pixes * time_per_pixel
    progess_info.set('正在生成数据(大约%.4f秒)...' % need_time)
    root.update()
    pixels = rng.integers(0, 256, (total_pixes, 3), dtype=np.uint8)
    print('生成数据使用%.10f秒' % (time.time() - a))

    progess_info.set('正在保存图片...')
    root.update()
    img = Image.fromarray(pixels.reshape((h, w, 3)), 'RGB')
    img.save(save_path.get())

    progess_info.set('正在释放资源...')
    root.update()
    del pixels

    progess_info.set('生成完成')


def select_path():
    file = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png'), ('JPEG', '*.jpg'), ('BMP', '*.bmp')])
    if file:
        save_path.set(file)


root = tk.Tk()
root.title('随机图片生成器')

size = tk.StringVar(value='100x100')
save_path = tk.StringVar(value=os.path.expanduser('~/Desktop/random_photo.png'))
progess_info = tk.StringVar(value='等待生成')

tk.Label(root, text='图片大小(宽度x高度):', font=('Arial', 20)).pack(padx=20, pady=10)
tk.Entry(root, textvariable=size, font=('Arial', 20), highlightbackground='white').pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=save_path, font=('Arial', 20)).pack(padx=20, pady=10)
tk.Button(root, text='选择保存位置', font=('Arial', 20), command=select_path).pack(padx=20, pady=10, fill=tk.X)
start_btn = tk.Button(root, text='开始生成', font=('Arial', 20), command=start)
start_btn.pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=progess_info, font=('Arial', 20)).pack(padx=20, pady=10)

root.focus_force()
root.mainloop()
