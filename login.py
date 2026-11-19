import tkinter as tk
from random import choice
import cv2
from datetime import datetime

texts = list('qwertyuiopasdfghjklzxcvbnm1234567890')
users = {
    'biantou': 'asdfghjkl',
    'admin': '7264',
    'big fat pig': 'fat'
}
show_password = False
try_count = 0


def login():
    global captcha, try_count
    if try_count >= 3:
        tip_label.config(text='密码输错太多次了,已锁定!')
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cv2.waitKey(1000)
        ret, frame = camera.read()
        if ret:
            now = datetime.now()
            cv2.imwrite('入侵者%d年%d月%d日%d时%d分%d秒.jpg' % (now.year, now.month, now.day, now.hour, now.minute, now.second), frame)
        camera.release()
        cv2.destroyAllWindows()
        return
    if user_entry.get() in users:
        if users.get(user_entry.get()) == password_entry.get():
            if captcha_entry.get() == captcha:
                tip_label.config(text='登录成功!欢迎%s' % user_entry.get())
                try_count = 0
            else:
                tip_label.config(text='验证码错误')
                captcha_entry.delete(0, tk.END)
                captcha = ''
                for _ in range(4):
                    captcha += choice(texts)
                captcha_text.config(text=captcha)
        else:
            try_count += 1
            tip_label.config(text='密码错误,还剩%d次机会' % (3 - try_count))
            password_entry.delete(0, tk.END)
            if try_count >= 3:
                tip_label.config(text='密码输错太多次了,已锁定!')
                camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                cv2.waitKey(1000)
                ret, frame = camera.read()
                if ret:
                    now = datetime.now()
                    cv2.imwrite('入侵者%d年%d月%d日%d时%d分%d秒.jpg' % (now.year, now.month, now.day, now.hour, now.minute, now.second), frame)
                camera.release()
                cv2.destroyAllWindows()
                return
    else:
        tip_label.config(text='用户不存在')
        user_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def show_password_set():
    global show_password
    show_password = not show_password
    if show_password:
        password_entry.config(show='')
        tip_label.config(text='注意:已显示密码')
    else:
        password_entry.config(show='*')
        tip_label.config(text='已隐藏密码')


root = tk.Tk()
root.title('登录页面模拟器')
root.configure(background='#323232')

title = tk.Label(root, text='欢迎使用xxx系统', font=('Arial', 40), fg='white', bg='#323232')
title.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

user_label = tk.Label(root, text='用户名:', font=('Arial', 30), fg='white', bg='#323232')
user_label.grid(row=1, column=0, pady=10, padx=10, sticky=tk.W)
user_entry = tk.Entry(root, width=20, font=('Arial', 30), fg='white', bg='#323232', highlightbackground='#c8c8c8')
user_entry.grid(row=1, column=1, pady=10, padx=10, sticky=tk.W)

password_label = tk.Label(root, text='密码:', font=('Arial', 30), fg='white', bg='#323232')
password_label.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)
password_entry = tk.Entry(root, width=20, font=('Arial', 30), fg='white', bg='#323232', highlightbackground='#c8c8c8', show='*')
password_entry.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)
show_password_btn = tk.Button(root, text='显示/隐藏密码', font=('Arial', 30), fg='black', bg='#323232', command=show_password_set)
show_password_btn.grid(row=3, column=0, pady=10, padx=10, columnspan=1000, sticky=tk.EW)

captcha_label = tk.Label(root, text='验证码:', font=('Arial', 30), fg='white', bg='#323232')
captcha_label.grid(row=4, column=0, pady=10, padx=10, sticky=tk.W)
captcha_entry = tk.Entry(root, width=20, font=('Arial', 30), fg='white', bg='#323232', highlightbackground='#c8c8c8')
captcha_entry.grid(row=4, column=1, pady=10, padx=10, sticky=tk.W)
captcha_text = tk.Label(root, text='----', bg='#323232', fg='white', font=('Arial', 30))
captcha_text.grid(row=4, column=2, pady=10, padx=10, sticky=tk.W)

login_btn = tk.Button(root, text='登录', font=('Arial', 30), fg='black', bg='#323232', command=login)
login_btn.grid(row=5, column=0, pady=10, padx=10, columnspan=1000, sticky=tk.EW)

tip_label = tk.Label(root, text='等待中...', fg='white', bg='#323232', font=('Arial', 30))
tip_label.grid(row=6, column=0, pady=10, padx=10, sticky=tk.W)

captcha = ''
for _ in range(4):
    captcha += choice(texts)
captcha_text.config(text=captcha)

root.focus_force()
root.mainloop()
