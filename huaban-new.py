import tkinter as tk
from random import randint

color = 'white'
colors = ['#ff0000', '#ff6400', '#ffc800', '#00ff00', '#0000ff', '#b800ff', '#ff00c8', '#8c4100', 'white']
writes = []
write_count = 0
write_counts = []


def draw(event):
    global write_count
    x, y = event.x, event.y
    if use_eraser.get():
        if shape.get() == 'circle':
            writes.append(canvas.create_oval(x, y, x + 30, y + 30, fill='black', outline='black'))
            write_count += 1
        if shape.get() == 'square':
            writes.append(canvas.create_rectangle(x, y, x + 30, y + 30, fill='black', outline='black'))
            write_count += 1
        if shape.get() == 'triangle':
            writes.append(canvas.create_polygon(x, y, x + thickness.get() / 2, y - thickness.get(), x + thickness.get(), y, x, y, fill='black', outline='black'))
            write_count += 1
        if shape.get() == 'spray':
            writes.append(canvas.create_oval(x, y, x + thickness.get(), y + thickness.get(), fill='black', outline='black'))
            write_count += 1
            for _ in range(randint(3, 6)):
                d = randint(-30, 30)
                writes.append(canvas.create_oval(x + d, y + d, x + d + (thickness.get() // 2), y + d + (thickness.get() // 2), fill='black', outline='black'))
                write_count += 1
    else:
        if shape.get() == 'circle':
            writes.append(canvas.create_oval(x, y, x + thickness.get(), y + thickness.get(), fill=color, outline=color))
            write_count += 1
        if shape.get() == 'square':
            writes.append(canvas.create_rectangle(x, y, x + thickness.get(), y + thickness.get(), fill=color, outline=color))
            write_count += 1
        if shape.get() == 'triangle':
            writes.append(canvas.create_polygon(x, y, x + thickness.get() / 2, y - thickness.get(), x + thickness.get(), y, x, y, fill=color, outline=color))
            write_count += 1
        if shape.get() == 'spray':
            writes.append(canvas.create_oval(x, y, x + thickness.get(), y + thickness.get(), fill=color, outline=color))
            write_count += 1
            for _ in range(randint(3, 6)):
                d = randint(-30, 30)
                writes.append(canvas.create_oval(x + d, y + d, x + d + (thickness.get() // 2), y + d + (thickness.get() // 2), fill=color, outline=color))
                write_count += 1


class ColorBtns:
    def __init__(self, color):
        self.color = color
        self.btn = tk.Label(color_frame, bg=color)
        self.btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.btn.bind('<Button-1>', lambda event: self.set_color(color))

    def set_color(self, c):
        global color
        color = c


def clear(event=None):
    global writes
    writes.clear()
    canvas.delete('all')


def undo(event=None):
    global writes, write_counts
    try:
        for i in range(write_counts[-1]):
            canvas.delete(writes[-1])
            writes.pop()
        write_counts.pop()
    except IndexError:
        clear()


def draw_done(event):
    global write_count, write_counts
    write_counts.append(write_count)
    write_count = 0


root = tk.Tk()
root.title('画板')

thickness = tk.IntVar(value=10)
use_eraser = tk.BooleanVar(value=False)
shape = tk.StringVar(value='circle')

canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind('<B1-Motion>', draw)

color_frame = tk.Frame(root)
for c in colors:
    ColorBtns(c)
color_frame.pack(fill=tk.X, expand=True)

thickness_frame = tk.Frame(root)
thickness_scale = tk.Scale(thickness_frame, from_=5, to=50, orient=tk.HORIZONTAL, label='粗细', tickinterval=5, showvalue=1, variable=thickness)
thickness_scale.pack(fill=tk.X, expand=True)
thickness_frame.pack(fill=tk.X, expand=True)

tool_frame = tk.Frame(root)
eraser_btn = tk.Checkbutton(tool_frame, text='使用橡皮', variable=use_eraser, onvalue=True, offvalue=False)
eraser_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
clear_btn = tk.Button(tool_frame, text='清除', command=clear)
clear_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
undo_btn = tk.Button(tool_frame, text='撤销', command=undo)
undo_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
tool_frame.pack(fill=tk.X, expand=True)

pens_frame = tk.Frame(root)
square_pen_btn = tk.Button(pens_frame, text='▣', command=lambda: shape.set('square'))
square_pen_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
circle_pen_btn = tk.Button(pens_frame, text='●', command=lambda: shape.set('circle'))
circle_pen_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
triangle_pen_btn = tk.Button(pens_frame, text='▲', command=lambda: shape.set('triangle'))
triangle_pen_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
spray_pen_btn = tk.Button(pens_frame, text='❖', command=lambda: shape.set('spray'))
spray_pen_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
pens_frame.pack(fill=tk.X, expand=True)

canvas.bind('<ButtonRelease-1>', draw_done)
root.bind('<Command-z>', undo)
root.bind('<Control-z>', undo)
root.bind('<Command-c>', clear)
root.bind('<Control-c>', clear)

root.focus_force()
root.mainloop()
