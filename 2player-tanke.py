import tkinter as tk
from tkinter import simpledialog as sd
from time import time

tanks = []
init_hp = 100
last_press_q = 0
last_press_l = 0
press_q_count = 0
press_l_count = 0
ai = False


class Tank:
    def __init__(self, x, y, player, color, speed):
        global tanks
        self.x = x
        self.y = y
        self.player = player
        self.color = color
        self.angle = 90
        self.speed = speed
        self.hp = int(init_hp)
        self.fail = False
        self.tank = canvas.create_rectangle(self.x - 50, self.y - 25, self.x + 50, self.y + 25, fill=self.color)
        if player == 1:
            root.bind('w', self.up)
            root.bind('s', self.down)
            root.bind('a', self.left)
            root.bind('d', self.right)
            root.bind('<space>', self.pong)
        else:
            if not ai:
                root.bind('<Up>', self.up)
                root.bind('<Down>', self.down)
                root.bind('<Left>', self.left)
                root.bind('<Right>', self.right)
                root.bind('<Return>', self.pong)
        tanks.append(self.tank)

    def update(self):
        canvas.delete(self.tank)
        if not self.fail:
            if self.angle == 0:
                self.tank = canvas.create_rectangle(self.x - 25, self.y - 50, self.x + 25, self.y + 50, fill=self.color)
            if self.angle == 90:
                self.tank = canvas.create_rectangle(self.x - 50, self.y - 25, self.x + 50, self.y + 25, fill=self.color)
            if self.angle == 180:
                self.tank = canvas.create_rectangle(self.x - 25, self.y - 50, self.x + 25, self.y + 50, fill=self.color)
            if self.angle == 270:
                self.tank = canvas.create_rectangle(self.x - 50, self.y - 25, self.x + 50, self.y + 25, fill=self.color)
            if self.x < -10:
                self.x = 800
            if self.x > 810:
                self.x = 0
            if self.y < -10:
                self.y = 600
            if self.y > 610:
                self.y = 0

    def up(self, event):
        self.angle = 0
        self.y -= self.speed
        self.update()

    def down(self, event):
        self.angle = 180
        self.y += self.speed
        self.update()

    def left(self, event):
        self.angle = 270
        self.x -= self.speed
        self.update()

    def right(self, event):
        self.angle = 90
        self.x += self.speed
        self.update()

    def pong(self, event):
        if not self.fail:
            Pong(self.x, self.y, self.angle, 20, self.player)

    def oh(self, minus_hp):
        self.hp -= minus_hp
        if self.hp <= 0:
            self.fail = True
            self.update()
        ht1.update()
        ht2.update()


class Pong:
    def __init__(self, x, y, angle, speed, player):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.pong = canvas.create_rectangle(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill='black', outline='black')
        self.player = player
        self.is_bon = False
        root.after(10, self.move)

    def move(self):
        if not self.is_bon:
            if self.angle == 0:
                self.y -= self.speed
            if self.angle == 180:
                self.y += self.speed
            if self.angle == 270:
                self.x -= self.speed
            if self.angle == 90:
                self.x += self.speed
            self.update()
            root.after(10, self.move)

    def update(self):
        canvas.delete(self.pong)
        self.pong = canvas.create_rectangle(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill='black', outline='black')
        if self.player == 1 and p2.tank in collision(self.pong):
            canvas.delete(self.pong)
            self.is_bon = True
            p2.oh(5)
        if self.player == 2 and p1.tank in collision(self.pong):
            canvas.delete(self.pong)
            self.is_bon = True
            p1.oh(5)
        if self.is_bon:
            self.boom_animation(self.x, self.y)

    def boom_animation(self, x, y):
        temp = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='yellow', outline='red', width=5)
        root.after(10, self.boom_move, temp, 10, x, y)

    def boom_move(self, boom, size, x, y):
        canvas.delete(boom)
        size += 10
        if size > 100:
            return
        temp = canvas.create_oval(x - size, y - size, x + size, y + size, fill='yellow', outline='red', width=5)
        root.after(10, self.boom_move, temp, size, x, y)


