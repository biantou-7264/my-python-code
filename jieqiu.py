import tkinter as tk
from random import randint
from time import time

bx = 400
x = 400
y = 0
pause = False
speed = 2.0
ai_mode = False
btime = time()

try:
    with open('jieqiu_sco.txt', 'r') as file:
        sco = int(file.read())
        file.close()
except:
    sco = 0
    with open('jieqiu_sco.txt', 'w') as file:
        file.write(str(sco))

def left(event):
    if not pause:
        global bx, board
        if bx > 0:
            for i in range(5):
                bx -= 10
                canvas.delete(board)
                board = canvas.create_line(bx, 570, bx + 150, 570, width=5, fill='red')
                root.update()

def right(event):
    if not pause:
        global bx, board
        if bx < 700:
            for i in range(5):
                bx += 10
                canvas.delete(board)
                board = canvas.create_line(bx, 570, bx + 150, 570, width=5, fill='red')
                root.update()

def ball_down(event=None):
    if not pause:
        global ball, y, sco, x, sco_text, btime, ai_mode
        canvas.delete(ball)
        y += speed
        ball = canvas.create_oval(x, y, x + 30, y + 30, width=3, fill='green', outline='red')
        if y >= 550:
            canvas.delete(ball)
            if x > bx - 50:
                if x < bx + 150:
                    sco += 1
            y = 0
            x = randint(0, 750)
        canvas.delete(sco_text)
        sco_text = canvas.create_text(20, 20, anchor=tk.NW, text=str(sco), font=('Arial', 50, 'bold'), fill='#FFc800')
    if abs(btime - time()) > 20:
        ai_mode = True
    else:
        ai_mode = False
    root.after(5, ball_down)

def now_ball_down(event=None):
    if not pause:
        global ball, y, x
        canvas.delete(ball)
        y += 50
        ball = canvas.create_oval(x, y, x + 30, y + 30, width=3, fill='green', outline='red')

def save(event=None):
    global sco, save_message
    with open('jieqiu_sco.txt', 'w') as file:
        file.write(str(sco))
    save_message = canvas.create_text(780, 20, anchor=tk.NE, text='auto save', font=('Arial', 30, 'bold'), fill='#FFc800')
    root.unbind('<Command-s>')
    root.after(10000, save)
    root.after(500, clear_save_message)

def now_save(event=None):
    global sco, save_message
    with open('jieqiu_sco.txt', 'w') as file:
        file.write(str(sco))
    save_message = canvas.create_text(780, 20, anchor=tk.NE, text='save', font=('Arial', 30, 'bold'), fill='#FFc800')
    root.unbind('<Command-s>')
    root.after(500, clear_save_message)

def Pause(event):
    global pause, pause_text
    pause = not pause
    if pause:
        pause_text = canvas.create_text(780, 20, anchor=tk.NE, text='PAUSE', font=('Arial', 30, 'bold'), fill='#FFc800')
    else:
        canvas.delete(pause_text)

def saveandquit(event=None):
    save()
    root.quit()

def clear_save_message():
    global save_message
    canvas.delete(save_message)
    root.bind('<Command-s>', now_save)

def focus_and_top():
    root.focus_force()
    root.attributes('-topmost', True)
    root.after(200, focus_and_top)

def fast(event=None):
    global speed,speed_text
    speed += 0.5
    canvas.delete(speed_text)
    speed_text = canvas.create_text(20, 70, anchor=tk.NW, text='speed:' + str(speed), font=('Arial', 20), fill='#FFc800')

def slow(event=None):
    global speed,speed_text
    if speed != 0.5:
        speed -= 0.5
    canvas.delete(speed_text)
    speed_text = canvas.create_text(20, 70, anchor=tk.NW, text='speed:' + str(speed), font=('Arial', 20), fill='#FFc800')

def AI_play():
    global x, bx, ai_mode
    if ai_mode:
        if speed > 5:
            slow()
        if speed < 5:
            fast()
        if x < bx:
            left(1)
        elif bx + 100  < x:
            right(1)
        root.after(20, AI_play)
    else:
        root.after(100, AI_play)

def close_AI(event=None):
    global ai_mode, btime
    if ai_mode:
        ai_mode = False
    btime = time()

def on_left(event=None):
    close_AI()
    left(1)

def on_right(event=None):
    close_AI()
    right(1)

root = tk.Tk()
root.title('接球游戏')

sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
scx, scy = (sw - 800) / 2, (sh - 600) / 2
root.geometry('+%d+%d' % (scx, scy))

canvas = tk.Canvas(root, width=800, height=600, bg='darkblue')
canvas.pack()

canvas.create_line(0, 580, 800, 580, width=5, fill='green')
board = canvas.create_line(bx, 570, bx + 150, 570, width=5, fill='red')
ball = canvas.create_oval(x, y, x + 30, y + 30, width=3, fill='green', outline='red')
sco_text = canvas.create_text(20, 20, anchor=tk.NW, text=str(sco), font=('Arial', 50, 'bold'), fill='#FFc800')
speed_text = canvas.create_text(20, 70, anchor=tk.NW, text='speed:' + str(speed), font=('Arial', 20), fill='#FFc800')

root.bind('<Left>', on_left)
root.bind('<Right>', on_right)
root.bind('<Down>', now_ball_down)
root.bind('<Command-s>', now_save)
root.bind('<space>', Pause)
root.bind('<Escape>', saveandquit)
root.bind(',', slow)
root.bind('.', fast)
root.protocol('WM_DELETE_WINDOW', saveandquit)

ball_down()
save()
AI_play()

root.focus_force()
root.after(500, focus_and_top)
root.resizable(False, False)
root.mainloop()