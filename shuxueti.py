from tkinter import messagebox, simpledialog
import tkinter as tk
import random as r
import sys

root = tk.Tk()
root.title('首页')
ask_you = 0
answer = 0
sco = 0
difficulty = 20


def random_blem():
    global a, b, answer, ask_you
    a = r.randint(0, difficulty)
    b = r.randint(0, difficulty)
    answer = a + b
    ask_you = '%d+%d' % (a, b)
    scolabel.config(text=sco)
    blem.config(text=ask_you)


def yes(debug=0):
    global sco
    if entry.get() == str(answer):
        sco += 1
        messagebox.showinfo('提示', '答对了')
    else:
        messagebox.showinfo('提示', '答错了')
    random_blem()
    entry.delete(0, 'end')
    root.focus_force()
    entry.focus_set()


def iwta():
    messagebox.showinfo('提示', '答案是%d' % answer)
    root.focus_force()
    entry.focus_set()


def more():
    global option
    option = tk.Tk()
    option.title('选项')
    option.geometry('200x200')
    option.bind("<Escape>", quitoption)
    global difficultydisplay
    difficultydisplay = tk.Label(option, text='难度:%d' % difficulty)
    difficultydisplay.pack()
    difficultybtn = tk.Button(option, text='设置难度', command=setdifficulty)
    difficultybtn.pack()
    switchbtn = tk.Button(option, text='切换题目', command=switch)
    switchbtn.pack()
    quitbtn = tk.Button(option, text='退出程序', command=quitcommand)
    quitbtn.pack()
    option.focus_force()


def setdifficulty():
    userinput = simpledialog.askstring('设置', '请输入难度')
    if not userinput is None:
        if userinput.isdigit():
            if int(userinput) > 10000:
                messagebox.showinfo('友情提示', '这是一个很高的难度，建议心脏病患者不要挑战该难度，必要时可以看答案')
            global difficulty
            difficulty = int(userinput)
            difficultydisplay.config(text='难度:%d' % difficulty)
        else:
            messagebox.showinfo('提示', '难度只能是一个大于等于0的整数')


def quitcommand():
    if messagebox.askokcancel(title='重要提示', message='确定要退出程序吗'):
        try:
            option.destroy()
        except:
            pass
        root.destroy()
        sys.exit()


def switch():
    random_blem()
    entry.delete(0, 'end')


def quitoption(debug=0):
    try:
        option.destroy()
    except:
        pass


root.protocol("WM_DELETE_WINDOW", quitcommand)
scolabel = tk.Label(root, text=sco)
scolabel.pack()
blem = tk.Label(root, text=ask_you)
blem.pack()
entry = tk.Entry(root, width=30)
entry.pack()
ok = tk.Button(root, text='确定', command=yes)
ok.pack()
idk = tk.Button(root, text='我不会', command=iwta)
idk.pack()
morebtn = tk.Button(root, text='更多选项', command=more)
morebtn.pack()
root.bind("<Return>", yes)
random_blem()
root.focus_force()
entry.focus_set()
root.mainloop()
