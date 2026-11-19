import tkinter as tk
from tkinter import scrolledtext as st
from PIL import ImageTk


class Button:
    def __init__(self, master, width, height, bg='white', fg='black', text='', command=None, font=('Arial', 12), press_bg=None, hover_bg=None, icon=None):
        self.master = master
        self.bg = bg
        self.fg = fg
        self.text = text
        self.command = command
        self.width = width
        self.height = height
        self.font = font
        self.press_bg = press_bg
        self.hover_bg = hover_bg
        self.icon = icon
        self.canvas = tk.Canvas(self.master, bg=self.bg, width=self.width, height=self.height)
        self.bind = self.canvas.bind
        self.canvas.create_text(self.width / 2, self.height / 2, text=self.text, fill=self.fg, font=self.font)
        self.canvas.bind('<ButtonPress-1>', self.press)
        self.canvas.bind('<ButtonRelease-1>', self.release)
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)
        if icon is not None:
            self.icon_img = ImageTk.PhotoImage(icon)
            self.canvas.create_image(10, self.height / 2, image=self.icon_img, anchor=tk.W)

    def press(self, event):
        if self.press_bg:
            self.canvas.config(bg=self.press_bg)

    def release(self, event):
        if self.hover_bg:
            self.canvas.config(bg=self.hover_bg)
        else:
            self.canvas.config(bg=self.bg)
        if self.command:
            self.command()

    def enter(self, event):
        if self.hover_bg:
            self.canvas.config(bg=self.hover_bg)

    def leave(self, event):
        self.canvas.config(bg=self.bg)

    def pack(self, **kw):
        self.canvas.pack(**kw)

    def grid(self, **kw):
        self.canvas.grid(**kw)

    def place(self, **kw):
        self.canvas.place(**kw)


class CircleProgessBar:
    def __init__(self, master, width, height, bg='black', highlightbg='gray', highlight='white', show_text=False, text_color='white', font=('Arial', 12)):
        self.master = master
        self.width = width
        self.height = height
        self.bg = bg
        self.highlightbg = highlightbg
        self.highlight = highlight
        self.show_text = show_text
        self.text_color = text_color
        self.font = font
        self.progess = 0
        self.canvas = tk.Canvas(self.master, bg=self.bg, width=self.width, height=self.height)
        self.canvas.create_arc(30, 30, self.width - 30, self.height - 30, start=90, extent=359.999999999, outline=self.highlightbg, style=tk.ARC, width=5)
        angle = self.progess * 3.6
        self.highlight_arc = self.canvas.create_arc(30, 30, self.width - 30, self.height - 30, start=90, extent=angle * -1, outline=self.highlight, style=tk.ARC, width=5)
        self.text = self.canvas.create_text(self.width / 2, self.height / 2, text='%d%%' % self.progess, fill=self.text_color, font=self.font)

    def pack(self, **kw):
        self.canvas.pack(**kw)

    def grid(self, **kw):
        self.canvas.grid(**kw)

    def place(self, **kw):
        self.canvas.place(**kw)

    def set_progess(self, progess):
        self.progess = progess
        angle = self.progess * 3.6
        self.canvas.itemconfig(self.highlight_arc, extent=angle * -1)
        self.canvas.itemconfig(self.text, text='%d%%' % self.progess)

    def demo(self, i=0):
        if i > 100:
            i = 0
        self.set_progess(i + 1)
        self.master.after(100, self.demo, i + 1)


class Scale:
    def __init__(self, master, width, height, value_var, bg='black', highlightbg='gray', highlight='white', show_text=False, text_color='white', font=('Arial', 12), press_bg='gray', hover_bg=None, _min=0, _max=100):
        self.master = master
        self.width = width
        self.height = height
        self.bg = bg
        self.highlightbg = highlightbg
        self.highlight = highlight
        self.show_text = show_text
        self.text_color = text_color
        self.font = font
        self.progess = 0
        self.press_bg = press_bg
        self.hover_bg = hover_bg
        self.min = _min
        self.max = _max
        self.value = 0
        if value_var:
            value_var.trace_add('write', lambda *args: self.var_change())
        self.value_var = value_var
        self.canvas = tk.Canvas(self.master, bg=self.bg, width=self.width, height=self.height)
        self.scalebg = self.canvas.create_rectangle(0, 0, self.progess * (self.width / 100), self.height, fill=self.highlightbg)
        self.scale = self.canvas.create_rectangle(0, 0, 30, self.height, fill=self.highlight, width=0)
        self.text = self.canvas.create_text(0, self.height / 2, text='%d' % self.progess, fill=self.text_color, font=self.font, anchor=tk.W)
        self.canvas.tag_bind(self.scale, '<B1-Motion>', self.drag)
        self.canvas.tag_bind(self.scale, '<ButtonPress-1>', self.press)
        self.canvas.tag_bind(self.scale, '<ButtonRelease-1>', self.release)
        self.canvas.tag_bind(self.scale, '<Enter>', self.enter)
        self.canvas.tag_bind(self.scale, '<Leave>', self.leave)
        self.canvas.tag_bind(self.text, '<B1-Motion>', self.drag)
        self.canvas.tag_bind(self.text, '<ButtonPress-1>', self.press)
        self.canvas.tag_bind(self.text, '<ButtonRelease-1>', self.release)
        self.canvas.tag_bind(self.text, '<Enter>', self.enter)
        self.canvas.tag_bind(self.text, '<Leave>', self.leave)

    def pack(self, **kw):
        self.canvas.pack(**kw)

    def grid(self, **kw):
        self.canvas.grid(**kw)

    def place(self, **kw):
        self.canvas.place(**kw)

    def set_progess(self, progess):
        self.progess = progess
        if progess < 0:
            self.progess = 0
        if progess > 100:
            self.progess = 100
        self.value = self.min + (self.max - self.min) * (self.progess / 100)
        self.value_var.set(self.value)
        self.canvas.coords(self.scalebg, 0, 0, self.progess * (self.width / 100), self.height)
        self.canvas.coords(self.scale, self.progess * (self.width / 100), 0, self.progess * (self.width / 100) + 30, self.height)
        self.canvas.coords(self.text, self.progess * (self.width / 100), self.height / 2)
        self.canvas.itemconfig(self.text, text='%d' % self.value)

    def drag(self, event):
        self.set_progess(event.x / self.width * 100 - 5)

    def press(self, event):
        if self.press_bg:
            self.canvas.itemconfig(self.scale, fill=self.press_bg)

    def release(self, event):
        if self.hover_bg:
            self.canvas.itemconfig(self.scale, fill=self.hover_bg)
        else:
            self.canvas.itemconfig(self.scale, fill=self.bg)

    def enter(self, event):
        if self.hover_bg:
            self.canvas.itemconfig(self.scale, fill=self.hover_bg)

    def leave(self, event):
        self.canvas.itemconfig(self.scale, fill=self.highlight)

    def var_change(self):
        self.set_progess(self.value_var.get())


