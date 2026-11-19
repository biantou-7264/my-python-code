import tkinter as tk
import sys
from random import randint
from AppKit import NSCursor


def create():
    w = canvas.winfo_screenwidth()
    speed = randint(10, 40)
    try:
        temp = randint(0, 2)
        if temp == 0:
            char = randint(161, 0x500)
        else:
            char = randint(33, 126)
        shape = canvas.create_text(randint(0, w), 0, text=chr(randint(33, 130)), font=('Arial', randint(20, 40)), fill='#00ff00')
        root.after(20, move, shape, speed)
    except:
        pass
    NSCursor.hide()
    root.after(30, create)


def move(shape, speed):
    h = canvas.winfo_screenheight()
    x, y = canvas.coords(shape)
    if y > h:
        canvas.delete(shape)
        return
    canvas.move(shape, 0, 10)
    root.after(speed, move, shape, speed)


root = tk.Tk()
root.title('黑客屏保')

canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

root.after(300, create)
root.bind('<Escape>', lambda e: sys.exit())
root.attributes('-fullscreen', True)
root.focus_force()
root.mainloop()
