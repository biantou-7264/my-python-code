import tkinter as tk
from tkinter import filedialog as fd
from tkinter import scrolledtext as st


def write():
    stdout('写入秘密')
    try:
        with open(path.get(), 'ab') as file:
            file.write(text.get().encode('utf-8'))
        stdout('已写入秘密')
    except BaseException as e:
        stdout('发生错误:%s:%s' % (type(e).__name__, str(e)))


def read():
    stdout('读取秘密')
    try:
        with open(path.get(), 'rb') as file:
            data = file.read()
            text = data.split(b'IEND')[1]
            stdout(text)
    except BaseException as e:
        stdout('发生错误:%s:%s' % (type(e).__name__, str(e)))


def delete():
    stdout('删除秘密')
    try:
        with open(path.get(), 'rb') as file:
            data = file.read()
            photo = data.split(b'IEND')[0]
        with open(path.get(), 'wb') as file:
            file.write(photo)
        stdout('已删除秘密')
    except BaseException as e:
        stdout('发生错误:%s:%s' % (type(e).__name__, str(e)))


def choose(event):
    choose_path = fd.askopenfilename(title='请选择图片', filetypes=[('PNG图片', '*.png')])
    if choose_path:
        path.set(choose_path)
        stdout('已选择:%s' % choose_path)
    else:
        stdout('已取消选择')


def stdout(text):
    text_area.insert(tk.END, text)
    text_area.see(tk.END)
    text_area.insert(tk.END, '\n')


root = tk.Tk()
root.title('图片藏秘密')
root.configure(background='#323232')

path = tk.StringVar(value='点击选择图片')
text = tk.StringVar(value='请输入文本')

path_label = tk.Label(root, textvariable=path, font=('Arial', 40), bg='black', fg='white')
path_label.pack(fill=tk.X, expand=True, padx=10, pady=10)
path_label.bind('<Button-1>', choose)
text_entry = tk.Entry(root, textvariable=text, font=('Arial', 40), bg='black', fg='white', highlightbackground='white', highlightthickness=2)
text_entry.pack(fill=tk.X, expand=True, padx=10, pady=10)
write_btn = tk.Button(root, text='写入秘密', font=('Arial', 30), command=write, bg='white', fg='black')
write_btn.pack(fill=tk.X, expand=True, padx=10, pady=10)
read_btn = tk.Button(root, text='读取秘密', font=('Arial', 30), command=read, bg='white', fg='black')
read_btn.pack(fill=tk.X, expand=True, padx=10, pady=10)
del_btn = tk.Button(root, text='删除秘密', font=('Arial', 30), command=delete, bg='white', fg='black')
del_btn.pack(fill=tk.X, expand=True, padx=10, pady=10)
text_area = st.ScrolledText(root, height=20, width=40, font=(None, 10))
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.focus_force()
root.mainloop()
