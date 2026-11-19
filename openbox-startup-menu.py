import subprocess as sp
import tkinter as tk
from tkinter import messagebox as mb


def startup():
    root.destroy()
    root.update()
    sp.run(['rofi', '-show', 'drun'])


def shutdown():
    if mb.askokcancel('关机', '你要关机吗?'):
        root.destroy()
        root.update()
        sp.run(['systemctl', 'poweroff'])


def reboot():
    if mb.askokcancel('重启', '你要重启吗?'):
        root.destroy()
        root.update()
        sp.run(['systemctl', 'reboot'])


def logout():
    if mb.askokcancel('注销', '你要注销吗?'):
        root.destroy()
        root.update()
        sp.run(['openbox', '--exit'])


root = tk.Tk()
root.title('开始')

tk.Button(root, text='启动', font=('Arial', 20), command=startup).pack(padx=20, pady=10, ipadx=40)
tk.Button(root, text='关机', font=('Arial', 20), command=shutdown).pack(padx=20, pady=10, ipadx=40)
tk.Button(root, text='重启', font=('Arial', 20), command=reboot).pack(padx=20, pady=10, ipadx=40)
tk.Button(root, text='注销', font=('Arial', 20), command=logout).pack(padx=20, pady=10, ipadx=40)
tk.Button(root, text='取消', font=('Arial', 20), command=root.destroy).pack(padx=20, pady=10, ipadx=40)

root.focus_force()
root.mainloop()