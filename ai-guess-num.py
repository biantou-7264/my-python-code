import tkinter as tk
from tkinter import scrolledtext as st
import os, sys
from tkinter import messagebox as mb

if os.path.exists('./ai-guess-num-fenghao.txt'):
    mb.showwarning('提示', '你的账号已被永久封禁!')
    sys.exit()

min_num = 0
max_num = 100
guess = 0


def stdout(text):
    text_area.insert(tk.END, text)
    text_area.insert(tk.END, '\n')
    text_area.see(tk.END)


def small():
    global min_num
    stdout('人:猜小了')
    min_num = guess + 1
    now_guess()


def big():
    global max_num
    stdout('人:猜大了')
    max_num = guess - 1
    now_guess()


def start():
    global min_num, max_num
    min_num = 0
    max_num = 100
    small_btn.config(state=tk.NORMAL)
    big_btn.config(state=tk.NORMAL)
    yes_btn.config(state=tk.NORMAL)
    now_guess()


def now_guess():
    global guess, min_num, max_num
    if min_num > max_num:
        stdout('机器人:你不讲武德,已进行封号处理!')
        try:
            with open('ai-guess-num-fenghao.txt', 'w') as file:
                file.write('你的账号已被永久封禁!')
        except BaseException as e:
            stdout(e)
        small_btn.config(state=tk.DISABLED)
        big_btn.config(state=tk.DISABLED)
        yes_btn.config(state=tk.DISABLED)
        return
    guess = (min_num + max_num) // 2
    stdout('机器人:现在范围是%d至%d' % (min_num, max_num))
    stdout('机器人:我猜%d' % guess)


def yes():
    stdout('人:猜对了')
    small_btn.config(state=tk.DISABLED)
    big_btn.config(state=tk.DISABLED)
    yes_btn.config(state=tk.DISABLED)


root = tk.Tk()
root.title('AI猜数字')

text_area = st.ScrolledText(root, bg='black', fg='white', height=20, width=60, wrap=tk.WORD, font=('Arial', 20))
text_area.pack(fill=tk.BOTH, expand=True)
control_frame = tk.Frame(root, bg='black')
small_btn = tk.Button(control_frame, text='猜小了', command=small, font=('Arial', 30), state=tk.DISABLED)
small_btn.grid(row=0, column=0, padx=10, pady=10)
yes_btn = tk.Button(control_frame, text='猜对了', command=yes, font=('Arial', 30), state=tk.DISABLED)
yes_btn.grid(row=0, column=1, padx=10, pady=10)
big_btn = tk.Button(control_frame, text='猜大了', command=big, font=('Arial', 30), state=tk.DISABLED)
big_btn.grid(row=0, column=2, padx=10, pady=10)
control_frame.pack(fill=tk.X, expand=True)
tk.Button(root, text='开始', font=('Arial', 30), command=start).pack(pady=10, fill=tk.X, expand=True)

root.focus_force()
root.mainloop()
