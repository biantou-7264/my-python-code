import tkinter as tk

root = tk.Tk()
root.title('mumget')


def gogogo():
    new = tk.Toplevel()
    new.title('胖')
    fat = tk.Label(new, text='胖', font=(None, 100))
    fat.pack()
    root.after(100, gogogo)


label = tk.Label(root, text='MUMGET', font=(None, 30))
label.pack()
start = tk.Button(root, text='开始', command=gogogo, font=(None, 30))
start.pack()

root.focus_force()
root.mainloop()