import tkinter as tk
from random import randint
from time import sleep

high_sco = 0
try:
    with open('flybird-high-sco.txt') as file:
        high_sco = int(float(file.read()))
except FileNotFoundError:
    with open('flybird-high-sco.txt', 'w') as file:
        file.write('0')
except ValueError:
    print('分数文件损坏!')
    with open('flybird-high-sco.txt', 'w') as file:
        file.write('0')
    sleep(1)


def bird_down():
    global speed, by, lose, has_shield
    if not pause:
        by += speed
        speed += 0.05
    update_bird()
    if not lose:
        root.after(10, bird_down)
    if by > 700:
        if has_shield:
            has_shield = False
            for i in range(700, py + 300, -10):
                by = i
                update_bird()
                root.update()
            speed = 0
        else:
            lose = True
    if by < 0:
        speed = 2


def update_bird():
    global by, bird, has_shield, sx
    canvas.delete(bird)
    if has_shield:
        bird = canvas.create_rectangle(300, by, 300 + 50, by + 50, fill='#ffff00')
    else:
        bird = canvas.create_rectangle(300, by, 300 + 50, by + 50, fill='#ffc800')
        if shield in collision(bird):
            sx = 900
            has_shield = True
            print(11)
    canvas.lower(bird)
    canvas.lower(pillar_up)
    canvas.lower(pillar_down)


def jump(event):
    global speed
    if not pause:
        if speed > 0:
            speed = -3
        else:
            speed -= 2


def pil_move():
    global px, py, sco, last_up_sco
    if not pause:
        px -= 3
    if px < -100:
        px = 900
        py = randint(-200, 0)
        last_up_sco = False
    if px < 300:
        if not last_up_sco:
            sco += 1
            last_up_sco = True
            update_sco_text()
    update_pil()
    if not lose:
        root.after(10, pil_move)


def update_pil():
    global px, pillar_up, pillar_down, bird, lose, has_shield
    canvas.delete(pillar_up)
    canvas.delete(pillar_down)
    pillar_up = canvas.create_rectangle(px, py, px + 50, py + 200, fill='green')
    pillar_down = canvas.create_rectangle(px, py + 500, px + 50, py + 300 + 500, fill='green')
    if bird in collision(pillar_up):
        if has_shield:
            px -= 100
            has_shield = False
        else:
            lose = True
    if bird in collision(pillar_down):
        if has_shield:
            px -= 100
            has_shield = False
        else:
            lose = True


def shield_move():
    global shield, sx, sy
    if not has_shield:
        if not pause:
            sx -= 2
    if sx < -100:
        sx = 900
        sy = randint(0, 600)
    update_shield()
    if not lose:
        root.after(10, shield_move)


def update_shield():
    global shield
    canvas.delete(shield)
    shield = canvas.create_rectangle(sx, sy, sx + 20, sy + 20, fill='pink')


def update_sco_text():
    global sco_text, high_sco_text
    canvas.delete(sco_text, high_sco_text)
    sco_text = canvas.create_text(50, 30, text=str(sco), font=('Arial', 50, 'bold'), fill='#c80000', anchor=tk.NW)
    high_sco_text = canvas.create_text(50, 80, text='high:' + str(high_sco), font=('Arial', 20), fill='#c80000', anchor=tk.NW)


def collision(a):
    coords = canvas.coords(a)
    collide = canvas.find_overlapping(*coords)
    collide_list = list(collide)
    return collide_list


def lose_tip():
    global lose_text, high_sco
    if lose:
        lose_text = canvas.create_text(400, 300, text='你挂了!', font=('Arial', 100, 'bold'))
        if sco > high_sco:
            high_sco = sco
            with open('flybird-high-sco.txt', 'w') as file:
                file.write(str(high_sco))
            update_sco_text()
        root.bind('<Return>', reset)
    else:
        root.after(100, lose_tip)


def change_pause(event):
    global pause, pause_text
    if not pause:
        pause = True
        pause_text = canvas.create_text(400, 300, text='暂停状态', font=('Arial', 100, 'bold'), fill='#c80000')
    else:
        pause = False
        canvas.delete(pause_text)


def reset(event=None):
    global pause, sco, last_up_sco, lose, px, root, lose_text, speed, py, by
    pause = False
    lose = False
    sco = 0
    speed = 0
    last_up_sco = False
    px = 900
    py = randint(-200, 0)
    by = 300
    update_bird()
    update_pil()
    update_sco_text()
    canvas.delete(lose_text)
    root.unbind('<Return>')
    root.bind('<Return>', change_pause)
    root.after(10, bird_down)
    root.after(100, pil_move)
    root.after(200, lose_tip)
    root.after(200, shield_move)


by = 300
px = 900
py = randint(-200, 0)
sx = 900
sy = randint(0, 600)
speed = 0
sco = 0
lose = False
last_up_sco = False
pause = False
has_shield = False

root = tk.Tk()
root.title('fly bird')
w, h = 800, 600
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (sw - w) / 2, (sh - h) / 2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

canvas = tk.Canvas(root, width=800, height=600, bg='#3264ff')
canvas.pack()
canvas.pack()

bird = canvas.create_rectangle(300, by, 300 + 50, by + 50, fill='#ffc800')
pillar_up = canvas.create_rectangle(px, py, px + 50, py + 300, fill='green')
pillar_down = canvas.create_rectangle(px, py, px + 50, py + 300 + 200, fill='green')
shield = canvas.create_rectangle(sx, sy, sx + 20, sy + 20, fill='pink')
sco_text = canvas.create_text(50, 30, text=str(sco), font=('Arial', 50, 'bold'), fill='#c80000', anchor=tk.NW)
high_sco_text = canvas.create_text(50, 80, text='high:' + str(high_sco), font=('Arial', 20), fill='#c80000', anchor=tk.NW)

root.bind('<space>', jump)
root.bind('<Return>', change_pause)
root.bind('<Escape>', lambda event: root.quit())
root.after(10, bird_down)
root.after(100, pil_move)
root.after(200, lose_tip)
root.after(200, shield_move)

root.focus_force()
root.mainloop()
