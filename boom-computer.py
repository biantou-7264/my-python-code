import time
import multiprocessing as mp
from random import randint


def boom():
    ls = []
    while True:
        a = randint(1000000, 9999999)
        b = randint(1000000, 9999999)
        c = a ** b  # noqa
        for _ in range(1000):
            ls.append(c)


if __name__ == '__main__':
    print('欢迎使用卡电脑工具!')
    print('是否开始运行? [y/n]')

    answer = input('> ')
    if answer.lower() != 'y':
        print('你取消了运行')

    print('\033[33m程序将在5秒后运行\033[0m')
    for c in range(5, 0, -1):
        print('还有%d秒' % c)
        time.sleep(1)

    print('开始!')
    time.sleep(1)
    for id in range(500):
        mp.Process(target=boom, daemon=True).start()
        print('已启动进程%d号' % id)
    print('进程全部开始')
    time.sleep(9999999)
