import tkinter as tk
from tkinter import scrolledtext as st


def stdout(text):
    text_area.insert(tk.END, text)
    text_area.insert(tk.END, '\n')
    text_area.see(tk.END)


root = tk.Tk()
root.title('全自动入侵系统')

text_area = st.ScrolledText(root, width=100, height=100, wrap=tk.WORD, bg='black', fg='#00ff00', font=('Arial', 15))
text_area.pack(fill=tk.BOTH, expand=True)

root.attributes('-fullscreen', True)
root.focus_force()
root.mainloop()
