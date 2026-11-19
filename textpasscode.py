from pyperclip import copy
from os import getpid
import psutil

pid = getpid()
process = psutil.Process(pid)
print('加密=1\n解密=2')
mode = input('输入模式:')
if mode == '1':
    text = input('输入内容:')
    result = '|'
    textlen = len(text)
    jindu1 = 0
    for i in text:
        mem = process.memory_info().rss
        totalmem = psutil.virtual_memory().total
        memp = (mem / totalmem) * 100
        count = ord(i)
        jindu = (jindu1 / textlen) * 100
        print('\r已完成百分之%.5f,占用内存百分之%.2f' % (jindu, memp), end='', flush=True)
        jindu1 += 1
        for i in range(count):
            result = result + '​'
        result = result + '‌'
        jindu = (jindu1 / textlen) * 100
        print('\r已完成百分之%.5f,占用内存百分之%.2f' % (jindu, memp), end='', flush=True)
    result = result + '|'
    copy(result)
    print('')
elif mode == '2':
    code = input('输入内容:')
    step1 = code.replace('|', '')
    step2 = step1.split('‌')
    codelen = len(step2)
    result = ''
    jindu1 = 0
    for i in step2:
        jindu = (jindu1 / codelen) * 100
        print('\r已完成百分之%.5f' % jindu, end='', flush=True)
        jindu1 += 1
        count = len(i)
        if count != 0:
            char = chr(count)
            result = result + char
        jindu = (jindu1 / codelen) * 100
        print('\r已完成百分之%.5f' % jindu, end='', flush=True)
    print('')
else:
    result = '无效选择'
print(result, flush=True)
