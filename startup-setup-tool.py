import tkinter as tk
import traceback, os, plistlib, psutil
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from time import sleep
import subprocess as sp

home: str = os.path.expanduser('~')
user_name: str = os.getenv('USER')
padx: int = 10
pady: int = 5


def install_daemon(plist_path: str) -> bool:
    sp.run(['launchctl', 'unload', '-w', plist_path], stderr=sp.DEVNULL, stdout=sp.DEVNULL)
    result = sp.run(['launchctl', 'load', '-w', plist_path], capture_output=True, text=True)

    if result.returncode == 0:
        label = os.path.basename(plist_path).replace('.plist', '')
        sp.run(['launchctl', 'start', label])
    else:
        return False

    return result.returncode == 0


def create() -> None:
    try:
        plist_dir: str = os.path.expanduser('~/Library/LaunchAgents')
        plist_path: str = os.path.join(plist_dir, '%s.plist' % com_name.get())
        plist_data: dict = {
            'Label': com_name.get(),
            'ProgramArguments': [app_path.get()],
            'RunAtLoad': True,
            'KeepAlive': keep_alive.get(),  # True = 自动重启  False = 不自动重启
            'ThrottleInterval': 5,  # 重启间隔(秒)
            'AbandonProcessGroup': True,  # 后台运行
            'ProcessType': 'Background' if background.get() else 'Standard',  # 后台进程类型
            'NSUIElement': True,  # 不显示程序坞图标（GUI应用）
            'StandardOutPath': stdout_path.get(),  # 输出
            'StandardErrorPath': stderr_path.get(),  # 错误
            'EnvironmentVariables': {
                'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin',
                'HOME': home,
            },
            'WorkingDirectory': work_path.get(),
        }
        with open(plist_path, 'wb') as f:
            plistlib.dump(plist_data, f)
        res: bool = install_daemon(plist_path)
        sleep(1)
        if res:
            mb.showinfo('提示', '成功添加')
    except Exception:
        print(traceback.format_exc())
        try:
            with open(os.path.expanduser('~/Library/Logs/com.biantou.startup_setup_tool.log'), 'w') as f:
                f.write(traceback.format_exc())
        except Exception:
            pass
        mb.showerror('错误', '代码报错了, 已保存报告')


def is_process_running(name: str) -> bool:
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False


class PathArgvLabel:
    def __init__(self, var: tk.StringVar, title: str):
        self.__var = var
        self.__title_label = tk.Label(root, text='%s (点击选择)' % title, font=('Arial', 20))
        self.__value_label = tk.Label(root, textvariable=self.__var, font=('Arial', 20))
        self.__title_label.bind('<Button-1>', self.__click)
        self.__value_label.bind('<Button-1>', self.__click)
        self.__title_label.pack(padx=padx, pady=pady)
        self.__value_label.pack(padx=padx, pady=pady)

    def __click(self, event) -> None:
        path = fd.askopenfilename(defaultextension='*.*', filetypes=[('All Files', '*.*')])
        if path:
            self.__var.set(path)


class TextArgvLabel:
    def __init__(self, var: tk.StringVar, title: str):
        self.__var = var
        self.__title_label = tk.Label(root, text='%s (点击选择)' % title, font=('Arial', 20))
        self.__value_label = tk.Label(root, textvariable=self.__var, font=('Arial', 20))
        self.__title_label.bind('<Button-1>', self.__click)
        self.__value_label.bind('<Button-1>', self.__click)
        self.__title_label.pack(padx=padx, pady=pady)
        self.__value_label.pack(padx=padx, pady=pady)

    def __click(self, event) -> None:
        text = sd.askstring('提示', '请输入文本')
        if text:
            self.__var.set(text)


class DirArgvLabel:
    def __init__(self, var: tk.StringVar, title: str):
        self.__var = var
        self.__title_label = tk.Label(root, text='%s (点击选择)' % title, font=('Arial', 20))
        self.__value_label = tk.Label(root, textvariable=self.__var, font=('Arial', 20))
        self.__title_label.bind('<Button-1>', self.__click)
        self.__value_label.bind('<Button-1>', self.__click)
        self.__title_label.pack(padx=padx, pady=pady)
        self.__value_label.pack(padx=padx, pady=pady)

    def __click(self, event) -> None:
        path = fd.askdirectory()
        if path:
            self.__var.set(path)


class BoolArgvLabel:
    def __init__(self, var: tk.BooleanVar, title: str):
        self.__var = var
        self.__title_label = tk.Label(root, text='%s (点击选择)' % title, font=('Arial', 20))
        self.__value_label = tk.Label(root, textvariable=self.__var, font=('Arial', 20))
        self.__title_label.bind('<Button-1>', self.__click)
        self.__value_label.bind('<Button-1>', self.__click)
        self.__title_label.pack(padx=padx, pady=pady)
        self.__value_label.pack(padx=padx, pady=pady)

    def __click(self, event) -> None:
        self.__var.set(not self.__var.get())


root = tk.Tk()
root.title('自启动设置工具')

app_path: tk.StringVar = tk.StringVar(value='None')
com_name: tk.StringVar = tk.StringVar(value='com.%s.xxx' % user_name)
work_path: tk.StringVar = tk.StringVar(value='/tmp')
keep_alive: tk.BooleanVar = tk.BooleanVar(value=True)
stdout_path: tk.StringVar = tk.StringVar(value='/dev/null')
stderr_path: tk.StringVar = tk.StringVar(value='/dev/null')
background: tk.BooleanVar = tk.BooleanVar(value=True)

PathArgvLabel(app_path, '可执行文件')
TextArgvLabel(com_name, '标志符')
DirArgvLabel(work_path, '工作目录')
BoolArgvLabel(keep_alive, '自动重启')
TextArgvLabel(stdout_path, 'stdout路径')
TextArgvLabel(stderr_path, 'stderr路径')
BoolArgvLabel(background, '后台运行')
tk.Button(root, text='立马生成', font=('Arial', 20), command=create).pack(padx=padx, pady=pady)

root.focus_force()
root.mainloop()
