import tkinter as tk
from tkinter import scrolledtext as st

log = []


def onkey(event):
    root.bell()
    log.append('Press: %s, Input: %s, Keycode: %s' % (event.keysym, event.char, event.keycode))
    update()
    return 'break'


def update():
    text_area.delete('1.0', tk.END)
    for l in log:
        text_area.insert(tk.END, l + '\n')
    text_area.see(tk.END)
    root.update()


root = tk.Tk()
root.title('键盘测试')

text_area = st.ScrolledText(root, width=50, height=20, font=('Arial', 20), bg='#003200', fg='#ff7f7f')
text_area.pack(fill=tk.BOTH, expand=True)
root.bind('<Key>', onkey)
text_area.bind('<FocusIn>', lambda event: root.focus_force())

root.focus_force()
root.mainloop()
