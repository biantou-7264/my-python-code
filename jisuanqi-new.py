import tkinter as tk

root = tk.Tk()
root.title('计算器')
root.geometry('270x360')

ok = False


def entry(c):
    global result, ok
    get = str(result.get())

    if get == '0':
        result.set(c)
    elif ok and str(c).isdigit():
        result.set(c)
    else:
        result.set(get + str(c))

    ok = False


def back():
    global result
    get = str(result.get())
    l = len(get)

    if l > 1:
        result.set(get[:-1])
    else:
        result.set('0')


def clear():
    global result
    result.set(0)


def pn():
    global result
    try:
        get = int(result.get())
    except ValueError:
        return
    except BaseException as e:
        print(type(e).__name__)
        print(e)
        return
    result.set(get * -1)


def eq():
    global result, ok
    try:
        get = result.get()
        result.set(eval(get))
    except SyntaxError:
        result.set('表达式错误')
    except ZeroDivisionError:
        result.set('不能除以0')
    except BaseException as e:
        print(type(e).__name__)
        print(e)
    ok = True


def crbtn(text, row, col):
    tk.Button(frame, text=str(text), font=(None, 40), command=lambda: entry(str(text)), cursor='pointinghand').grid(row=row, column=col, sticky='nesw')


def crbkbtn(row, col):
    tk.Button(frame, text='<-', font=(None, 40), command=back, cursor='pointinghand').grid(row=row, column=col, sticky='nesw')


def crclbtn(row, col):
    tk.Button(frame, text='C', font=(None, 40), command=clear, cursor='pointinghand').grid(row=row, column=col, sticky='nesw')


def crpnbtn(row, col):
    tk.Button(frame, text='±', font=(None, 40), command=pn, cursor='pointinghand').grid(row=row, column=col, sticky='nesw')


def creqbtn(row, col):
    tk.Button(frame, text='=', font=(None, 40), command=eq, cursor='pointinghand').grid(row=row, column=col, sticky='nesw')


result = tk.StringVar()
result.set('0')

lab = tk.Label(root, textvariable=result, bg='#ffc800', fg='#323232', font=(None, 40), justify=tk.RIGHT, anchor=tk.E)
lab.pack(fill=tk.X)
frame = tk.Frame(root, bg='#323232')
frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

crclbtn(0, 0)
crbkbtn(0, 1)
crpnbtn(0, 2)
crbtn(1, 1, 0)
crbtn(2, 1, 1)
crbtn(3, 1, 2)
crbtn(4, 2, 0)
crbtn(5, 2, 1)
crbtn(6, 2, 2)
crbtn(7, 3, 0)
crbtn(8, 3, 1)
crbtn(9, 3, 2)
crbtn(0, 4, 0)
crbtn('00', 4, 1)
crbtn('/', 0, 3)
crbtn('*', 1, 3)
crbtn('-', 2, 3)
crbtn('+', 3, 3)
crbtn('.', 4, 2)
creqbtn(4, 3)

root.mainloop()
