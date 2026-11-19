# 这个是自动打monkey-type的程序

import pyautogui as pag

pag.PAUSE = 0.01

print('欢迎使用monkey-type作弊程序 ^_^')
text = input('-- 请输入打字内容 (输入*--*读文件): ')
if text == '*--*':
    text = open('monkey-type-file.txt').read()

print('# 请在3秒内切换到网页!')
pag.sleep(3)
print('-> 开始!')

for t in text:
    pag.write(t)
    print('-> 输入: %s' % t)

print('* 打完了!')
