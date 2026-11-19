import tkinter as tk
from tkinter import ttk
from time import sleep
from random import randint

root = tk.Tk()
root.title('颜值检测器')
global valve
valve = 0


def start():
    global valve
    valve = 0
    for i in range(101):
        jindu['value'] = i
        valve += randint(8, 10)
        result['text'] = '%d/1000' % valve
        root.update()
        sleep(0.02)
    result['text'] = '1000/1000'


label = tk.Label(root, text='颜值检测器', font=(None, 50))
label.pack()
zuozhe = tk.Label(root, text='作者:扁头', font=(None, 20))
zuozhe.pack()
button = tk.Button(root, text='开始检测', command=start, font=(None, 30))
button.pack()
jindustyle = ttk.Style()
jindustyle.theme_use('classic')
jindustyle.configure('Horizontal.TProgressbar', thickness=20)
jindu = ttk.Progressbar(root, length=300, mode='determinate')
jindu.pack()
result = tk.Label(root, text='%d/1000' % valve, font=(None, 30))
result.pack()
root.mainloop()
