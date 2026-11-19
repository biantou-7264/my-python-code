import tkinter as tk
import os, time
from tkinter import ttk
from threading import Thread
import pyperclip as clip

data = {}
start = False
done = False
progess = 0
thread = None
stop_flag = False


def tongji():
    global start, data, done, progess, stop_flag
    start = True
    total = 0
    count = 0
    speed = 0
    progess = 0
    left_time = 0
    jindu_msg.set('统计文件总数: 共 0 个文件')
    last_speed_time = time.time()
    for _, _, filenames in os.walk('/'):
        total += len(filenames)
        if time.time() - last_speed_time > 0.5:
            last_speed_time = time.time()
            jindu_msg.set('统计文件总数: 共 %d 个文件' % total)
        if stop_flag:
            start = False
            stop_flag = False
            done = True
            jindu_msg.set('统计文件总数: 共 %d 个文件' % total)
            return
    progess = 0
    jindu_msg.set('0%% 0/%d 0/s 0s' % total)
    last_speed_time = time.time()
    speed_count = 0
    for dirpath, _, filenames in os.walk('/'):
        try:
            for filename in filenames:
                path = os.path.join(dirpath, filename)
                _, ext = os.path.splitext(path)
                ext = ext.replace('.', '').lower()
                if ext in data:
                    data[ext] += 1
                else:
                    data[ext] = 1
        except PermissionError:
            pass
        count += len(filenames)
        speed_count += len(filenames)
        if time.time() - last_speed_time > 0.2:
            speed = speed_count * 5
            last_speed_time = time.time()
            speed_count = 0
            progess = count / total * 100
            jindu_msg.set('%.2f%% %d/%d %d/s %.2fs' % (progess, count, total, speed, left_time))
        if stop_flag:
            start = False
            stop_flag = False
            done = True
            jindu_msg.set('%.2f%% %d/%d %d/s %.2fs' % (progess, count, total, speed, left_time))
            return
        if speed == 0:
            left_time = 0
        else:
            left_time = (total - count) / speed
    jindu_msg.set('100%% %d/%d 0/s 0s' % (total, total))
    progess = 100
    start = False
    done = True


def start_tongji():
    global thread, stop_flag
    stop_flag = False
    stop_btn.config(state=tk.NORMAL)
    start_btn.config(state=tk.DISABLED)
    thread = Thread(target=tongji, daemon=True)
    thread.start()


def nowstop():
    global stop_flag
    stop_flag = True


def show():
    global done
    if start:
        try:
            for item in tree.get_children():
                tree.delete(item)
            for key, value in data.items():
                tree.insert('', tk.END, text='', values=(key, value))
            jindu['value'] = progess
        except Exception:
            pass
    if done:
        start_btn.config(state=tk.NORMAL)
        stop_btn.config(state=tk.DISABLED)
        for item in tree.get_children():
            tree.delete(item)
        for key, value in data.items():
            tree.insert('', tk.END, text='', values=(key, value))
        done = False
        jindu['value'] = 100
        root.focus_force()
    if start:
        root.after(100, show)
    else:
        root.after(1000, show)


def copy_data():
    text = str(data)
    if not copy_has_dakuohao.get():
        text = text.rstrip('}')
        text = text.lstrip('{')
    if not copy_has_yinghao.get():
        text = text.replace("'", '')
    clip.copy(text)


root = tk.Tk()
root.title('文件统计')
root.configure(background='#0000c8')

copy_has_dakuohao = tk.BooleanVar()
copy_has_yinghao = tk.BooleanVar()
jindu_msg = tk.StringVar(value='0% 0/? 0/s 0s')

title = tk.Label(root, text='文件统计', bg='#0000c8', fg='white', font=('Arial', 30))
title.pack()

style = ttk.Style()
style.configure('Treeview.Heading', font=('Arial', 20))
style.configure('Treeview', font=('Arial', 20), rowheight=40)
style.map('Treeview', background=[('selected', '#0000c8')])

tree_frame = tk.Frame(root, bg='#0000c8')

tree = ttk.Treeview(tree_frame, columns=('ext', 'count'), height=10, show='headings')
tree.heading('ext', text='后缀')
tree.heading('count', text='数量')
tree.column('ext', width=200)
tree.column('count', width=200)

v_scroll = tk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=v_scroll.set)

tree.place(x=0, y=0, relwidth=1, relheight=1, width=-15, height=-15)
v_scroll.place(relx=1, x=-15, y=0, relheight=1, width=15)
tree_frame.pack(fill=tk.BOTH, expand=True, ipady=200, ipadx=300)

jindu = ttk.Progressbar(root, maximum=100, mode='determinate', orient='horizontal', length=10)
jindu.pack(padx=30, pady=10, fill=tk.X)
jindu_label = tk.Label(root, textvariable=jindu_msg, font=('Arial', 20), bg='#0000c8')
jindu_label.pack(padx=30, pady=10, fill=tk.X, expand=True)

start_btn = tk.Button(root, text='开始', command=start_tongji, font=('Arial', 20))
start_btn.pack(padx=30, pady=10, fill=tk.X, expand=True)
stop_btn = tk.Button(root, text='停下来', command=nowstop, font=('Arial', 20), state=tk.DISABLED)
stop_btn.pack(padx=30, pady=10, fill=tk.X, expand=True)
copy_btn = tk.Button(root, text='复制', command=copy_data, font=('Arial', 20))
copy_btn.pack(padx=30, pady=10, fill=tk.X, expand=True)
copy_has_dakuohao_btn = tk.Checkbutton(root, text='复制带大括号', variable=copy_has_dakuohao, font=('Arial', 20), bg='#0000c8')
copy_has_dakuohao_btn.pack(padx=30, pady=10, fill=tk.X, expand=True)
copy_has_yinghao_btn = tk.Checkbutton(root, text='复制带引号“\'”', variable=copy_has_yinghao, font=('Arial', 20), bg='#0000c8')
copy_has_yinghao_btn.pack(padx=30, pady=10, fill=tk.X, expand=True)

root.after(1000, show)
root.focus_force()
root.mainloop()
