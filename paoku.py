import sys
import tkinter as tk
from random import randint
from tkinter import simpledialog as sd

bx = 400
fail = False
sco = 0
speed = 10
pause = False


def update_people():
    global people
    canvas.delete(people)
    if fail:
        people = canvas.create_rectangle(bx - 30, 540, bx + 30, 600, fill='gray')
        fail_tip()
    else:
        people = canvas.create_rectangle(bx - 30, 540, bx + 30, 600, fill='red')


def left(event):
    global bx
    if not fail and not pause:
        bx -= 60
    if bx < 30:
        bx = 30
    update_people()


def right(event):
    global bx
    if not fail and not pause:
        bx += 60
    if bx > 770:
        bx = 770
    update_people()


def create_wall():
    if not pause:
        x, y = randint(30, 770), 0
        wall = canvas.create_rectangle(x - 30, y, x + 30, y + 60, fill='green')
        root.after(10, move_wall, x, y, wall)
    if fail:
        update_people()
    else:
        root.after(randint(700 // (speed // 10), 1300 // (speed // 10)), create_wall)


def move_wall(x, y, wall):
    global fail
    if not fail:
        if not pause:
            y += speed / 10 * 2
        if people in collision(wall):
            fail = True
            update_people()
            return
        canvas.delete(wall)
        if y < 540:
            wall = canvas.create_rectangle(x - 30, y, x + 30, y + 60, fill='green')
            root.after(10, move_wall, x, y, wall)


def create_coin():
    if not pause:
        x, y = randint(30, 770), 0
        coin = canvas.create_oval(x - 30, y, x + 30, y + 60, fill='yellow')
        root.after(10, move_coin, x, y, coin)
    if fail:
        update_people()
    else:
        root.after(randint(700 // (speed // 10), 1300 // (speed // 10)), create_coin)


def move_coin(x, y, coin):
    global sco
    if not fail:
        if not pause:
            y += speed / 10 * 2
        if people in collision(coin):
            sco += 1
            update_sco_text()
            canvas.delete(coin)
            return
        canvas.delete(coin)
        if y < 600:
            coin = canvas.create_oval(x - 30, y, x + 30, y + 60, fill='yellow')
            root.after(10, move_coin, x, y, coin)


def update_sco_text():
    global sco_text
    canvas.delete(sco_text)
    sco_text = canvas.create_text(20, 20, text=str(sco), font=('Arial', 50, 'bold'), fill='white', anchor=tk.NW)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def start(event):
    global people, sco_text, pause, fail, sco
    pause = False
    fail = False
    sco = 0
    canvas.delete('all')
    people = canvas.create_rectangle(bx - 30, 540, bx + 30, 600, fill='red')
    sco_text = canvas.create_text(20, 20, text=str(sco), font=('Arial', 50, 'bold'), fill='white', anchor=tk.NW)
    root.bind('<Left>', left)
    root.bind('<Right>', right)
    root.bind('p', set_pause)
    canvas.bind('<B1-Motion>', set_bx)
    root.after(1000, create_wall)
    root.after(1000, create_coin)


def minus_speed(event):
    global speed
    speed -= 1
    if speed < 10:
        speed = 10
    update_speed_text()


def plus_speed(event):
    global speed
    speed += 1
    update_speed_text()


def update_speed_text():
    global speed_text
    canvas.delete(speed_text)
    speed_text = canvas.create_text(400, 200, text='速度:%d' % speed, font=('Arial', 70, 'bold'), fill='white', anchor=tk.CENTER)
    canvas.tag_bind(speed_text, '<Button-1>', set_speed)


def set_speed(event):
    global speed
    user_input = sd.askinteger(title='设置速度', prompt='请输入设置的速度', initialvalue=speed, minvalue=10)
    speed = user_input
    update_speed_text()


def fail_tip():
    canvas.create_text(400, 300, text='你挂了!得分%d分!按R重新开始' % sco, font=('Arial', 50, 'bold'), anchor=tk.CENTER, fill='red')
    root.bind('r', re_try)


def set_bx(event):
    global bx
    if not fail and not pause:
        bx = (event.x // 60) * 60
        if bx < 30:
            bx = 30
        if bx > 770:
            bx = 770
        update_people()


def re_try(event):
    root.unbind('r')
    start(None)


def set_pause(event):
    global pause
    pause = not pause


root = tk.Tk()
root.title('暂无名字')

canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack()

minus_speed_btn = canvas.create_text(150, 200, text='-', font=('Arial', 100, 'bold'), fill='white', anchor=tk.CENTER)
plus_speed_btn = canvas.create_text(650, 200, text='+', font=('Arial', 100, 'bold'), fill='white', anchor=tk.CENTER)
speed_text = canvas.create_text(400, 200, text='速度:%d' % speed, font=('Arial', 70, 'bold'), fill='white', anchor=tk.CENTER)
start_btn = canvas.create_text(400, 400, text='开始', font=('Arial', 70, 'bold'), fill='white', anchor=tk.CENTER)
canvas.tag_bind(start_btn, '<Button-1>', start)
canvas.tag_bind(minus_speed_btn, '<Button-1>', minus_speed)
canvas.tag_bind(plus_speed_btn, '<Button-1>', plus_speed)
canvas.tag_bind(speed_text, '<Button-1>', set_speed)

root.bind('<Escape>', lambda event: root.quit())

root.focus_force()
root.mainloop()
sys.exit()
