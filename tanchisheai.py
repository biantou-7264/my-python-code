import tkinter as tk
from random import randint

bx = 0
by = 0
if randint(0, 3) == 0:
    sfx = randint(50, 700 - 50)
    sfy = randint(50, 500 - 50)
    fx = 1000000
    fy = 1000000
else:
    sfx = 1000000
    sfy = 1000000
    fx = randint(50, 700 - 50)
    fy = randint(50, 500 - 50)
angle = 90
sco = 0
snake_bodys = []
try:
    with open('tanchishe-sco-ai.txt', 'r') as file:
        sco = int(file.read())
except FileNotFoundError:
    try:
        with open('tanchishe-sco-ai.txt', 'w') as file:
            file.write(str(sco))
    except BaseException as e:
        print(type(e).__name__)
        print(e)
        raise SystemExit(1)
except BaseException as e:
    print(type(e).__name__)
    print(e)
    raise SystemExit(1)
speed = 4


def move():
    global bx, by, angle, snake, canvas, sco
    if angle == 90:
        if bx > canvas.winfo_width() - 20:
            bx = 20
        else:
            bx += speed
    elif angle == 180:
        if by > canvas.winfo_height() - 20:
            by = 20
        else:
            by += speed
    elif angle == 270:
        if bx < 5:
            bx = canvas.winfo_width() - 20
        else:
            bx -= speed
    elif angle == 0:
        if by < 5:
            by = canvas.winfo_height() - 20
        else:
            by -= speed
    else:
        angle = 90
    if snake_love_food():
        sco += 1
        update_sco_text()
        random_food()
    if snake_love_super_food():
        sco += 5
        update_sco_text()
        random_food()
    update_snake()
    root.after(10, move)


def update_snake():
    global bx, by, snake, canvas
    canvas.delete(snake)
    snake = canvas.create_rectangle(bx, by, bx + 20, by + 20, fill='red')


def update_food():
    global fx, fy, food, canvas, super_food
    canvas.delete(food)
    canvas.delete(super_food)
    food = canvas.create_rectangle(fx, fy, fx + 20, fy + 20, fill='#ffc800')
    super_food = canvas.create_rectangle(sfx, sfy, sfx + 20, sfy + 20, fill='#ffff64')


def update_sco_text():
    global sco, sco_text
    canvas.delete(sco_text)
    sco_text = canvas.create_text(30, 30, text=str(sco), font=('Arial', 50, 'bold'), fill='#c8c8c8', anchor=tk.NW)


def up(event=None):
    global angle
    angle = 0


def down(event=None):
    global angle
    angle = 180


def left(event=None):
    global angle
    angle = 270


def right(event=None):
    global angle
    angle = 90


def clone():
    global bx, by, sco, speed, snake_bodys
    new_snake = canvas.create_rectangle(bx, by, bx + 20, by + 20, fill='green')
    canvas.lower(new_snake)
    snake_bodys.append(new_snake)
    root.after(50, clone)
    root.after((sco + 1) * 125, del_new_snake, new_snake)


def del_new_snake(new_snake):
    global snake_bodys
    try:
        snake_bodys.remove(new_snake)
    except ValueError:
        pass
    canvas.delete(new_snake)


def snake_love_food():
    global food, snake, canvas
    x1, y1, x2, y2 = canvas.bbox(snake)
    overlap_items = canvas.find_overlapping(x1, y1, x2, y2)
    return food in overlap_items


def snake_love_super_food():
    global super_food, snake, canvas
    x1, y1, x2, y2 = canvas.bbox(snake)
    overlap_items = canvas.find_overlapping(x1, y1, x2, y2)
    return super_food in overlap_items


def top_and_full():
    global root
    root.attributes('-topmost', True)
    root.attributes('-fullscreen', True)
    root.after(200, top_and_full)


def autosave():
    global sco
    try:
        with open('tanchishe-sco-ai.txt', 'w') as file:
            file.write(str(sco))
    except BaseException as e:
        print(type(e).__name__)
        print(e)
    root.after(5000, autosave)


def save_and_quit(event=None):
    global root
    autosave()
    root.quit()


def ai_play():
    if sfx < 100000:
        if abs(bx - sfx) > 10:
            if bx < sfx:
                right()
            else:
                left()
        else:
            if by < sfy:
                down()
            else:
                up()
    else:
        if abs(bx - fx) > 10:
            if bx < fx:
                right()
            else:
                left()
        else:
            if by < fy:
                down()
            else:
                up()
    root.after(10, ai_play)


def random_food(event=None):
    global fx, fy, sfx, sfy
    if randint(0, 3) == 0:
        sfx = randint(50, canvas.winfo_width() - 50)
        sfy = randint(50, canvas.winfo_height() - 50)
        fx = 1000000
        fy = 1000000
    else:
        sfx = 1000000
        sfy = 1000000
        fx = randint(50, canvas.winfo_width() - 50)
        fy = randint(50, canvas.winfo_height() - 50)
    update_food()


root = tk.Tk()
canvas = tk.Canvas(root, bg='darkblue', width=700, height=500)
canvas.pack(fill=tk.BOTH, expand=True)

snake = canvas.create_rectangle(bx, by, bx + 20, by + 20, fill='red')
food = canvas.create_rectangle(fx, fy, fx + 20, fy + 20, fill='#ffc800')
super_food = canvas.create_rectangle(sfx, sfy, sfx + 20, sfy + 20, fill='#ffff64')
sco_text = canvas.create_text(30, 30, text=str(sco), font=('Arial', 50, 'bold'), fill='#c8c8c8', anchor=tk.NW)

root.bind('<Escape>', save_and_quit)
root.protocol('WM_DELETE_WINDOW', save_and_quit)

root.focus_force()
root.after(500, move)
root.after(500, clone)
root.after(200, top_and_full)
root.after(300, autosave)
root.after(400, ai_play)

root.mainloop()
