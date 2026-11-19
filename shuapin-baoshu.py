import pyautogui as pag
from pyperclip import copy
import tkinter as tk
from time import sleep

count_num = 3


def count():
    global count_num
    count_num -= 1
    count_label.config(text='还有%d秒!' % count_num)
    if count_num == 0:
        root.withdraw()
        root.update()
        shuapin()
    else:
        root.after(1000, count)


def shuapin():
    copy('开始报数!')
    pag.click()
    pag.hotkey('command', 'v')
    pag.write('\n')
    sleep(2)
    for i in range(1, 100):
        copy(str(i))
        pag.click()
        pag.hotkey('command', 'v')
        pag.write('\n')
        sleep(0.1)
    root.quit()


root = tk.Tk()
root.title('刷屏-报数-倒计时')

count_label = tk.Label(root, text='还有3秒!', font=('Arial', 50))
count_label.pack(padx=20, pady=20)

root.after(1000, count)
root.focus_force()
root.mainloop()
