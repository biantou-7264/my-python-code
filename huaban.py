import tkinter as tk

color = 'white'
writes = []
write_counts = []
write_count = 0


def draw(event):
    global write_count
    a = canvas.create_oval(event.x - thickness.get(), event.y - thickness.get(), event.x + thickness.get(), event.y + thickness.get(), fill=color, outline=color)
    writes.append(a)
    write_count += 1
    undo_btn.config(state=tk.NORMAL)


def crcolor(color):
    a = tk.Label(root, bg=color)
    a.pack(side='left', fill=tk.BOTH, expand=True)
    a.bind('<Button-1>', lambda e: change_color(color))


def change_color(c):
    global color
    color = c


def clear():
    global writes
    for a in writes:
        canvas.delete(a)
    writes.clear()
    undo_btn.config(state=tk.DISABLED)


def undo():
    global writes
    try:
        for _ in range(write_counts[-1]):
            canvas.delete(writes[-1])
            writes.pop()
        write_counts.pop()
    except IndexError:
        undo_btn.config(state=tk.DISABLED)


def draw_done(event):
    global write_count
    write_counts.append(write_count)
    write_count = 0


root = tk.Tk()
root.title('画板')

canvas = tk.Canvas(root, width=700, height=700, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', draw_done)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple', '#462800', 'white', 'black']
for i in colors:
    crcolor(i)

tk.Button(root, text='清除', command=clear, font=('Arial', 12)).pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
thickness = tk.IntVar(value=5)
tk.Scale(root, from_=2, to=30, orient=tk.HORIZONTAL, variable=thickness).pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
undo_btn = tk.Button(root, text='撤销', command=undo, font=('Arial', 12), state=tk.DISABLED)
undo_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

root.focus_force()
root.mainloop()
