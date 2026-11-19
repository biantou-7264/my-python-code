import turtle as t

start = False
angle = 0
speed = 10

t.tracer(0, 0)


def on_off(event):
    global start
    start = not start


def plus(event):
    global speed
    speed += 10
    if speed > 40:
        speed = 40


def minus(event):
    global speed
    speed -= 10
    if speed < 10:
        speed = 10


def draw():
    p.clear()
    p.setheading(0)
    p.left(angle)
    for _ in range(3):
        p.begin_fill()
        for _ in range(3):
            p.forward(200)
            p.left(120)
        p.end_fill()
        p.right(120)
    t.update()


def update():
    global angle
    if start:
        angle += speed
        draw()
    root.after(10, update)


s = t.Screen()
s.bgcolor('#323232')
s.title('风扇')

root = s.getcanvas().master

p = t.Pen()
p.hideturtle()
p.teleport(0, 100)
p.speed(0)
p.color('white')
p.fillcolor('white')
draw()

tips_p = t.Pen()
tips_p.hideturtle()
tips_p.penup()
tips_p.speed(0)
tips_p.color('white')
tips_p.goto(0, -250)
tips_p.write('按下空格键开启/关闭风扇', align='center', font=('Arial', 20))
tips_p.goto(0, -300)
tips_p.write('按下+ -键调节风速', align='center', font=('Arial', 20))

root.bind('<space>', on_off)
root.bind('<plus>', plus)
root.bind('<equal>', plus)
root.bind('<minus>', minus)
root.after(10, update)

t.update()
t.done()
