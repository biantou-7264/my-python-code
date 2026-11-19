import subprocess as sp
from threading import Thread
import tkinter as tk
from tkinter import filedialog


def play(path):
    sp.run(['ffplay', path])

def choose_play():
    path = filedialog.askopenfilename(title='选择文件', defaultextension='.mp4', filetypes=[('视频', '*.mp4 *.mkv *.avi *.mov *.wmv *.webm *.flv *.vob *.3gp'), ('音频', '*.mp3 *.aac *.flac *.wav *.ogg'), ('流媒体', '*.m3u8 *.rtmp *.rtsp'), ('图片', '*.jpg *.png *.gif')])
    if path:
        thread = Thread(target=play, args=(path,))
        thread.daemon = True
        thread.start()


root = tk.Tk()
root.title('播放器')

menu_bar = tk.Menu(root)
start_menu = tk.Menu(menu_bar, tearoff=0)
start_menu.add_command(label='选择播放', command=choose_play)
menu_bar.add_cascade(label='开始', menu=start_menu)
root.config(menu=menu_bar)

root.focus_force()
root.mainloop()
