import tkinter as tk
from tkinter import messagebox, simpledialog
from math import *

msgbox = messagebox
smldig = simpledialog
root = tk.Tk()
m = 0
result = 0


def update():
    global result
    a = len(str(result))
    notsize = False
    if a >= 20:
        r = result[0:a - 1]
        result = r
        label.config(text=result)
        notsize = True
    label.config(text=result)
    if a >= 14 and not notsize:
        b = 30 - ((a - 14) * 2)
        label.config(font=(None, b))


def goone(debug=0):
    global result
    a = 1
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gotwo(debug=0):
    global result
    a = 2
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gothree(debug=0):
    global result
    a = 3
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gofour(debug=0):
    global result
    a = 4
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gofive(debug=0):
    global result
    a = 5
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gosix(debug=0):
    global result
    a = 6
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def goseven(debug=0):
    global result
    a = 7
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def goeight(debug=0):
    global result
    a = 8
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gonine(debug=0):
    global result
    a = 9
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gozero(debug=0):
    global result
    a = 0
    if str(result) == '0':
        result = '​0'
    else:
        result = str(result) + str(a)
    update()


def godot(debug=0):
    global result
    a = '.'
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def goc(debug=0):
    global result
    result = 0
    update()


def goback(debug=0):
    global result
    if str(result) != '0':
        a = str(result)[:-1]
        result = a
    if len(str(result)) == 0:
        result = 0
    if result == '-':
        result = 0
    update()


def gosign(debug=0):
    try:
        global result
        result = str(int(result) * -1)
        update()
    except:
        pass


def gomc(debug=0):
    global m
    m = 0


def gomr(debug=0):
    global result
    result = m
    update()


def gomp(debug=0):
    global m
    try:
        m += int(result)
    except:
        pass


def gomm(debug=0):
    global m
    try:
        m -= int(result)
    except:
        pass


def govid(debug=0):
    global result
    a = '/'
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gotimes(debug=0):
    global result
    a = '*'
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def gominu(debug=0):
    global result
    a = '-'
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def goplus(debug=0):
    global result
    a = '+'
    if str(result) == '0':
        result = a
    else:
        result = str(result) + str(a)
    update()


def goequal(debug=0):
    global result
    a = str(result)
    result = a.lstrip('​')
    try:
        result = eval(result)
    except ZeroDivisionError as e:
        result = '错误:不能除以0'
        print(e)
    except MemoryError as e:
        goequal()
        print(e)
    except TypeError as e:
        result = result
    except SyntaxError as e:
        if '错误' in result:
            result = '错误:请清零后计算'
        else:
            result = '错误:输入值无效'
    except ValueError as e:
        if '错误' in result:
            result = '错误:请清零后计算'
        else:
            result = '错误:输入值无效'
    except NameError as e:
        if '错误' in result:
            result = '错误:请清零后计算'
        else:
            result = '错误:输入值无效'
    except BaseException as e:
        result = '错误:未知错误'
    update()


def safequit(debug=0):
    root.destroy()


def reset(debug=0):
    goc()
    gomc()
    update()
    root.focus_force()


def enter():
    uip = smldig.askstring('自定义输入', '请输入内容,覆盖原内容,支持数学函数')
    if uip is None:
        pass
    else:
        try:
            ban = ['import', 'os', 'remove', 'system', '系统', '__import__', 'subprocess', 'requests', 'open', 'file']
            for i in ban:
                if str(i).lower() in str(uip).lower():
                    raise ValueError('222')
            global result
            result = uip
            update()
        except:
            warenter()


def warenter():
    uip = smldig.askstring('自定义输入', '输入内容包含危险内容,请重新输入')
    if uip is None:
        pass
    else:
        try:
            ban = ['import', 'os', 'remove', 'system', '系统', '__import__', 'subprocess', 'requests', 'open', 'file', ':', 'HD', '\\']
            for i in ban:
                if str(i).lower() in str(uip).lower():
                    raise ValueError('222')
            global result
            result = uip
            update()
        except:
            warenter()


