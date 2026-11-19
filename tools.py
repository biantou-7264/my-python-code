import tkinter as tk
from tkinter import messagebox as mb


class SpecialCharTool:
    def __init__(self):
        self.window = None
        self.box = None
        self.char_var = None
        self.title = None
        self.get_btn = None

    def start(self):
        self.window = tk.Toplevel(root)
        self.window.title('特殊字符工具')
        self.char_var = tk.StringVar()
        self.title = tk.Label(self.window, text='特殊字符工具', font=('Arial', 50))
        self.title.pack(padx=30, pady=10)
        choices = ['⌘', '⌥', '⌃', '⚠︎', 'ℹ︎', '⟳', '↵', '▲', '▣', '⚡︎', '⇧', '⇥', '⇪', '⌫', '⌦', '◼︎', '●', '√', '→', '←', '↑', '↓', '⎋']
        self.box = tk.OptionMenu(self.window, self.char_var, *choices)
        self.box.config(font=('Arial', 30))
        self.box['menu'].config(font=(None, 30))
        self.box.pack(padx=30, pady=10)
        self.get_btn = tk.Button(self.window, text='复制', command=self.get, font=('Arial', 30))
        self.get_btn.pack(padx=30, pady=10)

    def get(self):
        from pyperclip import copy
        copy(self.char_var.get())
        del copy


class UnicodeTool:
    def __init__(self):
        self.window = None
        self.uni_var = None
        self.title = None
        self.chr_btn = None
        self.ord_btn = None
        self.entry = None

    def start(self):
        self.window = tk.Toplevel(root)
        self.window.title('Unicode工具')
        self.uni_var = tk.StringVar(value='请输入...')
        self.title = tk.Label(self.window, text='Unicode工具', font=('Arial', 50))
        self.title.pack(padx=30, pady=10)
        self.entry = tk.Entry(self.window, textvariable=self.uni_var, font=('Arial', 30), highlightbackground='#646464')
        self.entry.pack(padx=30, pady=10)
        self.ord_btn = tk.Button(self.window, text='编码并复制', command=self.ord, font=('Arial', 30))
        self.ord_btn.pack(padx=30, pady=10)
        self.chr_btn = tk.Button(self.window, text='解码并复制', command=self.chr, font=('Arial', 30))
        self.chr_btn.pack(padx=30, pady=10)

    def chr(self):
        from pyperclip import copy
        try:
            copy(chr(int(self.uni_var.get())))
        except Exception:
            try:
                copy(chr(int(self.uni_var.get(), 16)))
            except Exception as e:
                mb.showerror('错误', e)
        del copy

    def ord(self):
        from pyperclip import copy
        try:
            copy(ord(self.uni_var.get()))
        except Exception as e:
            mb.showerror('错误', e)
        del copy


class CopyTool:
    def __init__(self):
        self.window = None
        self.txt_var = None
        self.title = None
        self.get_btn = None
        self.entry = None

    def start(self):
        self.window = tk.Toplevel(root)
        self.window.title('复制工具')
        self.txt_var = tk.StringVar(value='请输入...')
        self.title = tk.Label(self.window, text='复制工具', font=('Arial', 50))
        self.title.pack(padx=30, pady=10)
        self.entry = tk.Entry(self.window, textvariable=self.txt_var, font=('Arial', 30), highlightbackground='#646464')
        self.entry.pack(padx=30, pady=10)
        self.get_btn = tk.Button(self.window, text='复制', command=self.get, font=('Arial', 30))
        self.get_btn.pack(padx=30, pady=10)

    def get(self):
        from pyperclip import copy
        raw_str = self.txt_var.get()
        try:
            copy(raw_str.encode('utf-8').decode('unicode-escape'))
        except Exception as e:
            mb.showerror('错误', e)


class AverageTool:
    def __init__(self):
        self.window = None
        self.txt_var = None
        self.title = None
        self.get_btn = None
        self.entry = None

    def start(self):
        self.window = tk.Toplevel(root)
        self.window.title('平均数工具')
        self.txt_var = tk.StringVar(value='请输入...')
        self.title = tk.Label(self.window, text='平均数工具', font=('Arial', 50))
        self.title.pack(padx=30, pady=10)
        self.entry = tk.Entry(self.window, textvariable=self.txt_var, font=('Arial', 30), highlightbackground='#646464')
        self.entry.pack(padx=30, pady=10)
        self.get_btn = tk.Button(self.window, text='计算', command=self.get, font=('Arial', 30))
        self.get_btn.pack(padx=30, pady=10)

    def get(self):
        try:
            num = self.txt_var.get().split(',')
            a = 0
            for n in num:
                a += int(n)
            mb.showinfo('结果', a / len(num))
        except Exception as e:
            mb.showerror('错误', e)


class RgbHexTool:
    def __init__(self):
        self.window = None
        self.txt_var = None
        self.title = None
        self.chr_btn = None
        self.ord_btn = None
        self.entry = None

    def start(self):
        self.window = tk.Toplevel(root)
        self.window.title('RgbHex工具')
        self.txt_var = tk.StringVar(value='请输入...')
        self.title = tk.Label(self.window, text='RgbHex工具', font=('Arial', 50))
        self.title.pack(padx=30, pady=10)
        self.entry = tk.Entry(self.window, textvariable=self.txt_var, font=('Arial', 30), highlightbackground='#646464')
        self.entry.pack(padx=30, pady=10)
        self.ord_btn = tk.Button(self.window, text='to rgb', command=self.torgb, font=('Arial', 30))
        self.ord_btn.pack(padx=30, pady=10)
        self.chr_btn = tk.Button(self.window, text='to hex', command=self.tohex, font=('Arial', 30))
        self.chr_btn.pack(padx=30, pady=10)

    def torgb(self):
        try:
            num = self.txt_var.get()
            mb.showinfo('rgb结果', self.hex_to_rgb(num))
        except Exception as e:
            mb.showerror('错误', e)

    def tohex(self):
        try:
            num = self.txt_var.get()
            split_words = [',', ';', ':', '|', ' ', ' ，', '。', '-', '_', '——']
            for split_word in split_words:
                if split_word in num:
                    nums = num.split(split_word)
                    break
            temp = []
            for n in nums:
                temp.append(int(n))
            nums = temp
            mb.showinfo('hex结果', self.rgb_to_hex(*nums))
        except Exception as e:
            mb.showerror('错误', e)

    def hex_to_rgb(self, hex):
        rh = hex[1:3]
        gh = hex[3:5]
        bh = hex[5:7]
        r = int(rh, 16)
        g = int(gh, 16)
        b = int(bh, 16)
        return r, g, b

    def rgb_to_hex(self, r, g, b):
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        res = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        return res


def start_pycharm():
    import subprocess as sp
    sp.run(['open', '/Applications/PyCharm.app'])
    del sp


root = tk.Tk()
root.title('编程小工具')

tk.Label(root, text='编程小工具', font=('Arial', 50)).pack(padx=30, pady=10)
tk.Button(root, text='特殊字符工具', command=lambda: SpecialCharTool().start(), font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='Unicode工具', command=lambda: UnicodeTool().start(), font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='复制工具', command=lambda: CopyTool().start(), font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='平均数工具', command=lambda: AverageTool().start(), font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='RgbHex工具', command=lambda: RgbHexTool().start(), font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)
tk.Button(root, text='PyCharm', command=start_pycharm, font=('Arial', 30)).pack(padx=30, pady=10, fill=tk.X, expand=True)

root.focus_force()
root.mainloop()
