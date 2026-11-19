from base64 import b64encode as encode
from base64 import b64decode as decode
import tkinter as tk
from tkinter import scrolledtext
from random import randint
from pyperclip import copy, paste
import sys


# <-----创建函数----->
def tocode(text):  # 加密
    try:
        res = ''
        shift = randint(1000, 9999)  # 生成随机偏移量
        s4 = ''
        for a in text:  # 偏移字符
            s1 = ord(a)  # 1.先获取字符码点
            s2 = s1 + shift  # 2.再偏移字符
            s3 = chr(s2)  # 3.重新变回字符
            s4 += s3  # 4.添加到字符串
        s5 = encode(s4.encode('utf-8')).decode('utf-8')  # 给偏移后内容编码
        res = s5 + '#' + str(shift)  # 带上偏移量
    except BaseException as e:
        res = '加密失败\n%s:%s' % (type(e).__name__, e)
    # 显示结果
    ta12.delete('1.0', tk.END)
    ta12.insert(tk.END, res)
    return res


def totext(code):
    try:
        res = ''
        shift = int(code.split('#')[1])  # 获取偏移量
        context = code.split('#')[0]  # 获取编码密文
        context = decode(context.encode('utf-8')).decode('utf-8')  # 解码密文
        res = ''
        for a in context:  # 偏移回去
            s1 = ord(a)  # 获取偏移后的量
            s2 = s1 - shift  # 偏移回去
            s3 = chr(s2)  # 重新变回字符
            res += s3  # 添加到字符串
    except BaseException as e:
        res = '解密失败:\n%s:%s' % (type(e).__name__, e)
    # 显示明文
    ta22.delete('1.0', tk.END)
    ta22.insert(tk.END, res)
    return res


def pastecode():
    ta21.delete('1.0', tk.END)
    ta21.insert(tk.END, paste())


# <-----创建界面----->
root = tk.Tk()
root.geometry('930x730')

# 创建容器
fra1 = tk.LabelFrame(root, text='加密')
fra2 = tk.LabelFrame(root, text='解密')

# 创建加密区
la11 = tk.Label(fra1, text='明文:', font=(None, 15))
ta11 = scrolledtext.ScrolledText(fra1, wrap=tk.WORD, width=40, height=10, font=(None, 15), highlightbackground='gray', highlightcolor='red')
la12 = tk.Label(fra1, text='密文:', font=(None, 15))
ta12 = scrolledtext.ScrolledText(fra1, wrap=tk.WORD, width=40, height=10, font=(None, 15), highlightbackground='gray', highlightcolor='red')
bt11 = tk.Button(fra1, text='加密', font=(None, 15), command=lambda: tocode(ta11.get('1.0', 'end-1c')), state='normal')
bt12 = tk.Button(fra1, text='复制密文', font=(None, 15), command=lambda: copy(ta12.get('1.0', 'end-1c')))
bt13 = tk.Button(fra1, text='清空明文', font=(None, 15), command=lambda: ta11.delete('1.0', tk.END))

# pack加密区
la11.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
ta11.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
la12.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
ta12.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt11.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt12.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt13.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
root.update()

# 创建解密区
la21 = tk.Label(fra2, text='密文:', font=(None, 15))
ta21 = scrolledtext.ScrolledText(fra2, wrap=tk.WORD, width=40, height=10, font=(None, 15), highlightbackground='gray', highlightcolor='red')
la22 = tk.Label(fra2, text='明文:', font=(None, 15))
ta22 = scrolledtext.ScrolledText(fra2, wrap=tk.WORD, width=40, height=10, font=(None, 15), highlightbackground='gray', highlightcolor='red')
bt21 = tk.Button(fra2, text='解密', font=(None, 15), command=lambda: totext(ta21.get('1.0', 'end-1c')), state='normal')
bt22 = tk.Button(fra2, text='粘贴密文', font=(None, 15), command=pastecode)
bt23 = tk.Button(fra2, text='清空明文', font=(None, 15), command=lambda: ta22.delete('1.0', tk.END))

# pack解密区
la21.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
ta21.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
la22.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
ta22.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt21.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt22.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
bt23.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
root.update()

# 布局容器
fra1.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)
fra2.grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

# <-----窗口创建完成----->
root.update()
root.focus_force()

root.mainloop()
sys.exit()
