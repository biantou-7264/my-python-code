import pyautogui as pag
from random import randint

w, h = pag.size()

print('===小游戏===')
print('1=开始\n其他=退出')
a = input('> ')
if a == '1':
    print('!你被骗啦!')
else:
    print('禁止退出')


while True:
    x, y = randint(0, w), randint(0, h)
    pag.moveTo(x, y)
