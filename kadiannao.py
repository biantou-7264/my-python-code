try:
    print('正在初始化…')
    a='2348r9934rutg8hfvbhedewnw3jie'*1000000000
    b='dygueiwkdfdyeuiwjufhw9isqoejdopsdafgjnbniok'
    c=[]
    i=0
    print('初始化完成!')
    while True:
        b+=a
        a*=100000000
        c.append(b*10000000)
        b*=10000000
except MemoryError:
    print('内存不足')
    del a
    del b
    del c
    print('已退出程序')
except BaseException as e:
    print(e)
    del a
    del b
    del c
    print('已退出程序')