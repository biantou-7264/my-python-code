import tkinter as tk
from random import randint
from tkinter import scrolledtext as st
from tkinter import ttk
from threading import Thread, Lock
import requests as rq
from traceback import format_exc
import os

scaned_port = []
logs = []
threads = 0
threads_lock = Lock()
scaned_port_lock = Lock()
logs_lock = Lock()


def scan(start, end):
    global threads
    threads_lock.acquire()
    threads += 1
    threads_lock.release()
    for port in range(start, end):
        logs_lock.acquire()
        logs.append('扫描端口%d' % port)
        print('scaned port %s' % port)
        logs_lock.release()
        try:
            rq.get('%s:%d' % (host.get(), port), timeout=60)
            scaned_port_lock.acquire()
            scaned_port.append(str(port))
            scaned_port_lock.release()
        except Exception:
            pass
    threads_lock.acquire()
    threads -= 1
    threads_lock.release()


def start():
    scaned_port.clear()
    logs.clear()
    a = start_port.get()
    jiange = 2000
    while True:
        print('thread created!')
        if a + jiange > end_port.get():
            Thread(target=scan, args=(a, end_port.get())).start()
            break
        else:
            Thread(target=scan, args=(a, a + jiange)).start()
        a += jiange


def update():
    try:
        if threads > 0:
            start_btn.config(state=tk.DISABLED)
        else:
            start_btn.config(state=tk.NORMAL)
        threads_label.config(text='线程数: %d' % threads)
        if len(scaned_port) > 20:
            result.set('扫到端口太多, 将保存到桌面')
            if randint(0, 5) == 0:
                with open(os.path.expanduser('~/Desktop/扫端口结果.txt'), 'w') as f:
                    f.write(', '.join(scaned_port))
        else:
            result.set(', '.join(scaned_port))
        log.delete('1.0', tk.END)
        for l in logs:
            log.insert(tk.END, l + '\n')
        log.see(tk.END)
        ports_count = end_port.get() - start_port.get()
        scaned_ports_count = len(logs)
        progess = (scaned_ports_count / ports_count) * 100
        progess_bar['value'] = progess
    except Exception:
        print(format_exc())
    root.update()
    root.after(200, update)


root = tk.Tk()
root.title('端口扫描器')

host = tk.StringVar(value='127.0.0.1')
start_port = tk.IntVar(value=1024)
end_port = tk.IntVar(value=65535)
result = tk.StringVar(value='')

tk.Label(root, text='端口扫描器', font=('Arial', 20)).pack(padx=20, pady=10)
host_frame = tk.Frame(root)
tk.Label(host_frame, text='host:', font=('Arial', 10)).pack(padx=20, pady=10, side=tk.LEFT)
tk.Entry(host_frame, textvariable=host, font=('Arial', 10), highlightbackground='white').pack(padx=20, pady=10, fill=tk.X, side=tk.LEFT)
host_frame.pack(padx=20, pady=10)
start_port_frame = tk.Frame(root)
tk.Label(start_port_frame, text='start port:', font=('Arial', 10)).pack(padx=20, pady=10, side=tk.LEFT)
tk.Entry(start_port_frame, textvariable=start_port, font=('Arial', 10), highlightbackground='white').pack(padx=20, pady=10, fill=tk.X, side=tk.LEFT)
start_port_frame.pack(padx=20, pady=10)
end_port_frame = tk.Frame(root)
tk.Label(end_port_frame, text='end port:', font=('Arial', 10)).pack(padx=20, pady=10, side=tk.LEFT)
tk.Entry(end_port_frame, textvariable=end_port, font=('Arial', 10), highlightbackground='white').pack(padx=20, pady=10, fill=tk.X, side=tk.LEFT)
end_port_frame.pack(padx=20, pady=10)
threads_label = tk.Label(root, text='线程数: ??', font=('Arial', 10))
threads_label.pack(padx=20, pady=10)
start_btn = tk.Button(root, text='开始', font=('Arial', 10), command=start)
start_btn.pack(padx=20, pady=10, fill=tk.X)
log = st.ScrolledText(root, wrap=tk.NONE, font=('Arial', 10), highlightbackground='white', width=50, height=20)
log.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
progess_bar = ttk.Progressbar(root, length=200, mode='determinate', maximum=100, orient=tk.HORIZONTAL)
progess_bar.pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=result, font=('Arial', 15)).pack(padx=20, pady=10)

root.after(100, update)
root.focus_force()
root.mainloop()