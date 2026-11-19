import tkinter as tk
from random import randint
import math


class Star:
    def __init__(self):
        w, h = canvas.winfo_screenwidth(), canvas.winfo_screenheight()
        self.x = randint(0, w)
        self.y = randint(0, h)
        self.star = canvas.create_oval(self.x, self.y, self.x + 5, self.y + 5, fill='white', width=0)
        self.brightness = randint(0, 255)
        self.status = randint(0, 1)
        root.after(100, self.flash)

    def flash(self):
        if self.status == 1:
            if self.brightness > 0:
                self.brightness -= 1
            else:
                self.status = 0
        else:
            if self.brightness < 255:
                self.brightness += 1
            else:
                self.status = 1
        hex = rgb_to_hex(self.brightness, self.brightness, self.brightness)
        canvas.itemconfig(self.star, fill=hex)
        root.after(10, self.flash)


class Meteor:
    def __init__(self):
        w, h = canvas.winfo_width(), canvas.winfo_height()
        self.x = randint(0, w)
        self.y = randint(0, h)
        self.angle = randint(0, 360)
        self.meteor = canvas.create_oval(self.x, self.y, self.x + 5, self.y + 5, fill='white', width=0)
        self.step = 0
        root.after(100, self.move)

    def move(self):
        x, y = cal_angle_and_xy(self.angle, 10)
        canvas.move(self.meteor, x, y)
        self.x, self.y, _, _ = canvas.coords(self.meteor)
        MeteorTail(self.x, self.y)
        self.step += 1
        if self.step >= 100:
            canvas.delete(self.meteor)
            return
        root.after(10, self.move)


class MeteorTail:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.brightness = 255
        self.tail = canvas.create_oval(self.x, self.y, self.x + 5, self.y + 5, fill='white', width=0)
        root.after(10, self.dark)

    def dark(self):
        if self.brightness < 0:
            canvas.delete(self.tail)
            return
        self.brightness -= 5
        hex = rgb_to_hex(self.brightness, self.brightness, self.brightness)
        canvas.itemconfig(self.tail, fill=hex)
        root.after(10, self.dark)


def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


def create_meteor():
    Meteor()
    root.after(1000, create_meteor)


root = tk.Tk()
root.title('星空屏保')
root.configure(background='#000015')

canvas = tk.Canvas(root, width=800, height=600, bg='#000015')
canvas.pack(fill=tk.BOTH, expand=True)
for _ in range(300):
    Star()

root.after(2000, create_meteor)
root.bind('<Escape>', lambda e: root.quit())
root.attributes('-fullscreen', True)
root.focus_force()
root.mainloop()
