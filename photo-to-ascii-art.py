import tkinter as tk
from PIL import Image
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import colorchooser as cs
from traceback import format_exc


def choice_path():
    a = fd.askopenfilename(title='file path', defaultextension='.jpg', filetypes=[('JPEG', '*.jpg'), ('PNG', '*.png'), ('BMP', '*.bmp'), ('All', '*.*')])
    if a:
        path.set(a)


def create():
    try:
        res = ''
        img = Image.open(path.get()).convert('RGB')
        pixes = img.load()
        w, h = img.size
        chars = ' .-=0OØ$&%#@'
        for y in range(0, h, ystep.get()):
            for x in range(0, w, xstep.get()):
                if x < w and y < h:
                    r, g, b = pixes[x, y]
                    brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
                    temp = brightness // (255 // len(chars))
                    if temp == 0:
                        char = chars[0]
                    else:
                        char = chars[int(temp - 1)]
                    res += char
            res += '\n'
        text.delete('1.0', tk.END)
        text.insert('1.0', res)
    except FileNotFoundError:
        mb.showerror('错误', '文件未找到')
        print('\033[41m')
        print(format_exc())
        print('\033[0m')
    except PermissionError:
        mb.showerror('错误', '我没权限')
        print('\033[41m')
        print(format_exc())
        print('\033[0m')
    except Exception as e:
        mb.showerror('未知错误', '%s:%s' % (type(e).__name__, e))
        print('\033[41m')
        print(format_exc())
        print('\033[0m')


def create_colorful():
    print('\033[43mWARNING: "create_colorful" is deprecated!\033[0m')
    try:
        img = Image.open(path.get()).convert('RGB')
        pixes = img.load()
        w, h = img.size
        chars = ' .-=0OØ$&%#@'
        text.delete('1.0', tk.END)
        row, col = 0, 0
        for y in range(0, h, ystep.get()):
            col += 1
            for x in range(0, w, xstep.get()):
                if x < w and y < h:
                    r, g, b = pixes[x, y]
                    brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
                    temp = brightness // (255 // len(chars))
                    if temp == 0:
                        char = chars[0]
                    else:
                        char = chars[int(temp - 1)]
                    row += 1
                    if 'color_%d,%d,%d' % (r, g, b) not in text.tag_names():
                        text.tag_configure(('color_%d,%d,%d' % (r, g, b)), foreground=rgb_to_hex(r, g, b))
                    text.insert('%d.%d' % (row, col), char)
                    text.tag_add('color_%d,%d,%d' % (r, g, b), '%d.%d' % (row, col), '%d.%d' % (row, col + 1))
            text.insert(tk.END, '\n')
    except FileNotFoundError:
        mb.showerror('错误', '文件未找到')
        print('\033[41m')
        print(format_exc())
        print('\033[0m')
    except PermissionError:
        mb.showerror('错误', '我没权限')
        print('\033[41m')
        print(format_exc())
        print('\033[0m')
    except Exception as e:
        mb.showerror('未知错误', '%s:%s' % (type(e).__name__, e))
        print('\033[41m')
        print(format_exc())
        print('\033[0m')


def set_font(*args):
    w, h = root.winfo_width(), root.winfo_height()
    text.config(font=('Menlo', font_size.get()))
    root.geometry('%dx%d' % (w, h))


def set_width(*args):
    text.config(width=width.get())


def set_height(*args):
    text.config(height=height.get())


def set_bg(*args):
    text.config(bg=bg.get())


def set_fg(*args):
    text.config(fg=fg.get())


def bg_click(event):
    temp = cs.askcolor(color=bg.get(), title='选择bg颜色')
    if temp != (None, None):
        bg.set(temp[1])


def fg_click(event):
    temp = cs.askcolor(color=fg.get(), title='选择fg颜色')
    if temp != (None, None):
        fg.set(temp[1])


def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    res = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return res


root = tk.Tk()
root.title('ascii-art生成器')

path = tk.StringVar(value='file path')
xstep = tk.IntVar(value=1)
ystep = tk.IntVar(value=1)
font_size = tk.IntVar(value=5)
width = tk.IntVar(value=100)
height = tk.IntVar(value=40)
bg, fg = tk.StringVar(value='#000000'), tk.StringVar(value='#ffffff')
colorful = tk.BooleanVar(value=True)
font_size.trace_add('write', set_font)
width.trace_add('write', set_width)
height.trace_add('write', set_height)
bg.trace_add('write', set_bg)
fg.trace_add('write', set_fg)

tk.Label(root, text='ascii-art生成器', font=('Arial', 15)).pack(padx=20)
tk.Label(root, textvariable=path, font=('Arial', 10)).pack(padx=20)
tk.Label(root, text='xstep:', font=('Arial', 10)).pack(padx=20)
tk.Entry(root, textvariable=xstep, highlightbackground='white', font=('Arial', 10)).pack(padx=20)
tk.Label(root, text='ystep:', font=('Arial', 10)).pack(padx=20)
tk.Entry(root, textvariable=ystep, highlightbackground='white', font=('Arial', 10)).pack(padx=20)
tk.Button(root, text='选择', font=('Arial', 10), command=choice_path).pack(padx=20, fill=tk.X, expand=True)
tk.Button(root, text='创建', font=('Arial', 10), command=create).pack(padx=20, fill=tk.X, expand=True)
tk.Scale(root, label='字体大小', from_=1, to=30, showvalue=1, font=('Arial', 10), orient=tk.HORIZONTAL, variable=font_size).pack(padx=10, fill=tk.X, expand=True)
tk.Scale(root, label='width', from_=10, to=400, showvalue=1, font=('Arial', 10), orient=tk.HORIZONTAL, variable=width).pack(padx=10, fill=tk.X, expand=True)
tk.Scale(root, label='height', from_=10, to=300, showvalue=1, font=('Arial', 10), orient=tk.HORIZONTAL, variable=height).pack(padx=10, fill=tk.X, expand=True)
tk.Label(root, text='bg: 下面颜色代码可以点', font=('Arial', 10)).pack(padx=20)
temp = tk.Label(root, textvariable=bg, font=('Arial', 10))
temp.pack(padx=20)
temp.bind('<Button-1>', bg_click)
tk.Label(root, text='fg: 下面颜色代码可以点', font=('Arial', 10)).pack(padx=20)
temp = tk.Label(root, textvariable=fg, font=('Arial', 10))
temp.pack(padx=20)
temp.bind('<Button-1>', fg_click)
text = st.ScrolledText(root, wrap=tk.NONE, font=('Menlo', 5), highlightbackground='white', highlightcolor='white', width=100, height=40, bg='black', fg='white')
text.pack(padx=20)

root.focus_force()
root.mainloop()
