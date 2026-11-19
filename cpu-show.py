import tkinter as tk
from cpu import cpu
from tkinter import ttk
import threading as th

res = 0


def update():
    global res, text, cpup
    text.config(text='%.1f%%' % res)
    cpup['value'] = res
    if res < 20:
        style.configure('Horizontal.TProgressbar', thickness=20, background='green')
    elif res < 40:
        style.configure('Horizontal.TProgressbar', thickness=20, background='yellow')
    elif res < 70:
        style.configure('Horizontal.TProgressbar', thickness=20, background='red')
    else:
        style.configure('Horizontal.TProgressbar', thickness=20, background='purple')
    root.after(100, update)


def test():
    global res
    while True:
        res = cpu(1)


root = tk.Tk()
root.attributes('-topmost', True)

style = ttk.Style()
style.theme_use('classic')
style.configure('Horizontal.TProgressbar', thickness=20, background='blue')
cpup = ttk.Progressbar(root, length=300, mode='determinate')
cpup.pack()
text = tk.Label(root, text='--%', font=(None, 30))
text.pack()
update()
thread = th.Thread(target=test)
thread.start()
root.mainloop()
