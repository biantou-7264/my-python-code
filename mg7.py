import tkinter as tk
from time import sleep


def start():
    for i in range(0, 101):
        tip.config(text='加载中%d%%' % i)
        sleep(0.1)
        root.update()
    tip.config(text='颜值:1000/1000')


root = tk.Tk()
root.title('mg7')

title = tk.Label(root, text='颜值检测器', font=('Arial', 50))
title.pack(padx=40, pady=10)
start_btn = tk.Button(root, text='检测', font=('Arial', 30), command=start)
start_btn.pack(padx=20, pady=10, fill=tk.X, expand=True)
tip = tk.Label(root, text='', font=('Arial', 30))
tip.pack(padx=10, pady=10)

root.focus_force()
root.mainloop()
