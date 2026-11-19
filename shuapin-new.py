import tkinter as tk
from pynput import keyboard
import pyautogui as pag
from pyperclip import copy
from tkinter import simpledialog as sd

"""
select_colors -> colors
ff -> 7f
64 -> 32
c8 -> 64

colors -> mouse_colors
7f -> c8
32 -> 50
64 -> 7f
"""
texts = ['老师上课玩手机!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
for i in range(1, 11):
    texts.append(str(i))
for i in ('老师好', '再见', '啊朋友再见', '逃之夭夭'):
    texts.append(i)
colors = ['#7f0000', '#7f3200', '#7f6400', '#007f00', '#00007f', '#64007f'] * 1000
mouse_colors = ['#c80000', '#c85000', '#c87f00', '#00c800', '#0000c8', '#7f00c8'] * 1000
select_colors = ['#ff0000', '#ff6400', '#ffc800', '#00ff00', '#0000ff', '#c800ff'] * 1000
r = False
ic = False
nup = False
ndn = False
nlt = False
nrt = False
nic = False
pag.PAUSE = 0
pag.FAILSAFE = True


class RadioButton:
    def __init__(self, color, select_color, mouse_color, text, text_color):
        self.canvas = tk.Canvas(root, width=200, height=20, bg=color)
        self.canvas.pack()
        self.color = color
        self.select_color = select_color
        self.mouse_color = mouse_color
        self.text = text
        self.mouse = False
        self.canvas.create_text(100, 10, text=text, font=('Arial', 10), anchor=tk.CENTER, fill=text_color)
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)
        root.after(100, self.change)

    def click(self, event):
        selected.set(self.text)

    def change(self):
        if selected.get() == self.text:
            self.canvas.config(bg=self.select_color)
        else:
            if self.mouse:
                self.canvas.config(bg=self.mouse_color)
            else:
                self.canvas.config(bg=self.color)
        root.after(20, self.change)

    def enter(self, event):
        self.mouse = True

    def leave(self, event):
        self.mouse = False


def s(k):
    global r, ic, nup, ndn, nlt, nrt
    if k == keyboard.Key.alt:
        if not r:
            r = True
        else:
            r = False
    if k == keyboard.Key.esc:
        r = False
    if k == keyboard.Key.ctrl:
        if not ic:
            ic = True
        else:
            ic = False
    if k == keyboard.Key.up:
        nup = True
    if k == keyboard.Key.down:
        ndn = True
    if k == keyboard.Key.left:
        nlt = True
    if k == keyboard.Key.right:
        nrt = True


def main():
    global r, ic, nup, ndn, nlt, nrt, nic
    if r:
        pag.click()
        pag.sleep(speed.get())
        copy(selected.get())
        pag.hotkey('command', 'v')
        pag.sleep(speed.get())
        pag.press('enter')
    if ic:
        nic = True
        root.withdraw()
    else:
        if nic:
            nic = False
            root.deiconify()
    if nup:
        nup = False
        try:
            i = texts.index(selected.get())
            i -= 1
            selected.set(texts[i])
        except ValueError:
            selected.set(texts[-1])
        except IndexError:
            selected.set(texts[-1])
        if ic:
            show_msg(selected.get())
    if ndn:
        ndn = False
        try:
            i = texts.index(selected.get())
            i += 1
            selected.set(texts[i])
        except ValueError:
            selected.set(texts[0])
        except IndexError:
            selected.set(texts[0])
        if ic:
            show_msg(selected.get())
    if nlt:
        nlt = False
        speed.set(speed.get() - 0.01)
        speed.set(round(speed.get(), 2))
        if speed.get() < 0:
            speed.set(0)
        if ic:
            show_msg(speed.get())
    if nrt:
        nrt = False
        speed.set(speed.get() + 0.01)
        speed.set(round(speed.get(), 2))
        if ic:
            show_msg(speed.get())
    root.after(20, main)


def set_speed(event):
    global speed
    user = sd.askfloat('提示', '请输入速度')
    if user:
        speed.set(user)


def show_msg(text):
    msg = tk.Toplevel(root)
    msg.title('message')
    msg.geometry('300x50+300+300')
    tk.Label(msg, text=text, font=('Arial', 30)).pack(padx=30, pady=5)
    root.after(200, msg.destroy)


def help():
    msg = tk.Toplevel(root)
    msg.title('help')
    context = """
    ======HELP======
    1.按alt/option开始停止刷屏;
    2.按ctrl显示隐藏窗口;
    3.按esc紧急停止
    4.按上下选择内容
    5.按左右选择速度
    """
    text = tk.Text(msg, width=30, height=10, font=('Arial', 10))
    text.pack(fill=tk.BOTH, expand=True)
    text.insert(tk.END, context)
    tk.Button(msg, text='关闭', command=msg.destroy, font=('Arial', 10)).pack(fill=tk.X, expand=True)


l = keyboard.Listener(on_press=s)
l.start()

root = tk.Tk()
root.title('刷屏器')
selected = tk.StringVar(value='')
speed = tk.DoubleVar(value=0.01)

for count, text in enumerate(texts):
    RadioButton(colors[count], select_colors[count], mouse_colors[count], text, 'white')
speed_label = tk.Label(root, textvariable=speed, font=('Arial', 10))
speed_label.pack()
speed_label.bind('<Button-1>', set_speed)
tk.Button(root, text='帮助', command=help, font=('Arial', 10)).pack(fill=tk.X, expand=True)
tk.Button(root, text='退出', command=root.destroy, font=('Arial', 10)).pack(fill=tk.X, expand=True)

root.after(100, main)
root.focus_force()
root.mainloop()

l.stop()
l.join()
