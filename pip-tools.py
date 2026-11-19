from subprocess import run
import tkinter as tk
from tkinter import scrolledtext
import threading, sys, wifi


def stdout(text):
    current_position = text_area.yview()
    text_area.insert(tk.END, f"\n{text}")
    if current_position[1] >= 0.99:
        text_area.see(tk.END)
    root.update()


def install():
    if not wifi.test():
        name = input_module.get()
        stdout('断网了,无法安装%s' % name)
        return

    def task():
        global input_module, jindu, name
        name = input_module.get()
        stdout('开始安装%s' % name)
        try:
            run([sys.executable, '-m', 'pip', 'install', name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '3'], check=True)
        except:
            stdout('安装%s时出现错误' % name)
        else:
            stdout('%s安装完成!' % name)

    threading.Thread(target=task).start()


import time

uninsall_presstime = time.time()


def uninstall():
    global input_module, uninsall_presstime
    if time.time() - uninsall_presstime < 2:
        yes_uninstall()
    else:
        name = input_module.get()
        stdout('即将卸载%s' % name)
        stdout('再点一下卸载确定卸载')
        uninsall_presstime = time.time()


def yes_uninstall():
    def task():
        global input_module, jindu, name
        name = input_module.get()
        stdout('开始卸载%s' % name)
        try:
            run([sys.executable, '-m', 'pip', 'uninstall', name, '-y'], check=True)
        except:
            stdout('卸载%s时出现错误' % name)
        else:
            stdout('%s卸载完成!' % name)

    threading.Thread(target=task).start()


def upgrade():
    if not wifi.test():
        name = input_module.get()
        stdout('断网了,无法更新%s' % name)
        return

    def task():
        global input_module, jindu, name
        name = input_module.get()
        stdout('开始更新%s' % name)
        try:
            run([sys.executable, '-m', 'pip', 'install', '--upgrade', name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '3'], check=True)
        except:
            stdout('更新%s时出现错误' % name)
        else:
            stdout('%s更新完成!' % name)

    threading.Thread(target=task).start()


def update_pip():
    if not wifi.test():
        name = 'pip'
        stdout('断网了,无法更新%s' % name)
        return

    def task():
        global input_module, jindu, name
        name = 'pip'
        stdout('开始更新%s' % name)
        try:
            run([sys.executable, '-m', 'pip', 'install', '--upgrade', name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '3'], check=True)
        except:
            stdout('更新%s时出现错误' % name)
        else:
            stdout('%s更新完成!' % name)

    threading.Thread(target=task).start()


def list_module():
    def task():
        stdout('开始列出所有库')
        try:
            result = run([sys.executable, '-m', 'pip', 'list'], check=True, capture_output=True, text=True)
        except:
            stdout('列出所有库时出现错误')
        else:
            stdout(result.stdout)

    threading.Thread(target=task).start()


root = tk.Tk()
root.title('pip小工具')
root.geometry('600x500')
text_area = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=75, height=20, font=(None, 10))
text_area.pack(padx=10, pady=10)
module_name = 0
input_tips = tk.Label(root, text='请在下方的输入框输入库名称')
input_tips.pack(pady=10)
input_module = tk.Entry(root, width=60)
input_module.pack()
install_button = tk.Button(root, text='现在安装!', command=install)
install_button.pack()
uninstall_button = tk.Button(root, text='卸载', command=uninstall)
uninstall_button.pack()
upgrade_button = tk.Button(root, text='更新到最新!', command=upgrade)
upgrade_button.pack()
update_pip_button = tk.Button(root, text='更新pip到最新!', command=update_pip)
update_pip_button.pack()
list_button = tk.Button(root, text='列出已安装的库', command=list_module)
list_button.pack()
root.mainloop()
