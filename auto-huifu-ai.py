import sys
import pyautogui as pag
from random import choice
from pyperclip import copy

says = ['你好', '很高兴认识你', '一加一等于几', '你是谁', '你叫什么', '什么情况下5*5=55555', '今天几月几日', '世界上最胖的人是谁', '谢谢你!', '哈哈哈哈哈哈哈', '讲个笑话', '夸夸我', '帮我用python写一个可以画正方形的程序', '你是机器人吗', '你会c++吗', '379297472 + 3897979249 * 479892739等于几']
is_exit = False
count = 0
huifus = []


def hotkey(*command):
    new_command = []
    for c in command:
        pag.keyDown(c)
        new_command.insert(0, c)
    for c in new_command:
        pag.keyUp(c)


def exit_report():
    print('\n\033[35m==>结束\033[0m\n\033[33m===报告单===\033[0m')
    print('已经发了\033[31m%d\033[0m句' % count)
    print('总共发送了这些:')
    for c, i in enumerate(huifus):
        print('\033[31m%d\033[0m   \033[32m%s\033[0m' % (c + 1, i))
    print('\033[33m=============\033[0m')
    print('\n\033[34m===程序退出===\033[0m')


print('\033[34m===给AI自动发消息===\033[0m')
print('\n\033[35m==> 请切换到DeepSeek\033[0m')

try:
    print('\033[31m')
    for i in range(5, 0, -1):
        print(i)
        pag.sleep(1)
    print('\033[0m')
    print('\n\033[32m==> 开始\033[0m')
except KeyboardInterrupt:
    is_exit = True
except Exception as e:
    print('\n\033[31m===发生错误===')
    print(type(e).__name__)
    print(e)
    print('\033[0m')
    is_exit = True

if is_exit:
    exit_report()
    sys.exit()

print('-先说\033[31m“你好”\033[0m')
copy('你好')
hotkey('command', 'v')
pag.write('\n')
count += 1
huifus.append('你好')
while True:
    try:
        pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/frameworks/dpsk可发送按钮.png')
        break
    except pag.ImageNotFoundException:
        pass
    except KeyboardInterrupt:
        is_exit = True
        break
    except Exception as e:
        print('\n\033[31m===发生错误===')
        print(type(e).__name__)
        print(e)
        print('\033[0m')
        is_exit = True
        break
    pag.sleep(0.1)

try:
    while True:
        if is_exit:
            break
        say = choice(says)
        copy(say)
        hotkey('command', 'v')
        pag.write('\n')
        count += 1
        huifus.append(say)
        print('==>已经发送\033[31m“%s”\033[0m\n\033[34m-等待AI回复\033[0m' % say)
        while True:
            try:
                pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/frameworks/dpsk可发送按钮.png')
                break
            except pag.ImageNotFoundException:
                pass
            except KeyboardInterrupt:
                is_exit = True
                break
            pag.sleep(0.1)
        if is_exit:
            break
        print('\033[32m==>继续\033[0m')
        print('')
except KeyboardInterrupt:
    pass
except Exception as e:
    print('\n\033[31m===发生错误===\033[0m')
    print(e)

exit_report()
