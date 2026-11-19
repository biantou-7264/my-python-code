import tkinter as tk
from threading import Thread
import requests as req
import sys, signal
from tkinter import simpledialog as sd

ok_count = 0
fail_count = 0
pause = False
thread_count = 0
zuoye_url = 'https://ucenter.17zuoye.com/login.vpage?returnURL=%2Fsso%2Fticket.vpage%3Fdata%3D%257B%2522sign%2522%253A%252277b7c719a2666a80b11fe41260c0208b%2522%252C%2522appKey%2522%253A%252217Platform%2522%252C%2522timestamp%2522%253A%25221781615928232%2522%252C%2522target%2522%253A%2522https%253A%252F%252Fwww.17zuoye.com%252Fssojump.vpage%253FreturnURL%253Dhttps%25253A%25252F%25252Fwww.17zuoye.com%2522%257D'
nowquit = False
timers = []
thread_id = 0


def climb(tid):
    global ok_count
    global fail_count
    global thread_count
    global pause
    print('%d进入' % tid)
    thread_count += 1
    if pause:
        thread_count -= 1
        print('%d退出' % tid)
        return
    try:
        if nowquit:
            thread_count -= 1
            print('%d退出' % tid)
            return
        print('%d开始' % tid)
        resp = req.get(url=zuoye_url, timeout=10)
        if resp.status_code == 200:
            ok_count += 1
            print('%d成功' % tid)
        else:
            print('%d失败' % tid)
            fail_count += 1
    except:
        print('%d失败' % tid)
        fail_count += 1
    thread_count -= 1
    print('%d退出' % tid)


def start():
    global pause, thread_count, thread_id
    if nowquit:
        return
    if not pause and thread_count < max_thread.get():
        for _ in range(20):
            try:
                Thread(target=climb, args=(thread_id,), daemon=True).start()
                print('创建%d' % thread_id)
                root.update()
                if nowquit:
                    return
                thread_id += 1
            except:
                print('%d创建失败' % thread_id)
    else:
        for _ in range(20):
            root.update()
    root.update()


def main():
    global pause
    if nowquit:
        return
    if not pause:
        root.after(0, start)
    root.update()
    temp = root.after(20, main)
    timers.append(temp)
    while True:
        if len(timers) > max_thread.get() + 200:
            timers.pop(0)
        else:
            break
        root.update()


def set_pause():
    global pause
    pause = not pause
    if pause:
        pause_label.config(text='已暂停')
    else:
        pause_label.config(text='运行中')
    root.update()


def update():
    global ok_count
    global fail_count
    if nowquit:
        return
    ok_count_label.config(text='已成功%d次' % ok_count)
    fail_count_label.config(text='已失败%d次' % fail_count)
    thread_count_label.config(text='共%d个线程' % thread_count)
    root.update()
    temp = root.after(10, update)
    timers.append(temp)


def quit_program():
    while True:
        if len(timers) > max_thread.get() + 200:
            timers.pop(0)
        else:
            break
    for i in timers:
        try:
            root.after_cancel(i)
        except:
            pass
        root.update()
    root.destroy()


def plus_max_thread():
    user_input = sd.askinteger('设置', '请输入最大可调整的最大线程数')
    if user_input:
        max_thread_scale.config(to=user_input)


root = tk.Tk()
root.title('新版卡一起作业服务器')
root.configure(bg='black')
max_thread = tk.IntVar(value=500)

title = tk.Label(root, text='卡一起作业服务器', font=('Arial', 50), fg='white', bg='black')
title.pack(padx=20, pady=10)
count_frame = tk.Frame(root, bg='#000032')
ok_count_label = tk.Label(count_frame, text='已成功%d次' % ok_count, font=('Arial', 30), fg='#00ff00', bg='#000032')
ok_count_label.pack(padx=20, pady=20)
fail_count_label = tk.Label(count_frame, text='已失败%d次' % fail_count, font=('Arial', 30), fg='#ff0000', bg='#000032')
fail_count_label.pack(padx=20, pady=20)
thread_count_label = tk.Label(count_frame, text='共%d个线程' % thread_count, font=('Arial', 30), fg='#ffffff', bg='#000032')
thread_count_label.pack(padx=20, pady=20)
count_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
set_frame = tk.Frame(root, bg='#000032')
max_thread_frame = tk.Frame(set_frame, bg='#000020')
max_thread_scale = tk.Scale(max_thread_frame, label='最大线程数', from_=100, to=1000, orient=tk.HORIZONTAL, showvalue=True, font=('Arial', 30), bg='#000020', variable=max_thread)
max_thread_scale.pack(padx=20, pady=20, fill=tk.X, expand=True, side=tk.LEFT)
plus_max_thread_btn = tk.Button(max_thread_frame, text='+', font=('Arial', 10), command=plus_max_thread, bg='#000020')
plus_max_thread_btn.pack(padx=5, pady=5, side=tk.RIGHT)
max_thread_frame.pack(fill=tk.BOTH, expand=True)
pause_label = tk.Label(set_frame, text='运行中', font=('Arial', 30), fg='white', bg='#000032')
pause_label.pack(padx=20, pady=20)
pause_btn = tk.Button(set_frame, text='开始/停止', font=('Arial', 30), command=set_pause)
pause_btn.pack(padx=20, pady=20)
set_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

signal.signal(signal.SIGTERM, lambda sig, frame: quit_program())
signal.signal(signal.SIGINT, lambda sig, frame: quit_program())
signal.signal(signal.SIGSEGV, lambda sig, frame: None)
signal.signal(signal.SIGALRM, lambda sig, frame: root.update())
signal.signal(signal.SIGUSR1, lambda sig, frame: set_pause())

root.after(10, main)
root.after(10, update)
root.protocol('WM_DELETE_WINDOW', quit_program)
root.focus_force()
root.mainloop()

nowquit = True
exit_win = tk.Tk()
exit_win.title('程序退出中')
exit_win.protocol('WM_DELETE_WINDOW', lambda: None)
signal.signal(signal.SIGTERM, lambda sig, frame: None)
signal.signal(signal.SIGINT, lambda sig, frame: None)
exit_count_label = tk.Label(exit_win, text='程序退出中, 还剩?个线程, 请耐心等待, 不要退出程序', font=('Arial', 30))
exit_count_label.pack(padx=20, pady=20)
while True:
    exit_count_label.config(text='程序退出中, 还剩%d个线程\n请耐心等待, 不要强制退出程序' % thread_count)
    exit_win.update()
    if thread_count <= 0:
        break
exit_win.destroy()
print('程序退出')
sys.exit()
