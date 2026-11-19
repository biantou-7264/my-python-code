import tkinter as tk


def format_time(hour, minute, second):
    hour, minute, second = str(hour), str(minute), str(second)
    if len(hour) < 2:
        hour = '0' + hour
    if len(minute) < 2:
        minute = '0' + minute
    if len(second) < 2:
        second = '0' + second
    return hour + ':' + minute + ':' + second


def update_progress():
    global progress_highlight
    canvas.delete(progress_highlight)
    try:
        if process_value >= 100:
            progress_highlight = canvas.create_arc(20, 20, 480, 480, start=90, extent=359.999, style=tk.ARC, outline=progress_highlight_color.get(), width=5)
        else:
            progress_highlight = canvas.create_arc(20, 20, 480, 480, start=90, extent=0 - (360 * (process_value / 100)), style=tk.ARC, outline=progress_highlight_color.get(), width=5)
    except Exception:
        pass


def update_time_text():
    global time_text
    try:
        canvas.delete(time_text)
        hour = left_time.get() // 3600
        remian_second = left_time.get() % 3600
        minute = remian_second // 60
        second = remian_second % 60
        time_text = canvas.create_text(250, 250, text='%s' % format_time(hour, minute, second), font=('Arial', 100), fill='white', anchor=tk.CENTER)
    except Exception:
        canvas.delete(time_text)
        time_text = canvas.create_text(250, 250, text='--:--:--', font=('Arial', 100), fill='white', anchor=tk.CENTER)


def update():
    global process_value
    try:
        process_value = (left_time.get() / total_time.get()) * 100
    except Exception:
        process_value = 0
    update_progress()
    update_time_text()
    root.after(10, update)


def count_down():
    global left_time, start
    if start.get():
        try:
            if left_time.get() > 1:
                left_time.set(left_time.get() - 1)
            else:
                left_time.set(0)
                start.set(False)
                msg = tk.Toplevel(root)
                tk.Label(msg, bitmap='info').pack(anchor=tk.NW, padx=20, pady=20)
                tk.Label(msg, text='时间到啦!!!!', font=('Arial', 40), justify='left').pack(anchor=tk.NW, padx=20)
                tk.Button(msg, text='我知道了', command=msg.destroy, font=('Arial', 30), cursor='pointinghand').pack(side=tk.BOTTOM, pady=10)
                msg.geometry('600x400')
                msg.update()
                msg.focus_force()
                msg.attributes('-topmost', True)
        except Exception as e:
            print(e)
            start.set(False)

    root.after(1000, count_down)


root = tk.Tk()
root.title('闹钟')
root.configure(background='black')

start = tk.BooleanVar(value=False)
left_time = tk.IntVar(value=5)
total_time = tk.IntVar(value=5)
progress_highlight_color = tk.StringVar(value='red')

canvas = tk.Canvas(root, width=500, height=500, bg='black')
canvas.pack()

process_value = 0
progress = canvas.create_arc(20, 20, 480, 480, start=0, extent=359.999, style=tk.ARC, outline='white', width=5)
if process_value >= 100:
    progress_highlight = canvas.create_arc(20, 20, 480, 480, start=90, extent=359.999, style=tk.ARC, outline=progress_highlight_color.get(), width=5)
else:
    progress_highlight = canvas.create_arc(20, 20, 480, 480, start=90, extent=360 * (process_value / 100), style=tk.ARC, outline=progress_highlight_color.get(), width=5)
time_text = canvas.create_text(250, 250, text='--:--:--', font=('Arial', 100), fill='white', anchor=tk.CENTER)
set_frame = tk.Frame(root, bg='black')
tk.Checkbutton(set_frame, text='开始计时', variable=start, onvalue=True, offvalue=False, bg='black', font=('Arial', 20)).grid(row=0, column=0, padx=5, pady=5)
tk.Label(set_frame, text='剩余时间:', bg='black', font=('Arial', 20)).grid(row=1, column=0, padx=5, pady=5)
tk.Entry(set_frame, textvariable=left_time, highlightbackground='white', font=('Arial', 20)).grid(row=1, column=1, padx=5, pady=5)
tk.Label(set_frame, text='总共时间:', bg='black', font=('Arial', 20)).grid(row=2, column=0, padx=5, pady=5)
tk.Entry(set_frame, textvariable=total_time, highlightbackground='white', font=('Arial', 20)).grid(row=2, column=1, padx=5, pady=5)
tk.Label(set_frame, text='进度颜色:', bg='black', font=('Arial', 20)).grid(row=3, column=0, padx=5, pady=5)
tk.Entry(set_frame, textvariable=progress_highlight_color, highlightbackground='white', font=('Arial', 20)).grid(row=3, column=1, padx=5, pady=5)
set_frame.pack(padx=5, pady=5)

root.after(10, update)
root.after(100, count_down)

root.focus_force()
root.mainloop()
