import tkinter as tk
from random import randint, choice
import math, time
from time import sleep

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
balls = []
fps_count = 0
fps = '?'
fps_time = time.time()


class Ball:
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.distance = 10
        self.ball = canvas.create_oval(self.x, self.y, self.x + self.w, self.y + self.h, fill=self.color)
        self.angle = randint(0, 360)
        balls.append(self.ball)
        root.after(100, self.peng)
        root.after(20, self.move)

    def peng(self):
        peng = False
        for i in collision(self.ball):
            if i in balls and i != self.ball:
                peng = True
                break

        if peng:
            self.angle = randint(0, 360)

    def move(self):
        if self.x > 800 - self.w:
            self.angle = randint(180, 359)
        if self.x < 0:
            self.angle = randint(0, 180)
        if self.y > 600 - self.h:
            if randint(0, 1) == 0:
                self.angle = randint(0, 90)
            else:
                self.angle = randint(0, 90)
        if self.y < 0:
            self.angle = 180
        x, y = cal_angle_and_xy(angle=self.angle, distance=self.distance)
        canvas.move(self.ball, x, y)
        self.x, self.y, _, _ = canvas.coords(self.ball)
        root.after(20, self.move)


class FpsText:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.text = canvas.create_text(x, y, text=fps, font=('Arial', 20), fill='black', anchor=tk.NW)
        root.after(500, self.update)

    def update(self):
        canvas.itemconfig(self.text, text=fps)
        root.after(500, self.update)


def create():
    Ball(choice(colors), randint(0, 800), randint(0, 600), 50, 50)
    root.after(1000 - speed.get(), create)


def start():
    start_btn.pack_forget()
    speed_scale.pack(fill=tk.X, expand=True)
    root.after(100, create)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


def safequit():
    root.is_destroy = True
    root.destroy()


root = tk.Tk()
root.title('卡电脑-new')

speed = tk.IntVar(value=0)

canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()

start_btn = tk.Button(root, text='START', command=start, font=('Arial', 20))
start_btn.pack(fill=tk.X, expand=True)

speed_scale = tk.Scale(root, variable=speed, from_=0, to=999, font=('Arial', 20), orient=tk.HORIZONTAL)

FpsText(10, 10)

root.is_destroy = False
root.protocol('WM_DELETE_WINDOW', safequit)
root.focus_force()

while True:
    if root.is_destroy:
        break
    root.update()
    sleep(0.006)
    fps_count += 1
    if time.time() - fps_time > 0.5:
        fps_time = time.time()
        fps = fps_count * 2
        fps_count = 0
