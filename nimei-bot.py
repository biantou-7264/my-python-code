import tkinter as tk
import jieba
from tkinter import scrolledtext as st
from random import choice, randint

symbols = set('!,.，?。？！“”\'\"》《、 ')
print('符号集合: %s' % '和'.join(symbols))


def stdout(a):
    text.insert(tk.END, a + '\n')
    text.see(tk.END)
    root.update()


def send(event):
    try:
        stdout('人: %s' % entry.get())
        if '你妹' in entry.get():
            stdout('AI: 你妈!')
        elif '你妈' in entry.get():
            stdout('AI: 你爹!')
        elif '你爹' in entry.get():
            stdout('AI: 你大爷!')
        elif '你大爷' in entry.get():
            stdout('AI: 你大奶!')
        elif '你大奶' in entry.get():
            stdout('AI: 你弟!')
        elif '你弟' in entry.get():
            stdout('AI: 你全家!')
        elif '你全家' in entry.get():
            stdout('AI: 开启鬼畜')
            root.after(100, guichu)
        else:
            words = jieba.lcut(entry.get())
            if len(words) == 0:
                words = [entry.get()]
            print('分词结果: %s' % words)
            for word in words:
                if word in symbols:
                    words.remove(word)
            print('替换后分词结果: %s' % words)
            word = choice(words)
            stdout('AI: %s你妹' % word)
        entry.delete(0, tk.END)
    except Exception as e:
        stdout('%s:%s' % (type(e).__name__, e))
        words = jieba.lcut(str(e))
        if len(words) == 0:
            words = [entry.get()]
        print('分词结果: %s' % words)
        for word in words:
            if word in symbols:
                words.remove(word)
        print('替换后分词结果: %s' % words)
        word = choice(words)
        stdout('AI: %s你妹' % word)
        entry.delete(0, tk.END)


def reset():
    stdout('系统: 开始初始化')

    words = '你妹, 打工人, YYDS, 傻, 学习, 胖, 抖音'.split(', ')
    for word in words:
        jieba.add_word(word)
        print('[初始化] 添加了%s' % word)

    stdout('系统: 初始化完成')

    stdout('AI: 你好, 我是你妹机器人!')
    stdout('AI: 我最喜欢说“你妹”了!')


def guichu(count=1):
    win = tk.Toplevel(root)
    win.title('我是第%d个窗口' % count)
    win.configure(background=rgb_to_hex(randint(0, 255), randint(0, 255), randint(0, 255)))
    win.geometry('300x300')
    root.after(1, guichu, count + 1)


def rgb_to_hex(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    res = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return res


root = tk.Tk()
root.title('你妹机器人')

text = st.ScrolledText(root, font=('Arial', 12), highlightbackground='white', highlightcolor='blue')
text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=('Arial', 12), highlightbackground='white')
entry.pack(padx=10, pady=10, fill=tk.X)
entry.bind('<Return>', send)

root.after(100, reset)

root.focus_force()
root.mainloop()