class HpText:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        if player == 1:
            h = p1.hp
            a = tk.NW
        else:
            h = p2.hp
            a = tk.NE
        self.text = canvas.create_text(self.x, self.y, text=str(h), font=('Arial', 30), fill='white', anchor=a)

    def update(self):
        canvas.delete(self.text)
        if self.player == 1:
            h = p1.hp
            a = tk.NW
        else:
            h = p2.hp
            a = tk.NE
        self.text = canvas.create_text(self.x, self.y, text=str(h), font=('Arial', 30), fill='white', anchor=a)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def start(event):
    global p1, p2, ht1, ht2
    canvas.delete('all')
    p1 = Tank(200, 300, 1, 'red', 50)
    p2 = Tank(600, 300, 2, 'yellow', 50)
    ht1 = HpText(20, 20, 1)
    ht2 = HpText(780, 20, 2)
    root.bind('q', cheat_q)
    root.bind('l', cheat_l)


def ai_start(event):
    global p1, p2, ht1, ht2, ai
    ai = True
    canvas.delete('all')
    p1 = Tank(200, 300, 1, 'red', 50)
    p2 = Tank(600, 300, 2, 'yellow', 50)
    ht1 = HpText(20, 20, 1)
    ht2 = HpText(780, 20, 2)
    root.bind('q', cheat_q)
    root.bind('l', cheat_l)
    root.after(100, ai_move)
    root.after(100, ai_pong)


def set_init_hp(event):
    global init_hp
    user_input = sd.askinteger('设置初始血量', '请输入初始血量')
    if user_input is not None:
        init_hp = user_input
        canvas.itemconfig(init_hp_text, text='初始血量:%d' % init_hp)


def cheat_q(event):
    global last_press_q, press_q_count
    if press_q_count >= 5:
        if p2.hp > 10:
            p2.hp = 10
        ht2.update()
        press_q_count = 0
    else:
        if abs(last_press_q - time()) > 2:
            last_press_q = time()
            press_q_count = 1
        else:
            last_press_q = time()
            press_q_count += 1


def cheat_l(event):
    global last_press_l, press_l_count
    if press_l_count >= 5:
        if p1.hp > 10:
            p1.hp = 10
        ht1.update()
        press_l_count = 0
    else:
        if abs(last_press_l - time()) > 2:
            last_press_l = time()
            press_l_count = 1
        else:
            last_press_l = time()
            press_l_count += 1


def ai_move():
    if abs(p1.x - p2.x) > 20:
        if p1.x > p2.x:
            p2.right(None)
        else:
            p2.left(None)
    else:
        if p1.y > p2.y:
            p2.down(None)
        else:
            p2.up(None)
    root.after(400, ai_move)


def ai_pong():
    p2.pong(None)
    root.after(300, ai_pong)


root = tk.Tk()
root.title('双人坦克大战')

canvas = tk.Canvas(root, width=800, height=600, bg='green')
canvas.pack()

canvas.create_text(400, 200, text='双人坦克大战', font=('Arial', 70, 'bold'), fill='white', anchor=tk.CENTER)
init_hp_text = canvas.create_text(400, 300, text='初始血量:100', font=('Arial', 50), fill='white')
canvas.create_text(400, 350, text='点击可修改初始血量', font=('Arial', 20), fill='white', anchor=tk.CENTER)
start_btn = canvas.create_text(400, 430, text='开始', font=('Arial', 50), fill='white', anchor=tk.CENTER)
ai_start_btn = canvas.create_text(400, 500, text='AI模式开始', font=('Arial', 30), fill='white', anchor=tk.CENTER)
canvas.tag_bind(init_hp_text, '<Button-1>', set_init_hp)
canvas.tag_bind(start_btn, '<Button-1>', start)
canvas.tag_bind(ai_start_btn, '<Button-1>', ai_start)

root.focus_force()
root.mainloop()

"""
            留言条
玩家你好:
    告诉你一个小秘密:
    这个游戏有一个耍赖后门,
    连按5下Q可以把2p的血量变成10,
    连按5下L可以把1p的血量变成10.
                                    作者
                        2026年6月2日
"""
