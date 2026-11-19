import tkinter as tk
from tkinter import filedialog as fd
from pydub import AudioSegment
from tkinter import messagebox as mb
import os


def choose_m4a():
    path = fd.askopenfilename(defaultextension='*.m4a', filetypes=[('M4A', '*.m4a'), ('All files', '*.*')])
    if path:
        m4a_path.set(path)


def choose_m4a_folder():
    path = fd.askdirectory()
    if path:
        m4a_folder_path.set(path)


def choose_mp3():
    path = fd.asksaveasfilename(defaultextension='*.mp3', filetypes=[('MP3', '*.mp3')])
    if path:
        mp3_path.set(path)


def choose_mp3_folder():
    path = fd.askdirectory()
    if path:
        mp3_folder_path.set(path)


def start():
    try:
        audio = AudioSegment.from_file(m4a_path.get(), format='m4a')
        audio.export(mp3_path.get(), format='mp3', bitrate='192k')
        mb.showinfo('提示', '转换成功')
    except BaseException as e:
        mb.showerror('错误', '%s:%s' % (type(e).__name__, e))


def many_start():
    root.title('批量转换中...')
    root.update()
    root.update_idletasks()
    for path in os.listdir(m4a_folder_path.get()):
        full_path = os.path.join(m4a_folder_path.get(), path)
        name, ext = os.path.splitext(path)
        if 'm4a' in ext:
            try:
                root.title('批量转换中...%s' % path)
                root.update()
                root.update_idletasks()
                audio = AudioSegment.from_file(full_path, format='m4a')
                full_path = os.path.join(mp3_folder_path.get(), '%s.mp3' % name)
                audio.export(full_path, format='mp3', bitrate='192k')
            except BaseException as e:
                mb.showerror('错误', '%s|%s:%s' % (path, type(e).__name__, e))
    root.title('m4a转换mp3工具')
    root.update()
    root.update_idletasks()
    mb.showinfo('提示', '转换完成')


root = tk.Tk()
root.title('m4a转换mp3工具')
m4a_path = tk.StringVar(value='请选择m4a文件位置')
m4a_folder_path = tk.StringVar(value='请选择m4a文件夹位置')
mp3_path = tk.StringVar(value='请选择mp3文件保存文件')
mp3_folder_path = tk.StringVar(value='请选择mp3文件保存目录')

tk.Label(root, textvariable=m4a_path, font=('Arial', 30)).pack(padx=30, pady=10)
tk.Label(root, textvariable=m4a_folder_path, font=('Arial', 30)).pack(padx=30, pady=10)
tk.Label(root, textvariable=mp3_path, font=('Arial', 30)).pack(padx=30, pady=10)
tk.Label(root, textvariable=mp3_folder_path, font=('Arial', 30)).pack(padx=30, pady=10)
tk.Label(root, text='请点击顶部菜单栏操作', font=('Arial', 20)).pack(padx=30, pady=10)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='选择m4a文件位置', command=choose_m4a)
file_menu.add_command(label='选择mp3文件保存位置', command=choose_mp3)
file_menu.add_command(label='选择m4a目录位置', command=choose_m4a_folder)
file_menu.add_command(label='选择mp3文件保存目录', command=choose_mp3_folder)
menu_bar.add_cascade(label='文件', menu=file_menu)
start_menu = tk.Menu(menu_bar, tearoff=0)
start_menu.add_command(label='开始转换', command=start)
start_menu.add_command(label='批量转换', command=many_start)
start_menu.add_command(label='退出', command=root.quit)
menu_bar.add_cascade(label='开始', menu=start_menu)
root.config(menu=menu_bar)

root.focus_force()
root.mainloop()
