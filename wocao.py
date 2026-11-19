try:
    import tkinter as tk

    exit = False
    windows = []


    def quit(a=0):
        global exit
        exit = True
        for i in windows:
            try:
                i.destroy()
            except Exception:
                pass


    def create_window():
        if not exit:
            new_window = tk.Toplevel()
            new_window.geometry("300x300")
            windows.append(new_window)
            new_window.title(window_count.get())
            button = tk.Button(new_window, text="退出(Q)", command=quit)
            button.pack()
            new_window.bind("<q>", quit)
            new_window.focus_set()
            window_count.set(window_count.get() + 1)
        new_window.after(20, create_window)


    root = tk.Tk()
    root.title("你好")
    root.geometry("300x300")
    window_count = tk.IntVar()
    windows.append(root)
    window_count.set(1)
    button = tk.Button(root, text="启动", command=create_window)
    button.pack()
    button = tk.Button(root, text="退出", command=quit)
    button.pack()
    root.mainloop()
except Exception:
    print("已退出")
