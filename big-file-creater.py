import tkinter as tk
import os
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
from traceback import format_exc


def create():
    try:
        with open(save_path.get(), 'wb') as f:
            f.write(b'')
        progess_bar['value'] = 0
        progess_info.set('正在生成1GB随机数据...')
        root.update()
        data_1GB = os.urandom(1024 * 1024 * 1024)
        for i in range(size.get()):
            with open(save_path.get(), 'ab') as f:
                f.write(data_1GB)
            progess = (i / size.get()) * 100
            progess_bar['value'] = progess
            progess_info.set('%.2f%% %dGB/%dGB' % (progess, i, size.get()))
            root.update()
        progess_info.set('100%% %dGB/%dGB' % (size.get(), size.get()))
        progess_bar['value'] = 100
        root.update()
        mb.showinfo('提示', '生成成功!')
    except Exception:
        print(format_exc())
        mb.showerror('错误', '生成失败')


def select_path():
    path = fd.asksaveasfilename(defaultextension='*.*', filetypes=[('All Files', '*.*')])
    if path:
        save_path.set(path)


root = tk.Tk()
root.title('大文件生成器')

size = tk.IntVar(value=10)
save_path = tk.StringVar(value=os.path.expanduser('~/Desktop/bigfile'))
progess_info = tk.StringVar(value='0% 0GB/0GB')

tk.Label(root, text='大文件生成器', font=('Arial', 30)).pack(padx=20, pady=10)
tk.Label(root, text='大小(GiB):', font=('Arial', 20)).pack(padx=20, pady=10)
tk.Entry(root, textvariable=size, font=('Arial', 20), highlightbackground='white').pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=save_path, font=('Arial', 20)).pack(padx=20, pady=10)
tk.Button(root, text='选择保存位置', font=('Arial', 20), command=select_path).pack(padx=20, pady=10, fill=tk.X)
tk.Button(root, text='开始生成!', font=('Arial', 20), command=create).pack(padx=20, pady=10, fill=tk.X)
progess_bar = ttk.Progressbar(root, orient='horizontal', length=20, mode='determinate')
progess_bar.pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=progess_info, font=('Arial', 20)).pack(padx=20, pady=10)

root.focus_force()
root.mainloop()
