import pyautogui as pag
from pyperclip import copy

print('===给AI报数===')

print('请输入最小值(包含):')
while True:
    try:
        min_num = int(input('> '))
        break
    except ValueError:
        print('请输入整数')

print('请输入最大值(包含):')
while True:
    try:
        max_num = int(input('> '))
        break
    except ValueError:
        print('请输入整数')

print('请输入步长:')
while True:
    try:
        step = int(input('> '))
        break
    except ValueError:
        print('请输入整数')

print('请将DeepSeek窗口切换填充模式!')

print('')
for i in range(5, 0, -1):
    print(i)
    pag.sleep(1)
print('\n==> 开始')

for i in range(min_num, max_num, step):
    copy(str(i))
    pag.hotkey('command', 'v')
    pag.write('\n')
    print('\n==已发送:%d' % i)
    print('==> 等待DeepSeek回复...')
    while True:
        try:
            pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/frameworks/dpsk可发送按钮.png')
            break
        except pag.ImageNotFoundException:
            pass
        pag.sleep(0.1)
    print('--即将继续')
    pag.sleep(0.1)

print('===结束===')
