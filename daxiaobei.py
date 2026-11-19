import tkinter as tk
from random import choice, randint
from time import sleep

sco = 0
fail = 0
left_time = 60
pause = False


def create_mouse():
    if not pause:
        x, y = choice(holes_xy)
        mouse = canvas.create_image(x, y, image=lwb_img)
        canvas.tag_bind(mouse, '<Button-1>', lambda event: die_mouse(mouse, x, y))
        root.after(randint(1000, 4000), down_mouse, mouse)
    root.after(700, create_mouse)


def del_mouse(mouse):
    canvas.delete(mouse)


def die_mouse(mouse, x, y):
    global sco
    if not pause:
        sco += 1
        del_mouse(mouse)
        mouse = canvas.create_image(x, y, image=lwb_bon_img)
        root.update()
        sleep(0.1)
        update_sco_text()
        del_mouse(mouse)


def down_mouse(mouse):
    global fail
    if mouse in canvas.find_all():
        if pause:
            root.after(1000, down_mouse, mouse)
            return
        del_mouse(mouse)
        fail += 1
        update_fail_text()


def update_sco_text():
    global sco_text
    canvas.delete(sco_text)
    sco_text = canvas.create_text(20, 20, text=str(sco), font=('Arial', 50, 'bold'), fill='yellow', anchor=tk.NW)


def update_fail_text():
    global fail_text
    canvas.delete(fail_text)
    fail_text = canvas.create_text(780, 20, text=str(fail), font=('Arial', 50, 'bold'), fill='red', anchor=tk.NE)


def start(event):
    global sco_text, fail_text, start_btn, time_text
    canvas.delete(start_btn)
    start_btn = canvas.create_text(400, 450, text='开始', font=('Arial', 70, 'bold'), fill='red', anchor=tk.CENTER)
    root.update()
    sleep(0.1)
    canvas.delete(start_btn)
    canvas.delete(title)
    canvas.delete(limit_time_btn)
    for x, y in holes_xy:
        canvas.create_rectangle(x - 50, y - 30, x + 50, y + 30, fill='#552d00', outline='#552d00')
    sco_text = canvas.create_text(20, 20, text=str(sco), font=('Arial', 50, 'bold'), fill='yellow', anchor=tk.NW)
    fail_text = canvas.create_text(780, 20, text=str(fail), font=('Arial', 50, 'bold'), fill='red', anchor=tk.NE)
    time_text = canvas.create_text(20, 70, text='time:%d' % round(left_time), font=('Arial', 30, 'bold'), fill='green', anchor=tk.NW)
    if limit_time:
        root.after(1000, count_time)
    root.bind('p', set_pause)
    root.after(2000, create_mouse)


def set_limit_time(event):
    global limit_time, limit_time_btn
    canvas.delete(limit_time_btn)
    limit_time_btn = canvas.create_text(400, 300, text='限时60秒:%s' % ('开' if limit_time else '关'), font=('Arial', 50, 'bold'), fill='red', anchor=tk.CENTER)
    root.update()
    sleep(0.1)
    limit_time = not limit_time
    canvas.delete(limit_time_btn)
    limit_time_btn = canvas.create_text(400, 300, text='限时60秒:%s' % ('开' if limit_time else '关'), font=('Arial', 50, 'bold'), fill='blue', anchor=tk.CENTER)
    canvas.tag_bind(limit_time_btn, '<Button-1>', set_limit_time)


def count_time():
    global left_time
    if not pause:
        left_time -= 0.01
        if left_time <= 0:
            root.after(10, times_up)
        update_time_text()
    root.after(10, count_time)


def times_up():
    global pause
    pause = True
    canvas.create_text(400, 300, text='时间到!', font=('Arial', 100, 'bold'), fill='green', anchor=tk.CENTER)


def set_pause(event):
    global pause
    pause = not pause


def update_time_text():
    global time_text
    canvas.delete(time_text)
    time_text = canvas.create_text(20, 70, text='time:%d' % round(left_time), font=('Arial', 30, 'bold'), fill='green', anchor=tk.NW)


root = tk.Tk()
root.title('打肖北简易版')
lwb_img = tk.PhotoImage(file='/Users/luojingfeng/Desktop/素材/罗文彬.gif')
lwb_bon_img = tk.PhotoImage(file='/Users/luojingfeng/Desktop/素材/罗文彬被打.gif')

holes_xy = [(100, 200), (250, 200), (400, 200), (550, 200), (700, 200), (170, 400), (320, 400), (470, 400), (620, 400)]
canvas = tk.Canvas(root, width=800, height=600, bg='#804000')
canvas.pack()

title = canvas.create_text(400, 150, text='打肖北简易版', font=('Arial', 100, 'bold'), fill='green', anchor=tk.CENTER)
limit_time = False
limit_time_btn = canvas.create_text(400, 300, text='限时60秒:%s' % ('开' if limit_time else '关'), font=('Arial', 50, 'bold'), fill='blue', anchor=tk.CENTER)
start_btn = canvas.create_text(400, 450, text='开始', font=('Arial', 70, 'bold'), fill='yellow', anchor=tk.CENTER)
canvas.tag_bind(start_btn, '<Button-1>', start)
canvas.tag_bind(limit_time_btn, '<Button-1>', set_limit_time)

root.focus_force()
root.mainloop()
