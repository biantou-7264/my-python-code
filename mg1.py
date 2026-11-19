import tkinter as tk
from time import sleep


def start():
    global starttest
    starttest = tk.Toplevel(root)
    starttest.title('mumget-即将开始')
    testinglabel = tk.Label(starttest, text='正在检测周围环境…', font=('Arial', 30))
    testinglabel.pack()
    starttest.after(2000, start2)


def start2():
    starttest.destroy()
    global cantstart
    cantstart = tk.Toplevel(root)
    cantstart.title('mumget-错误')
    cantstartlabel = tk.Label(cantstart, text='附近有大肥猪,无法启动', font=('Arial', 20))
    cantstartlabel.pack()
    cantstartexit = tk.Button(cantstart, text='好的', command=quitcant, width=15, height=1, font=('Arail', 20))
    cantstartexit.pack()


def quitcant():
    cantstart.destroy()


root = tk.Tk()
root.title('mumget-首页')
label = tk.Label(root, text='MUMGET', font=('Arial', 50))
label.pack()
button1 = tk.Button(root, text='开始', command=start, width=15, height=2, font=('Arail', 20))
button1.pack()
root.mainloop()
