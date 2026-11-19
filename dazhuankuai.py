import tkinter as tk
from random import choice, randint
import math

bricks = []
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
bx = 400
by = 520
bcolor = choice(colors)
fx = 350
fy = 550
angle = 45
speed = 3
fail = False
try_again_count = 0
bricks_len = 0
sco = 0
ball_collision_count = 0
file_bricks = []
max_ball_collision_count = 2
try:
    with open('dazhuankuai-record.txt', 'r') as file:
        try:
            for line in file:
                if 'None' not in line:
                    for i in line.split(','):
                        if i != '\n':
                            file_bricks.append(i)
        except Exception:
            raise ValueError
except FileNotFoundError:
    pass
except Exception:
    print('计分文件损坏,将启用新游戏')
    print('输入任意内容继续...')
    input('>')
    file_bricks = []

root = tk.Tk()
root.title('打砖块')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
ww, wh = 800, 600
x, y = (w - ww) / 2, (h - wh) / 2
root.geometry('+%d+%d' % (x, y))

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()


def move_ball():
    global ball, bx, by, angle, bricks, canvas, board, fail, bcolor, speed, sco, ball_collision_count, max_ball_collision_count
    for b in collision(ball):
        if b in bricks:
            bricks.remove(b)
            canvas.delete(b)
            sco += 1
            if ball_collision_count >= max_ball_collision_count:
                angle = randint(135, 225)
            else:
                ball_collision_count += 1
            bcolor = choice(colors)
            if bricks_len - sco <= 0:
                root.after(10, del_ask_win)
        if b == board:
            ball_collision_count = 0
            if randint(0, 1) == 0:
                angle = randint(315, 360)
            else:
                angle = randint(0, 45)
            bcolor = choice(colors)
    if by <= 20:
        if angle == 0:
            angle = 180
        elif angle < 180:
            angle = randint(90, 180)
        elif angle > 180:
            angle = randint(180, 360)
        by = 25
    if bx <= 20:  # 碰左
        print(1)
        print(bx)
        if angle < 180:
            angle = randint(90, 180)
        else:
            angle = randint(180, 270)
        bx = 25
    if bx >= canvas.winfo_width() - 20:  # 碰右
        print(2)
        print(canvas.winfo_width() - 30 - bx)
        if angle < 80:
            angle = randint(270, 360)
        else:
            angle = randint(180, 270)
        bx = canvas.winfo_width() - 25
    if by >= canvas.winfo_height() + 20:
        fail = True
    x, y = cal_angle_and_xy(angle, speed)
    bx, by = bx + x, by + y
    update_ball()
    root.after(10, move_ball)


def board_left(event):
    global fx
    fx -= 50
    update_board()


def board_right(event):
    global fx
    fx += 50
    update_board()


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


def update_ball():
    global ball, bx, by, canvas
    canvas.delete(ball)
    ball = canvas.create_oval(bx, by, bx + 40, by + 40, fill=bcolor)


def update_board():
    global canvas, board
    canvas.delete(board)
    board = canvas.create_rectangle(fx, fy, fx + 200, fy + 20, fill='yellow')


def update_text():
    global text, sco, bricks_len
    canvas.delete(text)
    text = canvas.create_text(20, 20, fill='white', text='已打%d个砖块,剩余%d个砖块,已重试%d次' % (sco, bricks_len - sco, try_again_count), font=('Arial', 20), anchor=tk.NW)
    root.after(100, update_text)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def try_again(event):
    global fail, by, bx, fx, try_again_count
    if fail:
        fail = False
        bx = fx + 100
        by = 520
        try_again_count += 1


def fast(event):
    global speed
    speed = 4


def slow(event):
    global speed
    speed = 3


def safequit(event=None):
    global bricks
    xys = []
    if bricks_len - sco > 0:
        for i in bricks:
            x1, y1, _, _ = canvas.coords(i)
            xys.append((x1, y1))
        xystext = ''
        for i in xys:
            a, b = i
            xystext = xystext + str(a) + '|' + str(b) + ','
        xystext = xystext.rstrip(',')
        try:
            with open('dazhuankuai-record.txt', 'w') as file:
                print(xystext)
                file.write(xystext)
        except Exception:
            pass
    else:
        xystext = 'None'
        try:
            with open('dazhuankuai-record.txt', 'w') as file:
                print(xystext)
                file.write(xystext)
        except Exception:
            pass
    root.quit()


bricks_size = 25
if not file_bricks:
    for x in range(50, 750, bricks_size):
        for y in range(50, 400, bricks_size):
            bricks.append(canvas.create_rectangle(x, y, x + bricks_size, y + bricks_size, fill=choice(colors)))
            bricks_len += 1
else:
    for i in file_bricks:
        try:
            x, y = i.split('|')
            bricks.append(canvas.create_rectangle(float(x), float(y), float(x) + bricks_size, float(y) + bricks_size, fill=choice(colors)))
            bricks_len += 1
        except Exception:
            print('计分文件损坏,将启用新游戏')
            print('输入任意内容继续...')
            input('>')
            for x in range(50, 750, bricks_size):
                for y in range(50, 400, bricks_size):
                    bricks.append(canvas.create_rectangle(x, y, x + bricks_size, y + bricks_size, fill=choice(colors)))
                    bricks_len += 1


def win():
    win_text = canvas.create_text(400, 300, text='恭喜通关', font=('Arial', 100), anchor=tk.CENTER)
    canvas.tag_raise(win_text)
    root.bind('<Button-1>', safequit)


ball = canvas.create_oval(bx, by, bx + 40, by + 40, fill=bcolor)
board = canvas.create_rectangle(fx, fy, fx + 200, fy + 20, fill='yellow')
text = canvas.create_text(20, 20, fill='white', text='正在初始化,暂无文本', font=('Arial', 20), anchor=tk.NW)

root.bind('a', board_left)
root.bind('d', board_right)
root.bind('<Left>', board_left)
root.bind('<Right>', board_right)
root.bind('<KeyPress-f>', fast)
root.bind('<KeyRelease-f>', slow)
root.bind('<KeyPress-space>', fast)
root.bind('<KeyRelease-space>', slow)
root.bind('r', try_again)
root.bind('<Escape>', safequit)
root.protocol('WM_DELETE_WINDOW', safequit)

root.after(100, move_ball)
root.after(200, update_text)

root.focus_force()
root.mainloop()
