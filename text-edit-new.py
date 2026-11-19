import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import filedialog as fd


def open_file(event=None):
    user = fd.askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if user:
        file_path.set(user)
        try:
            with open(file_path.get(), 'r') as file:
                for line in file:
                    text_area.insert(tk.END, line)
        except BaseException as e:
            print(e)


def save_file(event=None):
    if not file_path.get():
        user = fd.asksaveasfilename(filetypes=[('Text Files', '*.txt')])
        if user:
            file_path.set(user)
        else:
            return
    try:
        with open(file_path.get(), 'w') as file:
            file.write(text_area.get(1.0, tk.END))
    except BaseException as e:
        print(e)


def saveas_file(event=None):
    user = fd.asksaveasfilename(filetypes=[('Text Files', '*.txt')])
    if user:
        file_path.set(user)
    else:
        return
    try:
        with open(file_path.get(), 'w') as file:
            file.write(text_area.get(1.0, tk.END))
    except BaseException as e:
        print(e)


root = tk.Tk()
root.title('简易文本编辑')
file_path = tk.StringVar(value='')

text_area = st.ScrolledText(root, width=100, height=40, font=('Arial', 15))
text_area.pack(fill=tk.BOTH, expand=True)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=False)
file_menu.add_command(label='打开', command=open_file, accelerator='Command+O')
file_menu.add_command(label='保存', command=save_file, accelerator='Command+S')
file_menu.add_command(label='另存为', command=saveas_file, accelerator='Command+Option+S')
menu_bar.add_cascade(label='文件', menu=file_menu)
root.config(menu=menu_bar)

root.bind('<Command-o>', open_file)
root.bind('<Command-s>', save_file)
root.bind('<Option-Command-s>', saveas_file)

root.focus_force()
root.mainloop()
