import os
import subprocess as sp
import tkinter as tk
from threading import Thread
from time import sleep
from tkinter import scrolledtext as st
from traceback import format_exc

import aria2p

log = []
downloads_dir = os.path.expanduser('~/Downloads')
download = None
started = False
aria2 = None
os.environ['PATH'] = '/opt/homebrew/bin:' + os.environ['PATH']
os.environ['PATH'] = '/usr/local/bin:' + os.environ['PATH']


def start_rpc():
    global aria2
    try:
        print('正在启动rpc服务...')
        for _ in range(10):
            sp.run(['killall', 'aria2c'])
        sleep(1)
        sp.Popen(['aria2c', '--enable-rpc', '--rpc-listen-all=false', '--rpc-secret=123456'])
        aria2_client = aria2p.Client(
            host='http://localhost',
            port=6800,
            secret='123456'
        )
        aria2 = aria2p.API(aria2_client)
        sleep(1)
        version = aria2_client.get_version()['version']
        print('\033[32m成功启动rpc服务, aria2版本是%s\033[0m' % version)
    except Exception:
        print('\033[31m')
        print(format_exc())
        print('rpc服务启动失败\033[0m')


def start():
    global started, download
    started = True
    download = aria2.add_uris(
        [url.get()],
        options={
            'dir': downloads_dir,
            'split': str(split_num.get()),
            'max-connection-per-server': str(max_connect_num.get()),
            'continue': 'true',
            'min-split-size': '%dM' % split_size.get(),
            'allow-overwrite': 'true',
            'auto-file-renaming': 'false',
            'max-tries': '0',
            'retry-wait': '3',
            'summary-interval': '20',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    )


def format_size(byte):
    if byte >= 1024 * 1024:
        unit = 'MiB'
        num = byte / 1024 / 1024
    else:
        unit = 'KiB'
        num = byte / 1024
    return num, unit


def update():
    global started
    try:
        text.delete('1.0', tk.END)
        if download is None:
            text.insert(tk.END, '未开始下载')
        else:
            download.update()
            if download.status in ('complete', 'error', 'removed'):
                started = False
            if download.status == 'complete':
                text.insert(tk.END, '下载完成!')
            elif download.status == 'error':
                text.insert(tk.END, '下载失败\n')
                text.insert(tk.END, '错误码: %s\n' % download.error_code)
                text.insert(tk.END, '错误信息: %s\n' % download.error_message)
            else:
                text.insert(tk.END, 'GID: %s\n' % download.gid)
                text.insert(tk.END, '文件名: %s\n' % download.name)
                text.insert(tk.END, '状态: %s\n' % download.status)
                text.insert(tk.END, '进度: %s%%\n' % download.progress)
                num, unit = format_size(download.download_speed)
                text.insert(tk.END, '速度: %s%s\n' % (num, unit))
                text.insert(tk.END, '剩余时间: %s\n' % download.eta)
                num, unit = format_size(download.completed_length)
                text.insert(tk.END, '已下载大小: %s%s\n' % (num, unit))
                num, unit = format_size(download.total_length)
                text.insert(tk.END, '总共大小: %s%s\n' % (num, unit))
                text.insert(tk.END, '错误码: %s\n' % download.error_code)
                text.insert(tk.END, '错误信息: %s\n' % download.error_message)
        text.see(tk.END)
    except Exception:
        pass
    try:
        if started:
            start_btn.config(state=tk.DISABLED)
            stop_btn.config(state=tk.NORMAL)
        else:
            start_btn.config(state=tk.NORMAL)
            stop_btn.config(state=tk.DISABLED)
    except Exception:
        pass
    root.update()
    root.after(100, update)


def pause():
    if download is not None:
        download.pause()


def resume():
    if download is not None:
        download.resume()


def stop():
    global started
    if download is not None:
        download.remove()
        started = False


root = tk.Tk()
root.title('下载工具')

max_connect_num = tk.IntVar(value=16)
split_num = tk.IntVar(value=50)
split_size = tk.IntVar(value=10)
url = tk.StringVar(value='https://')

tk.Label(root, text='多线程下载工具', font=('Arial', 20)).pack()
tk.Label(root, text='使用aria2c, 速度更快, 支持断点续传', font=('Arial', 15)).pack()
tk.Entry(root, textvariable=url, font=('Arial', 15), highlightbackground='white').pack(fill=tk.X)
tk.Label(root, text='最大连接数(越大越快, 1-16):').pack(fill=tk.X)
tk.Entry(root, textvariable=max_connect_num, font=('Arial', 15), highlightbackground='white').pack(fill=tk.X)
tk.Label(root, text='分块数(越大越快, 1-∞):').pack(fill=tk.X)
tk.Entry(root, textvariable=split_num, font=('Arial', 15), highlightbackground='white').pack(fill=tk.X)
tk.Label(root, text='每块大小(MB, 1-1073):').pack(fill=tk.X)
tk.Entry(root, textvariable=split_size, font=('Arial', 15), highlightbackground='white').pack(fill=tk.X)
start_btn = tk.Button(root, text='开始', command=start, font=('Arial', 15))
start_btn.pack(fill=tk.X)
tk.Button(root, text='暂停', command=pause, font=('Arial', 15)).pack(fill=tk.X)
tk.Button(root, text='继续', command=resume, font=('Arial', 15)).pack(fill=tk.X)
stop_btn = tk.Button(root, text='停止', command=stop, font=('Arial', 15))
stop_btn.pack(fill=tk.X)

text = st.ScrolledText(root, font=('Arial', 15), wrap=tk.NONE, width=40, height=20, highlightbackground='white')
text.pack(fill=tk.BOTH, expand=True)

Thread(target=start_rpc, daemon=True).start()

root.after(20, update)
root.focus_force()
root.mainloop()