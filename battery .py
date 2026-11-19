import tkinter as tk
from tkinter import ttk
import battery as b
from tkinter.simpledialog import askstring

root = tk.Tk()


def update():
    global bap, bat
    bap['value'] = b.battery()
    if b.power():
        style.configure('Horizontal.TProgressbar', thickness=20, background='green')
        bat['text'] = '%d%%⚡︎%s' % (b.battery(), b.time(True))
    else:
        if b.battery() > 80:
            style.configure('Horizontal.TProgressbar', thickness=20, background='green')
        elif b.battery() > 50:
            style.configure('Horizontal.TProgressbar', thickness=20, background='blue')
        elif b.battery() > 20:
            style.configure('Horizontal.TProgressbar', thickness=20, background='yellow')
        else:
            style.configure('Horizontal.TProgressbar', thickness=20, background='red')
        bat['text'] = '%d%%' % b.battery()
    root.after(500, update)


def testb(event=None):
    i = askstring('测试', '请输入电量:')
    if i:
        try:
            b.testba = True
            b.testbai = int(i)
        except Exception:
            pass


def testp(event=None):
    i = askstring('测试', '请输入充电状态:')
    if i:
        try:
            b.testpo = True
            b.testpoi = bool(int(i))
        except Exception:
            pass


style = ttk.Style()
style.theme_use('classic')
style.configure('Horizontal.TProgressbar', thickness=20, background='blue')
bap = ttk.Progressbar(root, length=300, mode='determinate')
bap.pack(pady=(10, 0))
bat = tk.Label(root, text='0%', font=(None, 20))
bat.pack(pady=(5, 10))
root.bind('<F5>', testb)
root.bind('<F6>', testp)
update()
root.mainloop()
