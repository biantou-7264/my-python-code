import tkinter as tk
from random import choice
from msgbox import info

chesses = []
me_chesses = []
me_xy = []
player = 0
bot_xy = [(20, 20, 80, 80), (120, 20, 180, 80), (220, 20, 280, 80), (20, 120, 80, 180), (120, 120, 180, 180), (220, 120, 280, 180), (20, 220, 80, 280), (120, 120, 180, 180), (220, 220, 280, 280)]
bot_chesses = []
bot_chesses_xy = []
check_win_lines = [(0, 50, 300, 50), (0, 150, 300, 150), (0, 250, 300, 250), (50, 0, 50, 300), (150, 0, 150, 300), (250, 0, 250, 300), (0, 0, 300, 300), (300, 0, 0, 300)]

def me_down(event):
    global chesses, player, me_chesses
    if player == 0:
        if event.x < 100 and event.y < 100:
            if (20, 20, 80, 80) not in bot_chesses_xy:
                chess = canvas.create_oval(20, 20, 80, 80, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((20, 20, 80, 80))
            else:
                return
        if event.x > 100 and event.x < 200 and event.y < 100:
            if (120, 20, 180, 80) not in bot_chesses_xy:
                chess = canvas.create_oval(120, 20, 180, 80, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((120, 20, 180, 80))
            else:
                return
        if event.x > 200 and event.y < 100:
            if (220, 20, 280, 80) not in bot_chesses_xy:
                chess = canvas.create_oval(220, 20, 280, 80, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((220, 20, 280, 80))
            else:
                return

        if event.x < 100 and event.y < 200 and event.y > 100:
            if (20, 120, 80, 180) not in bot_chesses_xy:
                chess = canvas.create_oval(20, 120, 80, 180, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((20, 120, 80, 180))
            else:
                return
        if event.x > 100 and event.x < 200 and event.y < 200 and event.y > 100:
            if (120, 120, 180, 180) not in bot_chesses_xy:
                chess = canvas.create_oval(120, 120, 180, 180, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((120, 120, 180, 180))
            else:
                return
        if event.x > 200 and event.y < 200 and event.y > 100:
            if (220, 120, 280, 180) not in bot_chesses_xy:
                chess = canvas.create_oval(220, 120, 280, 180, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((220, 120, 280, 180))
            else:
                return

        if event.x < 100 and event.y < 300 and event.y > 200:
            if (20, 220, 80, 280) not in bot_chesses_xy:
                chess = canvas.create_oval(20, 220, 80, 280, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((20, 220, 80, 280))
            else:
                return
        if event.x > 100 and event.x < 200 and event.y < 300 and event.y > 200:
            if (120, 220, 180, 280) not in bot_chesses_xy:
                chess = canvas.create_oval(120, 220, 180, 280, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((120, 220, 180, 280))
            else:
                return
        if event.x > 200 and event.y < 300 and event.y > 200:
            if (220, 220, 280, 280) not in bot_chesses_xy:
                chess = canvas.create_oval(220, 220, 280, 280, fill='black', outline='white', width=5)
                chesses.append(chess)
                me_chesses.append(chess)
                me_xy.append((220, 220, 280, 280))
            else:
                return
        player = 1

        check_win()
        root.after(100, robot_down)

def robot_down():
    global player, bot_chesses
    if player == 1:
        xy = choice(bot_xy)
        if xy in me_xy:
            print(11)
            root.after(100, robot_down)
        else:
            x1, y1, x2, y2 = xy
            chess = canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text='X', fill='white', font=('Arial', 50, 'bold'))
            chesses.append(chess)
            bot_chesses.append(chess)
            bot_chesses_xy.append(xy)
            player = 0

def check_win():
    global player
    for xy in check_win_lines:
        x1, y1, x2, y2 = xy
        temp = canvas.create_line(x1, y1, x2, y2, fill='black', width=5)
        cols = collision(temp)
        a = 0
        b = 0
        for i in cols:
            if i in me_chesses:
                a += 1
            if i in bot_chesses:
                b += 1
        print('a=%d' % a)
        print('b=%d' % b)
        canvas.delete(temp)
        if a == 3:
            info(root, '人赢了', '好的')
            player = 2
            return
        if b == 3:
            info(root, '鸡赢了', '好的')
            player = 2
            return

def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


root = tk.Tk()
root.title('井字棋')

canvas = tk.Canvas(root, width=300, height=300, bg='black')
canvas.pack()

canvas.create_line(0, 100, 300, 100, fill='white', width=3)
canvas.create_line(0, 200, 300, 200, fill='white', width=3)
canvas.create_line(100, 0, 100, 300, fill='white', width=3)
canvas.create_line(200, 0, 200, 300, fill='white', width=3)

canvas.bind('<Button-1>', me_down)

root.focus_force()
root.mainloop()