class Entry:
    def __init__(self, master, width, height, var, font=('Arial', 20), bg='white', fg='black', hightlight='#000032'):
        self.master = master
        self.width = width
        self.height = height
        self.var = var
        self.font = font
        self.bg = bg
        self.fg = fg
        self.focus = False
        self.hightlight = hightlight
        self.canvas = tk.Canvas(self.master, bg=self.bg, width=self.width, height=self.height)
        self.text = self.canvas.create_text(10, self.height / 2, text=var.get(), font=self.font, anchor=tk.W)
        if var:
            var.trace_add('write', lambda *args: self.var_change())
        self.canvas.bind('<Button-1>', self.focus_set)
        self.master.bind('<Escape>', self.focus_cancel)
        self.master.bind('<Key>', self.onkey)

    def pack(self, **kw):
        self.canvas.pack(**kw)

    def grid(self, **kw):
        self.canvas.grid(**kw)

    def place(self, **kw):
        self.canvas.place(**kw)

    def focus_set(self, event=None):
        self.focus = True
        self.update_hightlight()

    def focus_cancel(self, event=None):
        self.focus = False
        self.update_hightlight()

    def update_hightlight(self):
        if self.focus:
            self.canvas.config(bg=self.hightlight)
        else:
            self.canvas.config(bg=self.bg)

    def onkey(self, event):
        if self.focus:
            if event.keysym == 'BackSpace':
                self.delete_end()
            self.insert(event.char)

    def insert(self, char):
        text = self.canvas.itemcget(self.text, 'text')
        self.canvas.itemconfig(self.text, text=text + char)

    def delete_end(self):
        text = self.canvas.itemcget(self.text, 'text')
        self.canvas.itemconfig(self.text, text=text[:-1])


class MessageBox:
    def __init__(self, master):
        self.master = master

    def show_info(self, title, prompt, font=('Arial', 12), bg='white', fg='black', press_bg='#ffffc8', hover_bg='#c8c8ff'):
        window = tk.Toplevel(self.master)
        text = st.ScrolledText(window, width=50, height=30, font=font)
        text.insert('1.0', prompt)
        text.pack(fill=tk.BOTH, expand=True)
        window.title(title)
        Button(window, width=200, height=50, text='OK', command=window.destroy, font=('Arial', 30), bg=bg, fg=fg, press_bg=press_bg, hover_bg=hover_bg).pack()
        window.focus_force()
        window.mainloop()


def test():
    def show_msg():
        msg = MessageBox(root)
        prompt = """
        哈哈哈哈!
        你居然点了按钮!
        """
        msg.show_info('哈哈哈', prompt, bg='red', fg='green', press_bg='orange', hover_bg='#c80000')

    root = tk.Tk()
    temp = tk.StringVar()
    Button(root, 200, 50, text='test', font=('Arial', 30), bg='red', fg='green', press_bg='orange', hover_bg='#c80000', command=show_msg).pack(padx=10, pady=10)
    progessbar = CircleProgessBar(root, 300, 300, show_text=True, font=('Arial', 30), bg='black', highlightbg='red', highlight='green', text_color='blue')
    progessbar.pack(padx=10, pady=10)
    progessbar.demo()
    Scale(root, 300, 50, temp, show_text=True, font=('Arial', 20), bg='black', highlightbg='orange', highlight='green', text_color='blue', press_bg='yellow', hover_bg='#00c800', _min=123, _max=456).pack(padx=10, pady=10)
    Entry(root, 300, 50, temp, font=('Arial', 20), bg='red', fg='green', hightlight='orange').pack(padx=10, pady=10)
    root.focus_force()
    root.mainloop()


if __name__ == '__main__':
    test()
