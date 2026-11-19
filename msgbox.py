import tkinter as tk


def info(root, text='请输入文本', close='请输入文本'):
    msg = tk.Toplevel(root)
    tk.Label(msg, bitmap='info').pack(anchor=tk.NW, padx=20, pady=20)
    la = tk.Label(msg, text=text, font=(None, 20), justify='left')
    la.pack(anchor=tk.NW, padx=20)
    bu = tk.Button(msg, text=close, command=msg.destroy, font=(None, 20), cursor='pointinghand')
    bu.pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')


def warning(root, text='请输入文本', close='请输入文本'):
    msg = tk.Toplevel(root)
    tk.Label(msg, bitmap='warning').pack(anchor=tk.NW, padx=20, pady=20)
    la = tk.Label(msg, text=text, font=(None, 20), justify='left')
    la.pack(anchor=tk.NW, padx=20)
    bu = tk.Button(msg, text=close, command=msg.destroy, font=(None, 20), cursor='pointinghand')
    bu.pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')


def error(root, text='请输入文本', close='请输入文本'):
    msg = tk.Toplevel(root)
    tk.Label(msg, bitmap='error').pack(anchor=tk.NW, padx=20, pady=20)
    la = tk.Label(msg, text=text, font=(None, 20), justify='left')
    la.pack(anchor=tk.NW, padx=20)
    bu = tk.Button(msg, text=close, command=msg.destroy, font=(None, 20), cursor='pointinghand')
    bu.pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')


def question(root, text='请输入文本', close='请输入文本'):
    msg = tk.Toplevel(root)
    tk.Label(msg, bitmap='question').pack(anchor=tk.NW, padx=20, pady=20)
    la = tk.Label(msg, text=text, font=(None, 20), justify='left')
    la.pack(anchor=tk.NW, padx=20)
    bu = tk.Button(msg, text=close, command=msg.destroy, font=(None, 20), cursor='pointinghand')
    bu.pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')


def ask(root, text='请输入文本', yes='请输入文本', no='请输入文本'):
    msg = tk.Toplevel(root)
    msg.wait = True
    msg.res = None

    def y():
        msg.wait = False
        msg.res = True

    def n():
        msg.wait = False
        msg.res = False

    tk.Label(msg, bitmap='question').pack(anchor=tk.NW, padx=20, pady=20)
    la = tk.Label(msg, text=text, font=(None, 20), justify='left')
    la.pack(anchor=tk.NW, padx=20)
    nob = tk.Button(msg, text=no, command=n, font=(None, 20), cursor='pointinghand')
    nob.pack(side=tk.BOTTOM, pady=10)
    yeb = tk.Button(msg, text=yes, command=y, font=(None, 20), cursor='pointinghand')
    yeb.pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')
    while True:
        msg.update()
        if not msg.wait:
            break
    msg.destroy()
    return msg.res


if __name__ == '__main__':
    def test1(e):
        info(root, '程序运行成功!', '关闭')


    def test2(e):
        warning(root, '输入错误', '关闭')


    def test3(e):
        error(root, '程序已崩溃\nWeightError:So fat!', '关闭')


    def test4(e):
        question(root, '你胖不胖', '关闭')


    def test5(e):
        print(ask(root, '你胖不胖', '胖', '不胖'))


    root = tk.Tk()
    root.bind('<Key-1>', test1)
    root.bind('<Key-2>', test2)
    root.bind('<Key-3>', test3)
    root.bind('<Key-4>', test4)
    root.bind('<Key-5>', test5)
    root.mainloop()
