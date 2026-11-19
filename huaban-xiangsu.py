import tkinter as tk

try:
    import pyautogui as pag
except ImportError:
    import subprocess as sp
    import sys

    while True:
        try:
            name = 'pyautogui'
            res = sp.run([sys.executable, '-m', 'pip', 'install', name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '3'])
            if res.returncode == 0:
                break
        except Exception as e:
            print(e)
    import pyautogui as pag

    del sp
    del sys

from tkinter import filedialog as fd

color = 'white'
width = 20
height = 20
grids = []


class Grid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.grid = canvas.create_rectangle(x, y, x + width, y + height, fill='black', outline='white', width=1)
        self.status = False
        canvas.tag_bind(self.grid, '<Button-1>', self.change)

    def change(self, event):
        if self.status:
            self.off()
        else:
            self.on()

    def on(self):
        canvas.itemconfig(self.grid, fill=color)
        self.status = True

    def off(self):
        canvas.itemconfig(self.grid, fill='black')
        self.status = False

    def update_edge(self):
        if hide_grid_edge.get():
            canvas.itemconfig(self.grid, width=0)
        else:
            canvas.itemconfig(self.grid, width=1)


class ColorBtn:
    def __init__(self, color):
        self.color = color
        self.btn = tk.Label(set_frame, bg=color)
        self.btn.pack(fill=tk.X, expand=True, side=tk.LEFT)
        self.btn.bind('<Button-1>', self.click)

    def click(self, event):
        global color
        color = self.color


def update_grid_edge():
    for grid in grids:
        grid.update_edge()


def clear():
    for grid in grids:
        grid.off()


def get_canvas_coords():
    left_top_x = canvas.winfo_rootx()
    left_top_y = canvas.winfo_rooty()
    right_bottom_x = left_top_x + canvas.winfo_width()
    right_bottom_y = left_top_y + canvas.winfo_height()
    return left_top_x, left_top_y, right_bottom_x, right_bottom_y


def save():
    left_top_x, left_top_y, _, _ = get_canvas_coords()
    screen_shot = pag.screenshot(region=(left_top_x, left_top_y, canvas.winfo_width(), canvas.winfo_height()))
    path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNG', '*.png')])
    if path:
        screen_shot.save(path)


root = tk.Tk()
root.title('像素画板')
hide_grid_edge = tk.BooleanVar()

canvas = tk.Canvas(root, width=600, height=600, bg='black')
canvas.pack()

for y in range(0, 600, height):
    for x in range(0, 600, width):
        grids.append(Grid(x, y, width, height))

set_frame = tk.Frame(root, bg='black')
colors = ['#ff0000', '#ff6400', '#ffc800', '#00ff00', '#0000ff', '#b800ff', '#ff00c8', '#8c4100', 'white']
for color in colors:
    ColorBtn(color)
tk.Checkbutton(set_frame, text='隐藏格子边框', variable=hide_grid_edge, onvalue=True, offvalue=False, command=update_grid_edge).pack(side=tk.LEFT)
tk.Button(set_frame, text='清空', command=clear).pack(side=tk.LEFT)
tk.Button(set_frame, text='保存', command=save).pack(side=tk.LEFT)
set_frame.pack(fill=tk.X, expand=True)

root.focus_force()
root.mainloop()
