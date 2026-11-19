import tkinter as tk
from random import randint, choice
from time import sleep


def start_press(event):
    canvas.itemconfig(start_btn, fill='red')
    canvas.itemconfig(start_btn, font=('Arial', 50, 'bold'))


def start(event):
    root.attributes('-fullscreen', True)
    canvas.delete('all')
    root.update()
    error_colors = ['#ff0000', '#ffc800', '#ff6400']
    colorful_colors = ['#ff0000', '#ff6400', '#ffc800', '#00ff00', '#0000ff', '#b800ff', '#ff00c8', '#8c4100']
    w, h = canvas.winfo_width(), canvas.winfo_height()
    sleep(1)
    for _ in range(100):
        for _ in range(10):
            x, y = randint(0, w), randint(0, h)
            canvas.create_rectangle(x, y, x + 150, y + 100, fill=choice(error_colors), outline=choice(error_colors), width=5)
            canvas.create_text(x + 75, y + 50, text='错误', fill='white', font=('Arial', 50, 'bold'))
        for _ in range(5):
            x, y = randint(0, w), randint(0, h)
            canvas.create_oval(x, y, x + 50, y + 50, fill=choice(colorful_colors), outline=choice(colorful_colors), width=5)
        root.update()
    canvas.delete('all')
    for _ in range(100):
        x, y = randint(0, w), randint(0, h)
        canvas.create_rectangle(x, y, x + 150, y + 100, fill=choice(error_colors), outline=choice(error_colors), width=5)
        canvas.create_text(x + 75, y + 50, text='错误', fill='white', font=('Arial', 50, 'bold'))
        x, y = randint(0, w), randint(0, h)
        canvas.create_oval(x, y, x + 50, y + 50, fill=choice(colorful_colors), outline=choice(colorful_colors), width=5)
    for _ in range(100):
        for _ in range(3):
            x, y = randint(0, w), randint(0, h)
            canvas.create_polygon(x, y, x + randint(-200, 200), y + randint(-200, 200), x + randint(-200, 200), y + randint(-200, 200), x, y, fill=choice(error_colors), outline=choice(error_colors), width=5)
            canvas.create_text(x, y, text='错误', fill='black', font=('Arial', 50, 'bold'))
            root.update()
    canvas.delete('all')
    for _ in range(100):
        for x in range(0, w, 10):
            for y in range(0, h, 10):
                if randint(0, 3) >= 1:
                    canvas.create_rectangle(x, y, x + 10, y + 10, fill='white', width=0)
                else:
                    canvas.create_rectangle(x, y, x + 10, y + 10, fill=choice(colorful_colors), width=0)
        root.update()
        sleep(0.1)
        canvas.delete('all')
    canvas.create_rectangle(0, 0, w, h, fill='blue', outline='blue')
    root.update()
    sleep(0.5)
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
    root.quit()


root = tk.Tk()
root.title('电脑病毒模拟器')

canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

title = canvas.create_text(400, 200, text='电脑病毒模拟器', fill='white', font=('Arial', 50, 'bold'))
start_btn = canvas.create_text(400, 400, text='开始动画', fill='white', font=('Arial', 50))
note = canvas.create_text(400, 500, text='该动画不适合光敏性癫痫患者观看, 造成的后果由使用者负责, 作者概不负责!', fill='white', font=('Arial', 20))
canvas.tag_bind(start_btn, '<ButtonPress-1>', start_press)
canvas.tag_bind(start_btn, '<ButtonRelease-1>', start)

root.focus_force()
root.mainloop()
