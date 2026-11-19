import tkinter as tk
from threading import Thread
import sys
from tkinter import scrolledtext as st
import subprocess as sp
from tkinter import messagebox as mb


class Edit:
    def __init__(self):
        self.window = tk.Toplevel(root)
        self.window.title('代码测试器')
        self.window.focus_force()
        self.text_area = st.ScrolledText(self.window, width=70, height=30, font=('Arial', 15))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, '# 在这里写下你的代码')
        self.run_btn = tk.Button(self.window, text='运行 [F5]', font=('Arial', 20), command=self.run)
        self.run_btn.pack(fill=tk.X, expand=True, padx=5, pady=5)
        self.window.bind('<F5>', self.run)

    def run(self, *args):
        text = self.text_area.get('1.0', tk.END)
        try:
            with open('/tmp/code-test.py', 'w') as file:
                file.write(text)
        except Exception as e:
            mb.showerror(type(e).__name__, str(e))
        runner = Runner()
        runner.run('/tmp/code-test.py')


class Runner:
    def __init__(self):
        self.window = tk.Toplevel(root)
        self.window.title('运行结果')
        self.window.focus_force()
        self.text_area = st.ScrolledText(self.window, width=70, height=30, font=('Arial', 15))
        self.text_area.pack(fill=tk.BOTH, expand=True)

    def run(self, file):
        Thread(target=self.run_task, args=(file,), daemon=True).start()

    def run_task(self, file):
        thread = sp.Popen([sys.executable, file], stdout=sp.PIPE, stderr=sp.STDOUT, text=True)
        for line in thread.stdout:
            self.stdout(line)
        thread.wait()
        self.stdout('\n------------------\n退出代码: %d' % thread.returncode)

    def stdout(self, text):
        self.text_area.insert(tk.END, text)


root = tk.Tk()
root.withdraw()

Edit()

root.mainloop()
