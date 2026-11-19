import tkinter as tk
from random import randint

arr = []
sorting_arr = []
list_len = 1000
max_num = 100
stop = False
pause = False


def sort():
    global arr
    while True:
        if pause:
            root.update()
            continue
        for i in range(list_len - 1):
            a = arr[i]
            b = arr[i + 1]
            if a > b:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorting_arr.append(i)
                sorting_arr.append(i + 1)
        c = 0
        no = False
        for i in arr:
            if i >= c:
                c = i
            if i < c:
                no = True
                break
        update()
        sorting_arr.clear()
        if not no:
            update()
            reset_btn.config(state=tk.NORMAL)
            stop_btn.config(state=tk.DISABLED)
            pause_btn.config(state=tk.DISABLED)
            return arr
        if stop:
            reset_btn.config(state=tk.NORMAL)
            stop_btn.config(state=tk.DISABLED)
            pause_btn.config(state=tk.DISABLED)
            return arr


def random_arr():
    global arr
    arr = []
    for _ in range(list_len):
        arr.append(randint(0, max_num))


def update():
    canvas.delete(tk.ALL)
    x = 0
    w = 800 / list_len
    for count, num in enumerate(arr):
        h = (600 / max_num) * num
        color = 'blue' if count in sorting_arr else 'white'
        canvas.create_rectangle(x, 600, x + w, 600 - h, fill=color, width=0)
        x += w
    root.update()


def reset():
    global stop
    stop = False
    reset_btn.config(state=tk.DISABLED)
    stop_btn.config(state=tk.NORMAL)
    pause_btn.config(state=tk.NORMAL)
    random_arr()
    root.after(10, sort)


def set_stop():
    global stop, pause
    stop_btn.config(state=tk.DISABLED)
    pause_btn.config(state=tk.DISABLED)
    stop = True
    pause = False


def set_pause():
    global pause
    pause = not pause
    if pause:
        pause_btn.config(text='继续')
    else:
        pause_btn.config(text='暂停')


root = tk.Tk()
root.title('冒泡排序')

canvas = tk.Canvas(root, width=800, height=600, background='black')
canvas.pack()

reset_btn = tk.Button(root, text='开始', command=reset, font=('Arial', 25))
reset_btn.pack(fill=tk.BOTH, expand=True)
stop_btn = tk.Button(root, text='停止', command=set_stop, font=('Arial', 25), state=tk.DISABLED)
stop_btn.pack(fill=tk.BOTH, expand=True)
pause_btn = tk.Button(root, text='暂停', command=set_pause, font=('Arial', 25), state=tk.DISABLED)
pause_btn.pack(fill=tk.BOTH, expand=True)

root.focus_force()
root.mainloop()
