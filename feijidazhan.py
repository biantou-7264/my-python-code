import tkinter as tk
from random import randint, choice

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'magenta']


def create_enemy_plane():
    ex = randint(0, 720)
    ey = -20
    color = choice(colors)
    enemy_plane = canvas.create_rectangle(ex, ey, ex + 50, ey + 50, fill=color)
    enemy_planes.append(enemy_plane)
    root.after(10, enemy_plane_down, enemy_plane, ex, ey, color)
    root.after(randint(500, 1000), create_enemy_plane)


def enemy_plane_down(plane, ex, ey, color):
    canvas.delete(plane)
    enemy_planes.remove(plane)
    ey += 1
    enemy_plane = canvas.create_rectangle(ex, ey, ex + 50, ey + 50, fill=color)
    if ey > 600:
        canvas.delete(enemy_plane)
    enemy_planes.append(enemy_plane)
    root.after(10, enemy_plane_down, enemy_plane, ex, ey, color)


mx = 300
my = 500

root = tk.Tk()
root.title('飞机大战')

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

me_plane = canvas.create_rectangle(mx, my, mx + 70, my + 70, fill='white')
enemy_planes = []

create_enemy_plane()
root.focus_force()
root.mainloop()
