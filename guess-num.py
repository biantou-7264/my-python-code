import tkinter as tk
from random import randint
import sys
from tkinter import simpledialog as sd

root = tk.Tk()
root.title('猜数字')
root.config(bg='#323232')
nch = False
num = 0
nowquit = False
maxnum = 100


def ok(event=None):
    global entry
    try:
        user = float(entry.get())
    except ValueError:
        return
    if user == float(num):
        staus.config(text='猜对了!')
        entry.delete(0, tk.END)
        okbtn.config(state=tk.DISABLED)
        entry.config(state=tk.DISABLED)
    if user > float(num):
        staus.config(text='猜大了')
        entry.delete(0, tk.END)
    if user < float(num):
        staus.config(text='猜小了')
        entry.delete(0, tk.END)


def change(event):
    global nch
    nch = True
    staus.config(text='等待你的猜测')
    entry.focus_set()


def reset(event=None):
    global num, maxnum
    num = randint(0, maxnum)
    okbtn.config(state=tk.NORMAL)
    entry.config(state=tk.NORMAL)
    staus.config(text='请开始你的猜测')
    entry.focus_set()


def safequit(event=None):
    global nowquit
    nowquit = True


def setmax():
    global maxnum, canfloat
    maxnum = sd.askinteger('设置最大生成数', '请输入最大生成数:')
    if maxnum is None:
        return
    maxnum = int(maxnum)
    canfloat = False
    sebtn.config(text='设置最大生成数%d' % maxnum)


def clan():
    staus.config(text='请继续你的猜测')


def answer(event):
    global num
    strnum = str(num)
    strnum = '-'.join(strnum)
    staus.config(text='发生错误,code:%s' % strnum)
    root.after(500, clan)


title = tk.Label(root, text='猜数字', font=(None, 50), bg='#323232', fg='#eeeeee')
title.pack(padx=100, pady=30)

entry = tk.Entry(root, font=(None, 30), highlightbackground='#000000', bg='#eeeeee', fg='#323232', state=tk.DISABLED)
entry.pack(padx=20, pady=(0, 10), fill=tk.X, expand=True)

entry.bind('<Escape>', lambda event: root.focus_set())
entry.bind('<Key>', change)
entry.bind('<Return>', ok)
root.bind('<Command-r>', reset)

staus = tk.Label(root, text='请点击重置按钮', font=(None, 20), bg='#323232', fg='#eeeeee')
staus.pack(padx=100, pady=30)

okbtn = tk.Button(root, text='确定↩', font=(None, 30), state=tk.DISABLED, command=ok)
okbtn.pack(padx=20, pady=(0, 20), fill=tk.X, expand=True)

rebtn = tk.Button(root, text='重置⌘R', font=(None, 30), command=reset)
rebtn.pack(padx=20, pady=(0, 20), fill=tk.X, expand=True)

sebtn = tk.Button(root, text='设置最大生成数%d' % maxnum, font=(None, 30), command=setmax)
sebtn.pack(padx=20, pady=(0, 20), fill=tk.X, expand=True)

root.protocol('WM_DELETE_WINDOW', safequit)
root.bind('<Control-a>', answer)
root.focus_force()

while True:
    try:
        float(entry.get())
    except ValueError:
        length = len(entry.get())
        if length > 0:
            entry.delete(length - 1, tk.END)
    root.update()
    if nowquit:
        break

sys.exit()
