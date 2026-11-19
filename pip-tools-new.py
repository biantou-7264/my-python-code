import sys
import tkinter as tk
import subprocess as sp
from tkinter import scrolledtext as st
from tkinter import messagebox as mb


def stdout(text):
    text_area.insert(tk.END, text)
    text_area.insert(tk.END, '\n')
    text_area.see(tk.END)
    root.update()


def install():
    try:
        command = [sys.executable, '-m', 'pip', 'install', name.get(), '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple']
        stdout('开始安装%s' % name.get())
        thread = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        for line in thread.stdout:
            stdout(line)
        thread.wait()
        if thread.returncode == 0:
            stdout('安装成功')
        else:
            stdout('安装失败')
    except:
        stdout('安装失败')


def uninstall():
    try:
        user_choice = mb.askyesno('重要提示', '你确定要卸载%s吗' % name.get())
        if not user_choice:
            return
        command = [sys.executable, '-m', 'pip', 'uninstall', name.get(), '-y']
        stdout('开始卸载%s' % name.get())
        thread = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        for line in thread.stdout:
            stdout(line)
        thread.wait()
        if thread.returncode == 0:
            stdout('卸载成功')
        else:
            stdout('卸载失败')
    except:
        stdout('卸载失败')


def upgrade():
    try:
        command = [sys.executable, '-m', 'pip', 'install', '--upgrade', name.get()]
        stdout('开始更新%s' % name.get())
        thread = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        for line in thread.stdout:
            stdout(line)
        thread.wait()
        if thread.returncode == 0:
            stdout('更新成功')
        else:
            stdout('更新失败')
    except:
        stdout('更新失败')


root = tk.Tk()
root.title('pip工具')
name = tk.StringVar(value='输入名字')

title = tk.Label(root, text='pip工具', font=('Arial', 40))
title.pack(pady=10)

text_area = st.ScrolledText(root, font=('Arial', 15), wrap=tk.WORD, width=50, height=20, highlightbackground='white')
text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

name_entry = tk.Entry(root, font=('Arial', 20), width=50, textvariable=name, highlightbackground='white')
name_entry.pack(pady=10, padx=10, fill=tk.X, expand=True)

install_btn = tk.Button(root, text='安装', font=('Arial', 20), command=install)
install_btn.pack(pady=10, padx=10, fill=tk.X, expand=True)
uninstall_btn = tk.Button(root, text='卸载', font=('Arial', 20), command=uninstall)
uninstall_btn.pack(pady=10, padx=10, fill=tk.X, expand=True)
upgrade_btn = tk.Button(root, text='更新', font=('Arial', 20), command=upgrade)
upgrade_btn.pack(pady=10, padx=10, fill=tk.X, expand=True)

root.focus_force()
root.mainloop()
