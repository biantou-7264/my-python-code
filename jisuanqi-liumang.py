import tkinter as tk
import os

calculation_ok = False
m = 0


class Button:
    def __init__(self, x, y, w, h, text='', color='black', press_color='white', command=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.press_color = press_color
        self.btn = canvas.create_oval(self.x, self.y, self.x + w, self.y + h, fill=color, outline='white', width=0)
        self.btn_text = canvas.create_text(self.x + w // 2, self.y + h // 2, text=self.text, font=('Arial', w // 2), fill='white', anchor=tk.CENTER)
        self.command = command
        canvas.tag_bind(self.btn, '<Button-1>', self.press)
        canvas.tag_bind(self.btn, '<ButtonRelease-1>', self.release)
        canvas.tag_bind(self.btn_text, '<Button-1>', self.press)
        canvas.tag_bind(self.btn_text, '<ButtonRelease-1>', self.release)
        canvas.tag_bind(self.btn, '<Enter>', self.enter)
        canvas.tag_bind(self.btn, '<Leave>', self.leave)
        canvas.tag_bind(self.btn_text, '<Enter>', self.enter)
        canvas.tag_bind(self.btn_text, '<Leave>', self.leave)

    def press(self, event):
        canvas.itemconfig(self.btn, fill=self.press_color)

    def release(self, event):
        canvas.itemconfig(self.btn, fill=self.color)
        if self.command is not None:
            self.command()

    def enter(self, event):
        canvas.itemconfig(self.btn, width=5)

    def leave(self, event):
        canvas.itemconfig(self.btn, width=0)


class BuyTips:
    def __init__(self):
        self.window = tk.Toplevel(root)
        self.window.configure(background='#0a0e27')
        self.window.title('需要购买')
        tk.Label(self.window, text='需要¥5才可以显示以下算式的答案', font=('Arial', 30), bg='#0a0e27').pack(padx=10, pady=10)
        tk.Label(self.window, text=result.get(), font=('Arial', 30), bg='#165Dff').pack(padx=10, pady=10, ipadx=10, ipady=10, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.window, height=50, width=300, bg='#165Dff')
        self.canvas.pack(padx=10, pady=10)
        self.canvas.create_text(150, 25, text='立即购买!', font=('Arial', 30), anchor=tk.CENTER)
        self.canvas.bind('<Button-1>', self.press)
        self.canvas.bind('<ButtonRelease-1>', self.release)
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)

    def press(self, event):
        self.canvas.config(bg='#3D7fff')

    def release(self, event):
        self.canvas.config(bg='#165Dff')
        BuyWindow(self.window)

    def enter(self, event):
        self.canvas.config(bg='#3177ff')

    def leave(self, event):
        self.canvas.config(bg='#165Dff')


class BuyWindow:
    def __init__(self, last_window):
        self.window = tk.Toplevel(root)
        self.window.title('Buy')
        self.last_window = last_window
        tk.Label(self.window, text='Buy  ¥5', anchor=tk.W, font=('Arial', 20)).pack(padx=(20, 200), pady=10)
        tk.Label(self.window, text='👤%s' % os.getenv('USER'), anchor=tk.W, font=('Arial', 20)).pack(padx=(20, 200), pady=10)
        tk.Label(self.window, text='password:', font=('Arial', 20)).pack(padx=(20, 200), pady=10)
        entry = tk.Entry(self.window, font=('Arial', 20), show='●', width=40, highlightbackground='white')
        entry.pack(padx=20, pady=10)
        entry.bind('<Return>', self.buy)
        entry.focus_set()

    def buy(self, event):
        really_cal()
        self.window.destroy()
        self.last_window.destroy()


def input_num(text):
    global result, calculation_ok
    if calculation_ok:
        result.set('0')
    if result.get() == '0':
        result.set(text)
    else:
        result.set(result.get() + text)
    calculation_ok = False


def input_txt(text):
    global result, calculation_ok
    result.set(result.get() + text)
    calculation_ok = False


def clear():
    global result
    result.set('0')


def back():
    global result
    if len(result.get()) == 1:
        result.set('0')
    else:
        result.set(result.get()[:-1])


def flip_sign():
    global result
    try:
        result.set(float(result.get()) * -1)
    except ValueError:
        pass


def really_cal():
    global result, calculation_ok
    try:
        result.set(eval(result.get()))
        calculation_ok = True
    except ZeroDivisionError:
        result.set('不能除以0')
    except SyntaxError:
        result.set('算式错误')


def calculation():
    BuyTips()


def mc():
    global m
    m = 0


def mr():
    global m, result, calculation_ok
    calculation_ok = False
    result.set(m)


def m_plus():
    global m, result
    try:
        m += int(result.get())
    except ValueError:
        pass


def m_minus():
    global m, result
    try:
        m -= int(result.get())
    except ValueError:
        pass


root = tk.Tk()
root.title('好看的计算器')
root.configure(bg='#0a0e27')
result = tk.StringVar(value='0')

res_label = tk.Label(root, textvariable=result, font=('Arial', 50), bg='#165Dff', fg='white', anchor=tk.E)
res_label.pack(fill=tk.X, expand=True)
canvas = tk.Canvas(root, height=550, width=400, bg='#0a0e27')
canvas.pack(fill=tk.BOTH, expand=True)
Button(15, 15, 70, 70, text='MC', color='#39c814', press_color='#39ff14', command=mc)
Button(105, 15, 70, 70, text='MR', color='#39c814', press_color='#39ff14', command=mr)
Button(195, 15, 70, 70, text='M+', color='#39c814', press_color='#39ff14', command=m_plus)
Button(285, 15, 70, 70, text='M-', color='#39c814', press_color='#39ff14', command=m_minus)
Button(15, 105, 70, 70, text='C', color='#ff2a95', press_color='#ff7faf', command=clear)
Button(105, 105, 70, 70, text='<', color='#ff2a95', press_color='#ff7faf', command=back)
Button(195, 105, 70, 70, text='±', color='#ff2a95', press_color='#ff7faf', command=flip_sign)
Button(285, 105, 70, 70, text='+', color='#a239ff', press_color='#e2a9ff', command=lambda: input_txt('+'))
Button(15, 195, 70, 70, text='1', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('1'))
Button(105, 195, 70, 70, text='2', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('2'))
Button(195, 195, 70, 70, text='3', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('3'))
Button(285, 195, 70, 70, text='-', color='#a239ff', press_color='#e2a9ff', command=lambda: input_txt('-'))
Button(15, 285, 70, 70, text='4', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('4'))
Button(105, 285, 70, 70, text='5', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('5'))
Button(195, 285, 70, 70, text='6', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('6'))
Button(285, 285, 70, 70, text='x', color='#a239ff', press_color='#e2a9ff', command=lambda: input_txt('*'))
Button(15, 375, 70, 70, text='7', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('7'))
Button(105, 375, 70, 70, text='8', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('8'))
Button(195, 375, 70, 70, text='9', color='#165Dff', press_color='#3D7fff', command=lambda: input_num('9'))
Button(285, 375, 70, 70, text='÷', color='#a239ff', press_color='#e2a9ff', command=lambda: input_txt('/'))
Button(15, 465, 70, 70, text='#', color='#ff2a95', press_color='#ff7faf', command=root.quit)
Button(105, 465, 70, 70, text='0', color='#165Dff', press_color='#3D7ffF', command=lambda: input_num('0'))
Button(195, 465, 70, 70, text='.', color='#ff2a95', press_color='#ff7faf', command=lambda: input_txt('.'))
Button(285, 465, 70, 70, text='=', color='#a239ff', press_color='#e2a9ff', command=calculation)

root.bind('<Key-1>', lambda event: input_num('1'))
root.bind('<Key-2>', lambda event: input_num('2'))
root.bind('<Key-3>', lambda event: input_num('3'))
root.bind('<Key-4>', lambda event: input_num('4'))
root.bind('<Key-5>', lambda event: input_num('5'))
root.bind('<Key-6>', lambda event: input_num('6'))
root.bind('<Key-7>', lambda event: input_num('7'))
root.bind('<Key-8>', lambda event: input_num('8'))
root.bind('<Key-9>', lambda event: input_num('9'))
root.bind('<Key-0>', lambda event: input_num('0'))
root.bind('<Escape>', lambda event: root.quit())
root.bind('c', lambda event: clear())
root.bind('<BackSpace>', lambda event: back())
root.bind('<plus>', lambda event: input_txt('+'))
root.bind('<minus>', lambda event: input_txt('-'))
root.bind('<asterisk>', lambda event: input_txt('*'))
root.bind('<slash>', lambda event: input_txt('/'))
root.bind('<period>', lambda event: input_txt('.'))
root.bind('<Return>', lambda event: calculation())
root.bind('<equal>', lambda event: calculation())

root.focus_force()
root.mainloop()
