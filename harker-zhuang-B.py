# 假装黑客装B器

import tkinter as tk
from random import sample
from tkinter import scrolledtext
from time import sleep

count = 0
texts = [("Connecting to the other party's computer...\n", 'done!\n'), ('Copying "bindu.exe" to 100.134.123.10...\n', '||||||||||', '|||||||||||||', '||||||||', '||||||||||', '||||||', '|||||||||||' '||||\n', 'done!\n'), ('running"bindu.exe\n"', 'please wait...\n', '', '', '', '', '', '', '', 'done!\n'), ('closing connect...\n', 'connect to 100.134.123.10 closed.\n')]


def stdout(event):
    global count
    text_area.insert(tk.END, '\n')
    try:
        text = texts[count]
        count += 1
    except IndexError:
        count = 0
        text = texts[count]
    for i in text:
        text_area.insert(tk.END, i)
        text_area.see(tk.END)
        root.update()
        sleep(1)


def show_count(event):
    text_area.insert(tk.END, count)
    text_area.insert(tk.END, '\n')
    text_area.see(tk.END)


root = tk.Tk()
root.title(''.join(sample('qwertyuiopasdfghjklzxcvbnm1234567890', 15)))
root.configure(background='black')

text_area = scrolledtext.ScrolledText(root, bg='black', fg='#00ff00', highlightbackground='black', highlightcolor='black', font=('Arial', 20), )
text_area.pack(fill=tk.BOTH, expand=True)
text_area.bind('<Return>', stdout)
root.bind('<Control-t>', show_count)

root.focus_force()
root.attributes('-fullscreen', True)
root.mainloop()
