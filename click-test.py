import tkinter as tk
root=tk.Tk()
def a():
    global count
    count+=1
    label.config(text=count)
count=0
label=tk.Label(root,text=0,font=(None,20))
label.pack()
button=tk.Button(root,text='click me!',command=a,font=(None,20))
button.pack()
root.mainloop()