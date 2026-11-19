import os, shutil
import subprocess as sp
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import scrolledtext as st
from time import sleep


def choose_file():
    path = fd.askopenfilename(title='请选择python文件', filetypes=[('python程序', '*.py')])
    if path:
        file.set(path)
        show_stdout('ℹ︎你选择了文件:%s\n' % path)
    else:
        show_stdout('ℹ︎你取消了文件选择\n')
    root.focus_force()


def show_stdout(line):
    current_position = text_area.yview()
    text_area.insert(tk.END, line)
    if current_position[1] >= 0.99:
        text_area.see(tk.END)
    root.update()


def start():
    global thread
    path = file.get()
    if os.path.exists(path):
        show_stdout('************************************\n')
        show_stdout('⟳开始打包%s\n' % path)
        command = ['/Library/Frameworks/Python.framework/Versions/3.14/bin/python3', '-m', 'PyInstaller', '--clean', '-w']
        if onefile.get():
            show_stdout('ℹ︎当前打包模式:单文件\n')
            command.append('-F')
        else:
            show_stdout('ℹ︎当前打包模式:多文件\n')
        for mod in exclu_mod_area.get('1.0', tk.END).splitlines():
            command.append('--exclude-module')
            command.append(mod)
            show_stdout('ℹ︎已排除库:%s\n' % mod)
        command.append('--name')
        command.append(name.get())
        command.append('--log-level=DEBUG')
        command.append(path)
        show_stdout('ℹ︎即将执行命令:%s\n' % ' '.join(command))
        sleep(1)
        thread = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        for line in thread.stdout:
            show_stdout(line)
        thread.wait()
        show_stdout('√进程已结束,退出代码为%d\n' % thread.returncode)
        if thread.returncode == 0:
            show_stdout('√进程正常退出\n')
        show_stdout('************************************\n')
        del thread
    else:
        show_stdout('⚠︎文件不存在!\n')
    root.focus_force()


def kill():
    global thread
    try:
        thread.kill()
        del thread
    except NameError:
        show_stdout('⚠︎还没有进程哦\n')
    except Exception as e:
        print(type(e).__name__)


def install():
    for file in os.listdir('./dist'):
        if file != '.DS_Store':
            shutil.move(os.path.join(os.path.abspath('./dist'), file), '/Applications/')
            print(file)
            show_stdout('√已安装 %s\n' % file)


root = tk.Tk()
root.title('软件打包工具')
onefile = tk.BooleanVar(value=False)
name = tk.StringVar(value='请输入名字')

title = tk.Label(root, text='欢迎使用软件打包工具', font=('Arial', 30))
title.pack(padx=10)
file = tk.StringVar(value='请选择文件')
file_text = tk.Label(root, textvariable=file, font=('Arial', 15), anchor='w', bg='black', fg='white')
file_text.pack(padx=10, anchor='w', fill='x', expand=True)
choose_file_btn = tk.Button(root, text='选择python文件', command=choose_file, font=('Arial', 15))
choose_file_btn.pack(padx=10, fill='x', expand=True)
onefile_checkbtn = tk.Checkbutton(root, text='使用单文件打包', variable=onefile, onvalue=True, offvalue=False, font=('Arial', 15))
onefile_checkbtn.pack(pady=2, ipadx=10)
name_entry = tk.Entry(root, font=('Arial', 15), textvariable=name, width=30, highlightbackground='white')
name_entry.pack(padx=10, fill='x', expand=True)
exclu_mod_area = st.ScrolledText(root, width=50, height=20, wrap=tk.WORD, highlightthickness=2, highlightbackground='white', highlightcolor='#7f7fff')
exclu_mod_area.pack(padx=10, fill='x', expand=True)
exclu_mod_area.insert(tk.END, '排除模块,一行一个')
start_btn = tk.Button(root, text='开始打包', command=start, font=('Arial', 15))
start_btn.pack(padx=10, fill='x', expand=True)
kill_btn = tk.Button(root, text='强制结束进程', command=kill, font=('Arial', 15))
kill_btn.pack(padx=10, fill='x', expand=True)
install_btn = tk.Button(root, text='一键安装', command=install, font=('Arial', 15))
install_btn.pack(padx=10, fill='x', expand=True)
text_area = st.ScrolledText(root, width=50, height=20, wrap=tk.WORD, highlightthickness=2, highlightbackground='white', highlightcolor='#7f7fff')
text_area.pack(padx=10, fill='x', expand=True)

root.update()
root.geometry('500x%d' % root.winfo_height())

root.focus_force()
root.mainloop()
