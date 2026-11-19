import tkinter as tk

colors = []


class ColorfulOval:
    def __init__(self, x1, y1, x2, y2, index):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.index = index
        self.oval = canvas.create_oval(x1, y1, x2, y2, fill=colors[index], width=0)
        root.after(100, self.change)

    def change(self):
        self.index += 1
        canvas.itemconfig(self.oval, fill=colors[self.index])
        root.after(50, self.change)


def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex


step = 20
start = 50
for r in range(start, 256, step):
    for g in range(start, 256, step):
        for b in range(start, 256, step):
            colors.append(rgb_to_hex(r, g, b))
colors *= 10000

root = tk.Tk()
root.title('圆锥')

canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()
s = 1
for i in range(50):
    y = 420 - i * 7
    s += 4
    y1 = y - 250 + s
    y2 = y + 50 - s
    if y2 < y1:
        continue
    ColorfulOval(100 + s, y1, 400 - s, y2, i)

root.focus_force()
root.mainloop()
