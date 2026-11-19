import multiprocessing as mp
import os, shutil, psutil
from time import sleep
import subprocess as sp

MB = 1000 * 1000
size: int = MB * 100  # 100MB


def boom():
    pid: int = os.getpid()
    print('我是PID为%d的进程, 我开始占空间了' % pid)
    try:
        with open('/Users/Shared/.bigfile', 'ab') as f:
            f.write(os.urandom(size))
    except Exception:
        print('我是%d, 我报错退出了' % pid)
        return 1
    print('我是PID%d, 我正常退出了' % pid)
    return 0


if __name__ == '__main__':
    print('欢迎使用占空间程序')
    print('本程序将把你的硬盘吃满')
    print('请输入停止阀值(MB)')
    while True:
        a: str = input('> ')
        if a.isdigit():
            min_size: int = int(a)
            break
    while True:
        _, _, free = shutil.disk_usage('/')
        if free / MB < min_size:
            break
        process = mp.Process(target=boom)
        process.start()
        cpu = psutil.cpu_percent(interval=0.3)
        if cpu > 90:
            print('CPU% > 90, 触发保护, 将在2秒后继续创建进程')
            sleep(2)
    sleep(1)
    print('已结束')
    _, _, free = shutil.disk_usage('/')
    print('您的磁盘还剩: %dMB' % (free / MB))
    sp.run(['killall', 'Python'])
    print('已为您清理进程')
