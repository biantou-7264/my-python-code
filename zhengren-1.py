#发明者:biantou
#发明项目:整蛊程序
#发明日期:2026年6月10日
import sys
import tkinter as tk
from time import sleep


def start():
    root.iconify()
    msgs = []
    for _ in range(200):
        msg = tk.Toplevel(root)
        msg.title('错误')
        msg.configure(bg='red')
        msg.bind('<Control-q>', lambda event: sys.exit(0))
        tk.Label(msg, text='错误', font=('Arial', 70), fg='yellow', bg='red').pack(padx=50, pady=50)
        root.update()
        msg.update()
        msgs.append(msg)
    for i in msgs:
        i.destroy()
    root.deiconify()
    title.destroy()
    start_btn.destroy()
    canvas = tk.Canvas(root, height=400, width=400)
    canvas.pack(fill=tk.BOTH, expand=True)
    root.attributes('-fullscreen', True)
    root.update()
    while True:
        canvas.config(bg='#0000ff')
        sleep(1)
        canvas.create_oval(100, 100, 150, 150, fill='white', outline='white')
        canvas.create_oval(100, 200, 150, 250, fill='white', outline='white')
        root.update()
        sleep(0.05)
        canvas.create_arc(200, 100, 300, 250, start=90, extent=180, fill='white', style=tk.ARC, width=30)
        root.update()
        sleep(0.3)
        canvas.create_text(300, 175, text='Your computer has encountered a problem \nand needs to be restarted.', font=('Arial', 50, 'bold'), fill='white', anchor=tk.NW)
        canvas.create_text(150, 350, text='We will collect some error information and restart it for you.', font=('Arial', 30), fill='white', anchor=tk.NW)
        root.update()
        sleep(0.2)
        progress = canvas.create_text(150, 500, text='0% Completed.', font=('Arial', 30), fill='white', anchor=tk.NW)
        root.update()
        for i in range(0, 101):
            canvas.itemconfig(progress, text='%d%% Completed.' % i)
            root.update()
            sleep(0.1)
        sleep(1)
        canvas.delete(tk.ALL)
        canvas.config(bg='black')
        root.update()
        sleep(2)
        canvas.create_rectangle(500, 250, 600, 350, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(650, 250, 750, 350, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(500, 400, 600, 500, fill='#00b9ff', outline='#00b9ff')
        canvas.create_rectangle(650, 400, 750, 500, fill='#00b9ff', outline='#00b9ff')
        root.update()
        sleep(1)
        angle = 0
        loading_arc = canvas.create_arc(600, 600, 650, 650, start=angle, extent=270, fill='white', outline='white', style=tk.ARC, width=10)
        for _ in range(500):
            angle += 3
            canvas.delete(loading_arc)
            loading_arc = canvas.create_arc(600, 600, 650, 650, start=angle, extent=270, fill='white', outline='white', style=tk.ARC, width=10)
            root.update()
        canvas.delete(tk.ALL)
        root.update()


root = tk.Tk()
root.title('游戏')

title = tk.Label(root, text='游戏', font=('Arial', 70))
title.pack(pady=20, padx=100)
start_btn = tk.Button(root, text='开始', font=('Arial', 40), command=start)
start_btn.pack(pady=20, padx=20, fill=tk.X, expand=True)

root.bind('<Control-q>', lambda event: sys.exit(0))
root.focus_force()
root.mainloop()
