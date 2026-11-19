import tkinter as tk
from tkinter import messagebox, Menu
from random import choice
import sys, os

msg = messagebox
okfpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ok.txt')
if not os.path.exists(okfpath):
    ok = msg.askyesno('重要提醒!!!', '当前作品含有颜色变化动画,不建议光敏性癫痫患者查看,是否继续?')
else:
    ok = True
if ok:
    okfile = open('ok.txt', 'w')
    okfile.close()
else:
    sys.exit()
root = tk.Tk()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']


def nocmdq(event):
    return 'break'


def zoom():
    root.attributes("-fullscreen", True)
    root.after(200, zoom)


def focus():
    root.focus_force()
    root.after(200, focus)


def color():
    root.configure(bg=choice(colors))
    root.after(500, color)


def tryquit():
    msg.showerror('Quit Failed', 'Unable to close the application. Please try again.')


def tryforcequit():
    msg.showerror('Force Quit Failed', 'Operation Not Permitted. Please try again.')


root.protocol("WM_DELETE_WINDOW", lambda: None)
menubar = Menu(root)
menu = Menu(menubar, tearoff=0)
menu.add_command(label='quit', command=tryquit)
menu.add_command(label='force quit', command=tryforcequit)
menubar.add_cascade(label='option', menu=menu)
root.config(menu=menubar)
root.createcommand('tk::mac::ShowPreferences', lambda: None)
root.createcommand('tk::mac::ShowHelp', lambda: None)
root.createcommand('tkAboutDialog', lambda *args: None)
root.tk.call('tk', 'appname', 'MyCustomApp')
zoom()
focus()
color()
root.mainloop()
