import tkinter as tk
from random import choice
#from tkinter import original_color
root=tk.Tk()
colors=['red','orange','yellow','green','blue','purple','pink']
def zoom():
    root.attributes("-fullscreen", True)
    root.after(200,zoom)
def color():
    root.configure(bg=choice(colors))
    root.after(500,color)
def focus():
    root.focus_force()
    root.after(200,focus)
def safequit(debug=0):
    root.destroy()
root.protocol("WM_DELETE_WINDOW",safequit)
root.bind('<Escape>',safequit)
zoom()
color()
focus()
root.mainloop()
