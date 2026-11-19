import keyboard
from time import sleep
from random import choice
sleep(2)
try:
    texts=list('asdfghjklqwertyuiopzxcvbnm1234567890')
    length=len(texts)
    while True:
        keyboard.write(choice(texts))
        sleep(0.02)
except KeyboardInterrupt:
    print('程序已退出')
except Exception as e:
    print(e)
