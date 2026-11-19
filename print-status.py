from pyperclip import copy

count: int = 0
user_input: str = ''
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while True:
    user_input = input('请输入最大数量: ')
    if user_input.isdigit():
        count = int(user_input)
        break
    else:
        print('请输入一个整数')

print('生成A1 B1 C1...Y1 Z1', end='')
for i in range(2, count + 1):
    print(' A%d B%d...Y%d Z%d' % (i, i, i, i), end='')
print('\n正在为您怒力生成...')

result = ''
for num in range(1, count + 1):
    for letter in LETTERS:
        result += '%s%d ' % (letter, num)
    if count > 1000:
        print('\r生成到: %d' % num, end='')
print('\n完成!')

print(result)
print('已复制到剪贴板')

copy(result)