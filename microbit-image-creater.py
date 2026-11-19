import tkinter as tk
import pyperclip as clip

pixes = {}


class Pix:
    def __init__(self, width, height, row, column):
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.on = False
        self.canvas = tk.Canvas(pixes_frame, width=width, height=height, bg='black', highlightcolor='white', highlightbackground='white', bd=1)
        self.canvas.grid(row=row, column=column)
        self.canvas.bind('<Button-1>', self.change)
        pixes['%d,%d' % (self.row, self.column)] = self

    def change(self, event=None):
        self.on = not self.on
        create()
        self.update()

    def update(self):
        if self.on:
            self.canvas.config(bg='#ff2541')
        else:
            self.canvas.config(bg='black')


def create():
    res = ''
    for row in range(0, 5):
        for column in range(0, 5):
            pix = pixes['%d,%d' % (row, column)]
            if pix.on:
                res += '1'
            else:
                res += '0'
        res += ':'
    res = res.rstrip(':')
    result.set(res)


def copy():
    clip.copy(result.get())


root = tk.Tk()
root.title('MICROBIT图片生成器')

result = tk.StringVar(value='00000:00000:00000:00000:00000')

pixes_frame = tk.Frame(root)
for row in range(0, 5):
    for column in range(0, 5):
        Pix(50, 50, row, column)
pixes_frame.pack()

tk.Button(root, text='生成', command=create, font=('Arial', 20)).pack(fill=tk.X)
tk.Button(root, text='复制', command=copy, font=('Arial', 20)).pack(fill=tk.X)
tk.Label(root, textvariable=result, font=('Arial', 20)).pack()

root.focus_force()
root.mainloop()
