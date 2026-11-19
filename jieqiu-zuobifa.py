import turtle
from _random import Random

sco = 0
try:
    with open('jieqiu_sco.txt', 'r') as file:
        sco = int(file.read())
        file.close()
except FileNotFoundError:
    sco = 0
    with open('jieqiu_sco.txt', 'w') as file:
        file.write(str(sco))


def left(event):
    canvas.move(board, -40, 0)


def right(event):
    canvas.move(board, 40, 0)


def randint(a, b):
    return a + int((Random().random()) * (b - a + 1))


class Ball:
    def __init__(self, x, y, width, height, speed):
        self.nx = x
        self.ny = y
        self.width = width
        self.height = height
        self.speed = speed
        self.ball = canvas.create_oval(x, y, x + width, y + height, fill='red')
        root.after(100, self.move)

    def move(self):
        global sco
        canvas.move(self.ball, 0, self.speed)
        _, y, _, _ = canvas.coords(self.ball)
        if board in collision(self.ball):
            sco += 1
            self.nx = randint(-350, 350)
            canvas.coords(self.ball, self.nx, self.ny, self.nx + self.width, self.ny + self.height)
        if y > 600:
            self.nx = randint(-350, 350)
            canvas.coords(self.ball, self.nx, self.ny, self.nx + self.width, self.ny + self.height)
        root.after(10, self.move)


class ScoText:
    def __init__(self, x, y, color, size, anchor):
        self.text = canvas.create_text(x, y, fill=color, font=('Arial', size), anchor=anchor, text='--')
        root.after(100, self.update)

    def update(self):
        canvas.itemconfig(self.text, text=str(sco))
        root.after(100, self.update)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def save():
    with open('jieqiu_sco.txt', 'w') as file:
        file.write(str(sco))
    root.after(1000, save)


def safe_quit():
    save()
    root.quit()


screen = turtle.Screen()
screen.setup(width=800, height=600)
canvas = screen.getcanvas()
canvas.config(bg='#000032')
canvas.config(bd=0)
root = canvas.master
root.title('接球游戏')

board = canvas.create_rectangle(-100, 200, 100, 230, fill='yellow')
ball = Ball(-50, -400, 50, 50, 3)
sco_text = ScoText(-380, -280, 'white', 40, 'nw')

root.after(1000, save)
root.bind('<Left>', left)
root.bind('<Right>', right)
root.bind('<Escape>', safe_quit)
root.protocol('WM_DELETE_WINDOW', safe_quit)
root.focus_force()
root.mainloop()
