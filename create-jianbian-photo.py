import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image
import time


def create_jianbian_colors(start_color: tuple, end_color: tuple, steps):
    # 特别说明: 此函数由AI生成
    colors = []
    for i in range(steps):
        ratio = i / (steps - 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        colors.append((r, g, b))
    return colors


def choose():
    path = fd.asksaveasfilename(title='选择保存位置', defaultextension='.jpg', filetypes=[('JPG', '*.jpg'), ('PNG', '*.png'), ('BMP', '*.bmp'), ('All Files', '*.*')])
    if path:
        file_path.set(path)


def create_image():
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
    img = Image.new('RGB', (w, h), 'white')
    pixes = img.load()
    x = 0
    colors = []
    jindu['value'] = 0
    speed = 0
    t1 = time.time()
    count1 = 0
    max_size = w * h
    steps = 0
    jianbian_step = 300
    for i in create_jianbian_colors((255, 0, 0), (255, 255, 0), jianbian_step):  # 1 - 2
        colors.append(i)
    for i in create_jianbian_colors((255, 255, 0), (0, 255, 0), jianbian_step):  # 2 - 3
        colors.append(i)
    for i in create_jianbian_colors((0, 255, 0), (0, 0, 255), jianbian_step):  # 3 - 4
        colors.append(i)
    for i in create_jianbian_colors((0, 0, 255), (0, 255, 0), jianbian_step):  # 4 - 3
        colors.append(i)
    for i in create_jianbian_colors((0, 255, 0), (255, 255, 0), jianbian_step):  # 3 - 2
        colors.append(i)
    for i in create_jianbian_colors((255, 255, 0), (255, 0, 0), jianbian_step):  # 2 - 1
        colors.append(i)
    colors *= w * 2
    done = False
    for color in colors:
        if done:
            break
        for y in range(h):
            try:
                pixes[x, y] = color
            except IndexError:
                done = True
            jindu['value'] = (x / w) * 100
            if time.time() - t1 > 0.2:
                t1 = time.time()
                speed = count1 * 5
                count1 = 0
            else:
                count1 += 1
            if speed == 0:
                left_time = 0
            else:
                left_time = (max_size - steps) / speed
        steps += h
        if x % 20 == 0:
            jindu_tip.set('%.2f%%  %dp/s  %.2fs' % (jindu['value'], speed, left_time))
            root.update()
        x += 1
    img.save(file_path.get())
    jindu['value'] = 100
    jindu_tip.set('Done')
    show_info('图片创建完成\n已保存至%s' % file_path.get())


def show_info(a):
    msg = tk.Toplevel(root)
    msg.title('提示')
    text = tk.Text(msg, height=10, width=50, font=('Arial', 15))
    text.pack(fill=tk.BOTH, expand=True)
    text.insert('1.0', a)
    tk.Button(msg, text='关闭', command=msg.destroy, font=('Arial', 30)).pack(fill=tk.X, expand=True)
    msg.focus_force()


root = tk.Tk()
root.title('生成渐变图片')

file_path = tk.StringVar(value='请选择保存位置')
size = tk.StringVar(value='1000x1000')
jindu_tip = tk.StringVar(value='waiting')

tk.Label(root, textvariable=file_path, font=('Arial', 30)).pack(padx=40, pady=10)
tk.Entry(root, textvariable=size, font=('Arial', 30), highlightbackground='white').pack(padx=40, pady=10)
tk.Button(root, text='选择保存位置', command=choose, font=('Arial', 30)).pack(padx=40, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='创建图片', command=create_image, font=('Arial', 30)).pack(padx=40, pady=10, fill=tk.X, expand=True)
jindu = ttk.Progressbar(root, value=0, maximum=100, mode='determinate')
jindu.pack(padx=20, pady=10, fill=tk.X, expand=True)
tk.Label(root, textvariable=jindu_tip, font=('Arial', 20)).pack(padx=40, pady=10)

root.focus_force()
root.mainloop()
