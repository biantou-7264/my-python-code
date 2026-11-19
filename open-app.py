import os
import threading
import tkinter as tk
from subprocess import run
from tkinter import messagebox as mb

import pyperclip as clip

apps = []
appnames = []
please_show = False


def re_task(debug=0):
    global apps, appnames, please_show
    apps = []
    appnames = []

    for root1, dirs, files in os.walk('/Applications'):
        for file in dirs:
            if file.endswith('.app'):
                path = os.path.join(root1, file)
                apps.append(path)
                appnames.append(file)
    for root1, dirs, files in os.walk('/System/Applications'):
        for file in dirs:
            if file.endswith('.app'):
                path = os.path.join(root1, file)
                apps.append(path)
                appnames.append(file)
    box.delete(0, tk.END)
    please_show = True


def re():
    threading.Thread(target=re_task, daemon=True).start()


def locate():
    global apps
    index = box.curselection()
    if len(index) > 0:
        index = index[0]
    else:
        return
    path = apps[index]
    res = run(['open', '-R', path], capture_output=True, text=True)
    if res.returncode != 0:
        mb.showerror('错误', '打开文件位置时出现错误')


def start():
    global apps
    index = box.curselection()
    if len(index) > 0:
        index = index[0]
    else:
        return
    path = apps[index]
    res = run(['open', path], capture_output=True, text=True)
    if res.returncode != 0:
        mb.showerror('错误', '打开文件位置时出现错误')


def copy():
    global apps
    index = box.curselection()
    if len(index) > 0:
        index = index[0]
    else:
        return
    path = apps[index]
    name = os.path.basename(path)
    clip.copy(name)


def update():
    global please_show
    if please_show:
        box.delete(0, tk.END)
        for i in appnames:
            box.insert(tk.END, i)
        please_show = False
        root.update()
    root.after(100, update)


re()
root = tk.Tk()
box = tk.Listbox(root, font=(None, 20), highlightthickness=0)
box.pack(fill=tk.BOTH, expand=True, ipadx=50, ipady=80, padx=10, pady=5)

tk.Button(root, text='显示文件所在位置', command=locate, font=(None, 20)).pack(padx=10, pady=5)
tk.Button(root, text='打开', command=start, font=(None, 20)).pack(padx=10, pady=5)
tk.Button(root, text='立即刷新列表', command=re, font=(None, 20)).pack(padx=10, pady=5)
tk.Button(root, text='复制名字', command=copy, font=(None, 20)).pack(padx=10, pady=5)

root.bind('<F5>', re)
root.after(100, update)

root.focus_force()
root.mainloop()
