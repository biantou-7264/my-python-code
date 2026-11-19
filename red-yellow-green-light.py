import tkinter as tk

darkred = '#640000'
darkgreen = '#006400'
darkyellow = '#646400'
lightred = '#ff0000'
lightgreen = '#00ff00'
lightyellow = '#ffff00'
now_light = 0
left_time = 0


class Light:
    def __init__(self, x1, y1, x2, y2, offcolor, oncolor):
        self.offcolor = offcolor
        self.oncolor = oncolor
        light = canvas.create_oval(x1, y1, x2, y2, fill=offcolor, outline='black')
        self.id = light

    def change(self, staus):
        if staus:
            canvas.itemconfig(self.id, fill=self.oncolor)
        else:
            canvas.itemconfig(self.id, fill=self.offcolor)


class Counter:
    def __init__(self, red_time, green_time, yellow_time):
        global left_time
        left_time = red_time
        self.red_time = red_time
        self.green_time = green_time
        self.yellow_time = yellow_time
        root.after(100, self.count)

    def count(self):
        global now_light, left_time
        left_time -= 1
        if left_time <= 0:
            if now_light == 2:
                now_light = 0
            else:
                now_light += 1
            if now_light == 0:
                left_time = self.red_time
            if now_light == 1:
                left_time = self.green_time
            if now_light == 2:
                left_time = self.yellow_time
        root.after(1000, self.count)

    def set_time(self, red_time, green_time, yellow_time):
        global now_light, left_time
        self.red_time = red_time
        self.green_time = green_time
        self.yellow_time = yellow_time
        now_light = 0
        left_time = red_time


class TimeText:
    def __init__(self):
        self.xys = [(150, 100), (150, 335), (150, 220)]
        self.colors = [darkred, darkgreen, darkyellow]
        x, y = self.xys[now_light]
        self.text = canvas.create_text(x, y, text=str(left_time), fill=self.colors[now_light], font=('Digital-7 Mono', 40))
        root.after(100, self.update)

    def update(self):
        canvas.delete(self.text)
        x, y = self.xys[now_light]
        self.text = canvas.create_text(x, y, text=str(left_time), fill=self.colors[now_light], font=('Digital-7 Mono', 40))
        root.after(100, self.update)


def update_light():
    if now_light == 0:
        red.change(True)
        yellow.change(False)
        green.change(False)
    if now_light == 2:
        red.change(False)
        yellow.change(True)
        green.change(False)
    if now_light == 1:
        red.change(False)
        yellow.change(False)
        green.change(True)
    root.after(100, update_light)


def apply_times():
    try:
        red = int(red_time_entry.get())
        green = int(green_time_entry.get())
        yellow = int(yellow_time_entry.get())
        counter.set_time(red, green, yellow)
    except BaseException as e:
        times_apply_status_label.config(text='Error:%s' % e)
    else:
        times_apply_status_label.config(text='Success')


def pedestrians_crossing():
    global left_time
    if now_light == 1 and left_time > 5:
        left_time = 5


root = tk.Tk()
root.title('红绿灯模拟器')
root.config(bg='#64c8ff')

canvas = tk.Canvas(root, width=300, height=600, bg='#64c8ff')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

canvas.create_rectangle(50, 570, 250, 600, fill='black', outline='black')
canvas.create_rectangle(130, 580, 170, 400, fill='black', outline='black')
canvas.create_oval(70, 260, 230, 420, fill='black', outline='black')
canvas.create_rectangle(70, 340, 230, 100, fill='black', outline='black')
canvas.create_oval(70, 30, 230, 190, fill='black', outline='black')
red = Light(100, 50, 200, 150, darkred, lightred)
yellow = Light(100, 170, 200, 270, darkyellow, lightyellow)
green = Light(100, 290, 200, 390, darkgreen, lightgreen)
counter = Counter(60, 120, 3)
TimeText()

set_frame = tk.Frame(root, bg='#64c8ff')
red_time_entry = tk.Entry(set_frame, bg='black', fg='white', font=('Digital-7 Mono', 40))
green_time_entry = tk.Entry(set_frame, bg='black', fg='white', font=('Digital-7 Mono', 40))
yellow_time_entry = tk.Entry(set_frame, bg='black', fg='white', font=('Digital-7 Mono', 40))
tk.Label(set_frame, text='Red light time:', bg='#64c8ff', fg='black', font=('Digital-7 Mono', 40)).pack(padx=30, pady=5)
red_time_entry.pack(padx=30, pady=5)
tk.Label(set_frame, text='Green light time:', bg='#64c8ff', fg='black', font=('Digital-7 Mono', 40)).pack(padx=30, pady=5)
green_time_entry.pack(padx=30, pady=5)
tk.Label(set_frame, text='Yellow light time:', bg='#64c8ff', fg='black', font=('Digital-7 Mono', 40)).pack(padx=30, pady=5)
yellow_time_entry.pack(padx=30, pady=5)
tk.Button(set_frame, text='Apply', command=apply_times, font=('Digital-7 Mono', 40)).pack(padx=30, pady=5)
times_apply_status_label = tk.Label(set_frame, text='Waiting', bg='#64c8ff', fg='black', font=('Digital-7 Mono', 40), wraplength=400)
times_apply_status_label.pack(padx=30, pady=5)
tk.Button(set_frame, text='Pedestrians crossing', command=pedestrians_crossing, font=('Digital-7 Mono', 40)).pack(padx=30, pady=5)
set_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.after(100, update_light)
root.focus_force()
root.mainloop()
