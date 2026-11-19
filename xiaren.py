import tkinter as tk
from random import randint
import time

jiu_shapes = []
status = 1
mouse_move_count = 0
mouse_move_time = time.time()


def update():
    global jiu_shapes, status
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    jiange = 5
    new_shapes = []
    if status == 4:
        for y in range(h, -100, jiange * -1):
            for x in range(0, w + 1, jiange):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                hex_color = rgb_to_hex(r, g, b)
                new_shapes.append(canvas.create_rectangle(x, y, x + jiange, y + jiange, fill=hex_color, width=0))
            canvas.update()
    elif status == 3:
        for x in range(w, -1, jiange * -1):
            for y in range(0, h + 1, jiange):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                hex_color = rgb_to_hex(r, g, b)
                new_shapes.append(canvas.create_rectangle(x, y, x + jiange, y + jiange, fill=hex_color, width=0))
            canvas.update()
    elif status == 2:
        for y in range(0, h + 1, jiange):
            for x in range(0, w + 1, jiange):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                hex_color = rgb_to_hex(r, g, b)
                new_shapes.append(canvas.create_rectangle(x, y, x + jiange, y + jiange, fill=hex_color, width=0))
            canvas.update()
    elif status == 1:
        for x in range(0, w + 1, jiange):
            for y in range(0, h + 1, jiange):
                r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
                hex_color = rgb_to_hex(r, g, b)
                new_shapes.append(canvas.create_rectangle(x, y, x + jiange, y + jiange, fill=hex_color, width=0))
            canvas.update()
    for shape in jiu_shapes:
        canvas.delete(shape)
    jiu_shapes += new_shapes
    root.update()
    if status == 4:
        status = 1
    else:
        status += 1
    root.after(100, update)


def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color


def the_mouse_is_moved_please_look(event):
    global mouse_move_count, mouse_move_time
    if time.time() - mouse_move_time > 2:
        mouse_move_time = time.time()
        mouse_move_count = 0
    mouse_move_count += 1
    if mouse_move_count > 5:
        root.destroy()


root = tk.Tk()
root.title('电脑花屏了')
root.attributes('-fullscreen', True)
root.config(cursor='none')

canvas = tk.Canvas(root, width=1234, height=1234, bg='red')
canvas.pack(fill=tk.BOTH, expand=True)

root.bind('<Key>', lambda event: root.destroy())
root.bind('<Motion>', the_mouse_is_moved_please_look)
root.bind('<Button>', lambda event: root.destroy())
root.after(500, update)
root.focus_force()
root.mainloop()
