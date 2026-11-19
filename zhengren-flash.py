import tkinter as tk
from time import sleep


def flash():
    root.deiconify()
    root.geometry('100000000000x100000000000')
    root.update()
    sleep(0.1)
    root.withdraw()
    root.after(2000, flash)


root = tk.Tk()
root.title('')
root.config(bg='white')
root.after(2000, flash)
root.after(100, root.withdraw)
root.withdraw()
root.mainloop()
