import tkinter as tk
from random import randint


def up(event):
    global bx, by, sco, de_wall_status, direction, angle
    by -= GRID_SIZE
    angle = 90
    if (bx, by) in walls:
        if de_wall_status:
            canvas.delete(walls[(bx, by)])
            walls.pop((bx, by))
        else:
            by += GRID_SIZE
    if (bx, by) in coins:
        sco += 1
        try:
            canvas.delete(coins[(bx, by)])
            coins.pop((bx, by))
        except KeyError:
            pass
        update_sco_text()
    if by < 0:
        by = 0
    direction = 'up'
    update_people()
    de_wall_status = False


def down(event):
    global bx, by, sco, de_wall_status, direction, angle
    by += GRID_SIZE
    angle = 270
    if (bx, by) in walls:
        if de_wall_status:
            canvas.delete(walls[(bx, by)])
            walls.pop((bx, by))
        else:
            by -= GRID_SIZE
    if (bx, by) in coins:
        sco += 1
        try:
            canvas.delete(coins[(bx, by)])
            coins.pop((bx, by))
        except KeyError:
            pass
        update_sco_text()
    if by > canvas.winfo_height() - GRID_SIZE:
        by = canvas.winfo_height() - GRID_SIZE
    direction = 'down'
    update_people()
    de_wall_status = False


def left(event):
    global bx, by, sco, de_wall_status, direction, angle
    bx -= GRID_SIZE
    angle = 180
    if (bx, by) in walls:
        if de_wall_status:
            canvas.delete(walls[(bx, by)])
            walls.pop((bx, by))
        else:
            bx += GRID_SIZE
    if (bx, by) in coins:
        sco += 1
        try:
            canvas.delete(coins[(bx, by)])
            coins.pop((bx, by))
        except KeyError:
            pass
        update_sco_text()
    if bx < 0:
        bx = 0
    direction = 'left'
    update_people()
    de_wall_status = False


def right(event):
    global bx, by, sco, de_wall_status, direction, angle
    bx += GRID_SIZE
    angle = 0
    if (bx, by) in walls:
        if de_wall_status:
            canvas.delete(walls[(bx, by)])
            walls.pop((bx, by))
        else:
            bx -= GRID_SIZE
    if (bx, by) in coins:
        sco += 1
        try:
            canvas.delete(coins[(bx, by)])
            coins.pop((bx, by))
        except KeyError:
            pass
        update_sco_text()
    if bx > canvas.winfo_width():
        bx = canvas.winfo_width() - GRID_SIZE
    direction = 'right'
    update_people()
    de_wall_status = False


def update_people():
    global people
    canvas.delete(people)
    people = canvas.create_arc(bx, by, bx + GRID_SIZE, by + GRID_SIZE, start=angle + 30, extent=300, fill=PEOPLE_COLOR, outline=PEOPLE_COLOR)


def mainloop():
    global bx, by
    if bx % GRID_SIZE != 0:
        bx = (bx // GRID_SIZE) * GRID_SIZE
    if by % GRID_SIZE != 0:
        by = (by // GRID_SIZE) * GRID_SIZE
    root.after(100, mainloop)


def update_sco_text():
    global sco_text
    canvas.delete(sco_text)
    sco_text = canvas.create_text(SCO_TEXT_XY[0], SCO_TEXT_XY[1], text=str(sco), font=SCO_TEXT_FONT, fill=SCO_TEXT_COLOR, anchor=SCO_TEXT_ANCHOR)


def de_wall(event):
    global de_wall_status
    if direction != 0:
        de_wall_status = True
        try:
            if direction == 'up':
                up(0)
            if direction == 'down':
                down(0)
            if direction == 'left':
                left(0)
            if direction == 'right':
                right(0)
        except NameError:
            de_wall_status = False


PEOPLE_COLOR = '#ffc800'
WALL_COLOR = 'white'
COIN_COLOR = 'yellow'
GRID_SIZE = 20
SCO_TEXT_XY = (10, 10)
SCO_TEXT_COLOR = '#00ff00'
SCO_TEXT_FONT = ('Arial', 50, 'bold')
SCO_TEXT_ANCHOR = tk.NW
bx, by = 0, 0
walls = {}
coins = {}
sco = 0
de_wall_status = False
direction = 0
angle = 0

root = tk.Tk()
root.title('吃豆人')

canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()

for x in range(GRID_SIZE, 500, GRID_SIZE):
    for y in range(GRID_SIZE, 500, GRID_SIZE):
        n = randint(0, 15)
        if n < 7:
            temp = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=WALL_COLOR)
            walls[(x, y)] = temp
        if n == 15:
            temp = canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=COIN_COLOR)
            coins[(x, y)] = temp
people = canvas.create_arc(bx, by, bx + GRID_SIZE, by + GRID_SIZE, start=angle + 30, extent=300, fill=PEOPLE_COLOR, outline=PEOPLE_COLOR)
sco_text = canvas.create_text(SCO_TEXT_XY[0], SCO_TEXT_XY[1], text=str(sco), font=SCO_TEXT_FONT, fill=SCO_TEXT_COLOR, anchor=SCO_TEXT_ANCHOR)

root.bind('<Up>', up)
root.bind('<Down>', down)
root.bind('<Right>', right)
root.bind('<Left>', left)
root.bind('w', up)
root.bind('s', down)
root.bind('a', left)
root.bind('d', right)
root.bind('<space>', de_wall)
root.bind('f', de_wall)

root.after(100, mainloop)

root.focus_force()
root.mainloop()
