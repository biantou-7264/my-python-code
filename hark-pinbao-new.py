import tkinter as tk
from random import randint, choice

words = set('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]\\;\'"{}|:<>?!@#$%^&*()1234567890`~-=_+取我热过额发环境文俊唯粉姐姐粉就哦我发费金额低筋粉加我疯狂发扣肉饭就哦今晚就哦额文俊分无论金额佛佛教经卷佛让我跑粉我陪哦废品')
words = list(words)
texts = []


class Rain:
    def __init__(self):
        w = canvas.winfo_screenwidth()
        self.rain = canvas.create_text(randint(0, w), 0, text=choice(words), fill='#00ff00', font=('Arial', randint(20, 40)))
        self.speed = randint(10, 30)
        self.move()

    def move(self):
        h = canvas.winfo_height()
        x, y = canvas.coords(self.rain)
        if y > h:
            canvas.delete(self.rain)
            return
        canvas.move(self.rain, 0, self.speed)
        root.after(20, self.move)


def create():
    Rain()
    root.after(2, create)


def create_text(text=None):
    h = canvas.winfo_height()
    move_texts()
    if text is None:
        text = [choice(words) for _ in range(randint(100, 150))]
    texts.append(canvas.create_text(10, h, text=text, fill='#00c800', font=('Arial', 10), anchor=tk.W))
    root.after(100, create_text)


def move_texts():
    for text in texts:
        try:
            x, y = canvas.coords(text)
            if y < 0:
                canvas.delete(text)
                continue
            canvas.move(text, 0, -20)
        except ValueError:
            pass


root = tk.Tk()
root.title('黑客屏保')

canvas = tk.Canvas(root, width=400, height=400, bg='black')
canvas.pack(fill=tk.BOTH, expand=True)

root.bind('<Escape>', lambda e: root.destroy())
root.attributes('-fullscreen', True)
root.after(100, create)
root.after(20, create_text, '提示:快速按键盘,可以假装你是黑客')
root.after(21, create_text, '提示:按ESC可以退出')
root.focus_force()
root.mainloop()