root.title('计算器')
size = '260x288'
root.geometry(size)
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", safequit)
root.bind('<Escape>', safequit)
root.bind('<Key-1>', goone)
root.bind('<Key-2>', gotwo)
root.bind('<Key-3>', gothree)
root.bind('<Key-4>', gofour)
root.bind('<Key-5>', gofive)
root.bind('<Key-6>', gosix)
root.bind('<Key-7>', goseven)
root.bind('<Key-8>', goeight)
root.bind('<Key-9>', gonine)
root.bind('<Key-0>', gozero)
root.bind('+', goplus)
root.bind('-', gominu)
root.bind('*', gotimes)
root.bind('/', govid)
root.bind('=', goequal)
root.bind('<Return>', goequal)
root.bind('<BackSpace>', goback)
root.bind('c', goc)
root.bind('C', goc)
root.bind('.', godot)
root.bind('<period>', godot)
root.bind('p', gosign)
root.bind('n', gosign)
root.bind('P', gosign)
root.bind('N', gosign)
root.bind('r', reset)
root.bind('R', reset)
root.bind('<F5>', reset)
try:
    root.bind('<Command-C>', gomc)
    root.bind('<Command-R>', gomr)
    root.bind('<Command-c>', gomc)
    root.bind('<Command-r>', gomr)
    root.bind('<Command-plus>', gomp)
    root.bind('<Command-equal>', gomp)
    root.bind('<Command-KP_Add>', gomp)
    root.bind('<Command-minus>', gomm)
    root.bind('<Command-underscore>', gomm)
    root.bind('<Command-KP_Subtract>', gomm)
except:
    pass
root.bind('<Control-C>', gomc)
root.bind('<Control-R>', gomr)
root.bind('<Control-c>', gomc)
root.bind('<Control-r>', gomr)
root.bind('<Control-plus>', gomp)
root.bind('<Control-equal>', gomp)
root.bind('<Control-KP_Add>', gomp)
root.bind('<Control-minus>', gomm)
root.bind('<Control-underscore>', gomm)
root.bind('<Control-KP_Subtract>', gomm)
label = tk.Label(root, text=result, font=(None, 30))
label.grid(row=0, column=0, sticky='w', columnspan=1000)
mc = tk.Button(root, text='MC', command=gomc, font=(None, 20))
mc.grid(row=1, column=0, sticky='nesw')
mr = tk.Button(root, text='MR', command=gomr, font=(None, 20))
mr.grid(row=1, column=1, sticky='nesw')
mp = tk.Button(root, text='M+', command=gomp, font=(None, 20))
mp.grid(row=1, column=2, sticky='nesw')
mm = tk.Button(root, text='M-', command=gomm, font=(None, 20))
mm.grid(row=1, column=3, sticky='nesw')
c = tk.Button(root, text='C', command=goc, font=(None, 20))
c.grid(row=2, column=0, sticky='nesw')
back = tk.Button(root, text='←', command=goback, font=(None, 20))
back.grid(row=2, column=1, sticky='nesw')
sign = tk.Button(root, text='±', command=gosign, font=(None, 20))
sign.grid(row=2, column=2, sticky='nesw')
div = tk.Button(root, text='/', command=govid, font=(None, 20))
div.grid(row=2, column=3, sticky='nesw')
one = tk.Button(root, text='1', command=goone, font=(None, 20))
one.grid(row=3, column=0, sticky='nesw')
two = tk.Button(root, text='2', command=gotwo, font=(None, 20))
two.grid(row=3, column=1, sticky='nesw')
three = tk.Button(root, text='3', command=gothree, font=(None, 20))
three.grid(row=3, column=2, sticky='nesw')
times = tk.Button(root, text='*', command=gotimes, font=(None, 20))
times.grid(row=3, column=3, sticky='nesw')
four = tk.Button(root, text='4', command=gofour, font=(None, 20))
four.grid(row=4, column=0, sticky='nesw')
five = tk.Button(root, text='5', command=gofive, font=(None, 20))
five.grid(row=4, column=1, sticky='nesw')
six = tk.Button(root, text='6', command=gosix, font=(None, 20))
six.grid(row=4, column=2, sticky='nesw')
minu = tk.Button(root, text='-', command=gominu, font=(None, 20))
minu.grid(row=4, column=3, sticky='nesw')
seven = tk.Button(root, text='7', command=goseven, font=(None, 20))
seven.grid(row=5, column=0, sticky='nesw')
eight = tk.Button(root, text='8', command=goeight, font=(None, 20))
eight.grid(row=5, column=1, sticky='nesw')
nine = tk.Button(root, text='9', command=gonine, font=(None, 20))
nine.grid(row=5, column=2, sticky='nesw')
plus = tk.Button(root, text='+', command=goplus, font=(None, 20))
plus.grid(row=5, column=3, sticky='nesw')
zero = tk.Button(root, text='0', command=gozero, font=(None, 20))
zero.grid(row=6, column=0, columnspan=2, sticky='nesw')
dot = tk.Button(root, text='.', command=godot, font=(None, 20))
dot.grid(row=6, column=2, sticky='nesw')
equal = tk.Button(root, text='=', command=goequal, font=(None, 20))
equal.grid(row=6, column=3, sticky='nesw')
re = tk.Button(root, text='重置', command=reset)
re.grid(row=7, column=0, columnspan=2, sticky='nesww')
edit = tk.Button(root, text='输入', command=enter)
edit.grid(row=7, column=2, columnspan=2, sticky='nesww')
root.focus_force()
root.mainloop()
