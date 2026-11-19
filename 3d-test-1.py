from random import randint

from vpython import *

c = box(color=color.red)
ball = sphere(pos=vector(0, 3, 0), color=color.green)
arrow1 = arrow(pos=vector(0, -3, 0), color=color.blue, axis=vector(1, 1, 0))
label(text='这几个图形其实没动!', pos=vector(0, 5, 0), color=color.white, height=20)

while True:
    rate(30)
    pos = vector(randint(-3, 3), randint(-3, 3), randint(-3, 3))
    ball.pos = pos
    pos = vector(randint(-3, 3), randint(-3, 3), randint(-3, 3))
    c.pos = pos
    pos = vector(randint(-3, 3), randint(-3, 3), randint(-3, 3))
    arrow1.pos = pos
    c.rotate(angle=0.1, axis=vector(randint(-10, 10), randint(-10, 10), randint(-10, 10)))
    arrow1.rotate(angle=1, axis=vector(randint(-10, 10), randint(-10, 10), randint(-10, 10)))
