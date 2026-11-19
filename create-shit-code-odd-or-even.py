max_num = 10000000
name = '1-%d-odd-or-even.py' % max_num

try:
    print('开始生成文件...')
    with open(name, 'w') as file:
        file.write(f"n = int(input('输入1-{max_num}数字:'))\n")
    with open(name, 'a') as file:
        for i in range(1, max_num + 1):
            file.write('if n == %d:' % i)
            if i % 2 == 0:
                file.write("print('偶数')\n")
            else:
                file.write("print('奇数')\n")
            print('\r%.2f%%' % (i / max_num * 100), end='')
    print('\n文件生成成功!')
except Exception as e:
    print(type(e).__name__)
    print(e)
print('文件生成结束')