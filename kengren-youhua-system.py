from time import sleep
import subprocess as sp

print('===一键清理系统垃圾===')
print('==>开始清理')

print('\n==>正在清理缓存文件...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在询问电脑今天心情...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在调节性能至最佳状态...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在清理无用日志...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在教育电脑...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在教电脑做人...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n==>正在鼓励电脑...')
print('进度: ', end='')
for _ in range(30):
    print('#', end='')
    sleep(0.1)

print('\n√完成\n\n^_^ 即将给你个大惊喜')
for i in range(3, 0, -1):
    print('\r%d' % i, end='')
    sleep(1)
print('\r^_^ 嘿嘿!')
sleep(0.5)
for _ in range(5):
    sp.run(['pmset', 'sleepnow'])
    sleep(3)
sleep(2)
volume = 100
sp.run('osascript -e "set volume output volume %d"' % volume, shell=True)
sp.run(['say', '-r', '200', '诺和忻司美格鲁肽片，原研好药，下单即送血糖仪套装，赠完即止，戳3.cn/v/pt7GYf'])