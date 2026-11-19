import tkinter as tk
root=tk.Tk()
def onkey(event):
    print('keysym=%s,state=%d,keycode=%d'% (event.keysym,event.state,event.keycode))
root.bind_all('<Key>',onkey)
root.mainloop()