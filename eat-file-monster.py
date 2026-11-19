import os
import shutil
from time import sleep
import tkinter as tk

monster_path = '/Users/luojingfeng/Desktop/吃文件的怪物'
interval = 4
root = tk.Tk()
root.iconify()

try:
    print('\033[34m===吃文件的怪物===\033[0m')
    print('\033[35m怪物位置: %s' % monster_path)
    print('\033[35m检测间隔: %d 秒' % interval)

    print('\n\033[32m==>怪物已启动!\033[0m\n')
    while True:
        root.update()
        root.iconify()
        print('\033[33m==>怪物检测了一次\033[0m')
        print('\033[34m检测到了\033[31m%d\033[34m个文件/目录\033[0m\n' % len(os.listdir(monster_path)))
        if len(os.listdir(monster_path)) > 0:
            for i in os.listdir(monster_path):
                try:
                    if os.path.isdir(os.path.join(monster_path, i)):
                        shutil.rmtree(os.path.join(monster_path, i))
                    else:
                        os.remove(os.path.join(monster_path, i))
                    print('\033[35m==>怪物吃掉了\033[31m%s\033[0m' % i)
                except Exception as e:
                    print('\033[31m===发生错误===')
                    print(type(e).__name__)
                    print(e)
                    print('==============\033[0m')
            print('\n\033[32m√已经吃完了\033[0m')
        else:
            print('\033[35m ==>这次跳过\033[0m\n')
        for _ in range(interval * 2):
            root.update()
            root.iconify()
            sleep(0.5)
except KeyboardInterrupt:
    print('\n\033[35m===程序退出===\033[0m')
except FileNotFoundError as e:
    print('\n\033[31m===发生错误===')
    print(type(e).__name__)
    print(e)
    print('请检查怪物位置')
    print('==============\033[0m')
    print('\n\033[35m===程序退出===\033[0m')
except TypeError as e:
    print('\n\033[31m===发生错误===')
    print(type(e).__name__)
    print(e)
    print('请检查变量类型')
    print('怪物位置必须是一个字符串')
    print('间隔必须是一个整数')
    print('==============\033[0m')
    print('\n\033[35m===程序退出===\033[0m')
except BaseException as e:
    print('\n\033[31m===发生错误===')
    print(type(e).__name__)
    print(e)
    print('==============\033[0m')
    print('\n\033[35m===程序退出===\033[0m')
