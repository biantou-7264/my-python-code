import tkinter as tk
from tkinter import scrolledtext as st


def stdout(text):
    current_position = text_area.yview()
    text_area.insert(tk.END, text)
    text_area.insert(tk.END, '\n')
    if current_position[1] >= 0.99:
        text_area.see(tk.END)


def update_status(*args):
    status.set('机器人赢%d次, 人赢0次' % robot.get())


def stone():
    stdout('人出了石头')
    stdout('机器人出了布')
    stdout('机器人赢了!')
    robot.set(robot.get() + 1)


def cut():
    stdout('人出了剪刀')
    stdout('机器人出了石头')
    stdout('机器人赢了!')
    robot.set(robot.get() + 1)


def paper():
    stdout('人出了布')
    stdout('机器人出了剪刀')
    stdout('机器人赢了!')
    robot.set(robot.get() + 1)


root = tk.Tk()
root.title('石头剪刀布')
status = tk.StringVar(value='机器人赢0次, 人赢0次')
robot = tk.IntVar(value=0)

text_area = st.ScrolledText(root, width=70, height=30, font=('Arial', 15), highlightbackground='white')
text_area.pack(fill=tk.BOTH, expand=True)
status_label = tk.Label(root, textvariable=status, font=('Arial', 20))
status_label.pack()
choose_frame = tk.Frame(root)
stone_btn = tk.Button(root, text='出石头', command=stone, font=('Arial', 20))
stone_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
cut_btn = tk.Button(root, text='出剪刀', command=cut, font=('Arial', 20))
cut_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
paper_btn = tk.Button(root, text='出布', command=paper, font=('Arial', 20))
paper_btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
choose_frame.pack(fill=tk.X, expand=True)
robot.trace_add('write', update_status)

root.focus_force()
root.mainloop()
