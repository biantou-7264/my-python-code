import tkinter as tk


def goyes():
    yes.config(state='disabled', bg='lightgray')
    no.config(state='disabled', bg='lightgray')
    root.configure(cursor='wait')
    root.after(5000, yes2)


def yes2():
    root.withdraw()
    fat = tk.Toplevel(root)
    fatlabel = tk.Label(fat, text='没错!', font=(None, 100))
    fatlabel.pack()
    fat.update()
    while True:
        fat.update()


def gono():
    yes.config(state='disabled', bg='lightgray')
    no.config(state='disabled', bg='lightgray')
    root.configure(cursor='wait')
    root.after(5000, no2)


def no2():
    yes.config(state='normal', bg='SystemButtonFace')
    no.config(state='normal', bg='SystemButtonFace')
    root.configure(cursor='arrow')
    error = tk.Toplevel(root)
    errortips = tk.Label(error, text='加载失败,请重试', font=(None, 50))
    errortips.pack()
    ok = tk.Button(error, text='关闭', command=error.destroy, font=(None, 30))
    ok.pack()


root = tk.Tk()
root.title('mumget')
title = tk.Label(root, text='你胖不胖', font=(None, 50))
title.pack()
yes = tk.Button(root, text='yes', command=goyes, font=(None, 30))
yes.pack()
no = tk.Button(root, text='no', command=gono, font=(None, 30))
no.pack()
root.mainloop()
