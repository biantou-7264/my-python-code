import tkinter as tk
from signal import *
from threading import Thread
from time import sleep

start = False
thread_id = 0
thread_count = 0


def calculation(tid):
    global thread_count
    print('%d开始' % tid)
    thread_count += 1
    for _ in range(2000):
        5 ** 3
        sleep(0.001)
    thread_count -= 1
    print('%d结束' % tid)


def create():
    global thread_id
    root.update()
    if not start:
        return
    for i in range(20):
        if not start:
            return
        root.update()
        try:
            if thread_count > 150:
                continue
            thread = Thread(target=calculation, args=(thread_id,))
            thread.deamon = True
            thread.start()
            print('%d创建' % thread_id)
        except:
            print('%d错误' % thread_id)
        thread_id += 1
    root.update()
    root.update_idletasks()
    root.after(0, update)


def run():
    if start:
        root.after(10, create)
    root.update()
    root.update_idletasks()
    root.after(0, update)
    root.after(20, run)


def update():
    if start:
        root.configure(bg='#ff0000')
        title.config(bg='#7f0000')
        start_btn.config(bg='#c80000')
        thread_count_label.config(bg='#c80000')
    else:
        root.configure(bg='#0000c8')
        title.config(bg='#00007f')
        start_btn.config(bg='#000064')
        thread_count_label.config(bg='#000064')
    thread_count_label.config(text='%d个线程' % thread_count)
    root.update()
    root.update_idletasks()


def update_start(*args):
    global start
    start = start_var.get()
    root.update()


root = tk.Tk()
root.title('暖手宝')
root.configure(background='#0000c8')
start_var = tk.BooleanVar(value=False)
start_var.trace_add('write', update_start)

title = tk.Label(root, text='暖手宝', font=('Arial', 50), bg='#00007f')
title.pack(padx=100, pady=30, ipadx=10, ipady=10)
start_btn = tk.Checkbutton(root, text='开启加热', variable=start_var, onvalue=True, offvalue=False, font=('Arial', 30), bg='#000064')
start_btn.pack(padx=20, pady=50, ipadx=10, ipady=10)
thread_count_label = tk.Label(root, text='?个线程', font=('Arial', 30), bg='#000064')
thread_count_label.pack(padx=20, pady=20, ipadx=10, ipady=10)

signal(SIGALRM, lambda sig, frame: root.update())

root.after(100, update)
root.after(10, update_start)
root.after(500, run)
root.focus_force()
root.mainloop()

start_var.set(False)
start = False
