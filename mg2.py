import tkinter as tk
from time import sleep

root = tk.Tk()


def start():
    for i in range(0, 100):
        loading.config(text='%d%%' % i)
        root.update()
        sleep(i * 0.001)
    sleep(2)
    loading.config(text='0%')
    root.update()
    global error
    error = tk.Toplevel(root)
    errorlabel = tk.Label(error, text='体重过胖,启动失败', font=(None, 30))
    errorlabel.pack()
    errorbutton = tk.Button(error, text='退出', command=lambda: error.destroy(), font=(None, 20))
    errorbutton.pack()


root.title('mumget启动器')
label = tk.Label(root, text='MUMGET', font=(None, 50))
label.pack()
button = tk.Button(root, text='启动', command=start, font=(None, 30))
button.pack()
loading = tk.Label(root, text='0%', font=(None, 20))
loading.pack()

root.focus_force()
root.mainloop()