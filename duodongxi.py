import tkinter as tk
from random import randint, choice
from tkinter import messagebox
import math

fail = False
delay = 1000
time = 0
stones = []
pause = False

try:
    with open('/Users/luojingfeng/Desktop/duodongxi_framework/duodongxi_sco.txt', 'r') as file:
        high_time = int(file.read())
except FileNotFoundError:
    high_time = 0


class Player:
    def __init__(self, speed):
        self.x, self.y = 350, 350
        self.speed = speed
        self.size = 20
        self.player = canvas.create_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill='white', outline='white', width=0)
        root.bind('<Up>', lambda e: self.move(0))
        root.bind('<Down>', lambda e: self.move(180))
        root.bind('<Left>', lambda e: self.move(270))
        root.bind('<Right>', lambda e: self.move(90))
        root.bind('w', lambda e: self.move(0))
        root.bind('s', lambda e: self.move(180))
        root.bind('a', lambda e: self.move(270))
        root.bind('d', lambda e: self.move(90))

    def update(self):
        canvas.delete(self.player)
        if fail:
            self.player = canvas.create_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill='red', outline='red', width=0)
        else:
            self.player = canvas.create_rectangle(self.x - self.size, self.y - self.size, self.x + self.size, self.y + self.size, fill='white', outline='white', width=0)

    def move(self, angle):
        if not fail and not pause:
            if angle == 0:
                self.y -= self.speed
            if angle == 90:
                self.x += self.speed
            if angle == 180:
                self.y += self.speed
            if angle == 270:
                self.x -= self.speed
        if self.x < -30:
            self.x = 700
        if self.x > 700:
            self.x = -30
        if self.y < -30:
            self.y = 700
        if self.y > 700:
            self.y = -30
        self.update()


class Stone:
    def __init__(self, speed):
        spawn_list = [(randint(0, 700), 0), (randint(0, 700), 700), (0, randint(0, 700)), (700, randint(0, 700))]
        self.x, self.y = choice(spawn_list)
        if self.x <= 350:
            self.bx = speed
        if self.x > 350:
            self.bx = -speed
        if self.y <= 350:
            self.by = speed
        if self.y > 350:
            self.by = -speed
        self.speed = speed
        self.stone = canvas.create_oval(self.x - 30, self.y - 30, self.x + 30, self.y + 30, fill='#c8c8c8', outline='white')
        root.after(100, self.move)

    def move(self):
        global fail, high_time
        if not pause:
            canvas.move(self.stone, self.bx, self.by)
        if collision(self.stone, player.player):
            fail = True
            player.update()
            root.bind('<Return>', try_again)
            if time > high_time:
                try:
                    with open('/Users/luojingfeng/Desktop/duodongxi_framework/duodongxi_sco.txt', 'w') as file:
                        file.write(str(time))
                        high_time = time
                    messagebox.showinfo('新纪录!', '你达成了新纪录,已保存!')
                except BaseException as e:
                    print(e)
                    messagebox.showerror('新纪录保存失败', e)
            time_text.update()
        if not fail:
            root.after(10, self.move)


class TimeText:
    def __init__(self):
        self.text = canvas.create_text(20, 20, text=str(time), font=('Arial', 40), anchor=tk.NW)
        self.high_text = canvas.create_text(20, 70, text='high:%d' % high_time, font=('Arial', 20), anchor=tk.NW)

    def update(self):
        canvas.delete(self.text)
        canvas.delete(self.high_text)
        self.text = canvas.create_text(20, 20, text=str(time), font=('Arial', 40), anchor=tk.NW)
        self.high_text = canvas.create_text(20, 70, text='high:%d' % high_time, font=('Arial', 20), anchor=tk.NW)


class Pong:
    def __init__(self, cx, cy, px, py, speed):
        self.speed = speed
        self.bx, self.by = cal_angle_and_xy(get_angle(px, py, cx, cy), speed)
        self.pong = canvas.create_oval(px, py, px + 10, py + 10, fill='yellow', outline='yellow')
        root.after(10, self.move)

    def move(self):
        canvas.move(self.pong, self.bx, self.by)
        for stone in stones:
            if collision(self.pong, stone):
                canvas.delete(stone)
                canvas.delete(self.pong)
                return
        root.after(10, self.move)


def auto_create_stone():
    if not fail:
        if not pause:
            stones.append(Stone(2).stone)
        root.after(delay, auto_create_stone)


def count_time():
    global delay, time
    if not fail and not pause:
        delay -= 5
        time += 1
    time_text.update()
    root.after(1000, count_time)


def collision(a, b):
    try:
        coords = canvas.coords(a)
        collide = canvas.find_overlapping(*coords)
        collide_list = list(collide)
        return b in collide_list
    except:
        return False


def try_again(event):
    global fail, time, delay
    fail = False
    delay = 1000
    time = 0
    time_text.update()
    player.update()
    for stone in stones:
        canvas.delete(stone)
    root.unbind('<Return>')
    root.after(delay, auto_create_stone)


def set_pause(event):
    global pause
    pause = not pause


def pong(event):
    Pong(event.x, event.y, player.x, player.y, 5)


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


def get_angle(start_x, start_y, end_x, end_y):
    dx = end_x - start_x
    dy = end_y - start_y
    rad = math.atan2(dy, dx)
    angle = math.degrees(rad)
    result_angle = angle + 90
    if result_angle < 0:
        result_angle += 360
    return result_angle


root = tk.Tk()
root.title('躲东西射东西')

canvas = tk.Canvas(root, width=700, height=700, bg='black')
canvas.pack()

player = Player(30)
time_text = TimeText()

root.bind('p', set_pause)
canvas.bind('<Button-1>', pong)
root.after(1000, auto_create_stone)
root.after(1000, count_time)

root.focus_force()
root.mainloop()
