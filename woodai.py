import tkinter as tk
import woodAI as w
from tkinter import scrolledtext
import threading as thread
from time import sleep
import os
from signal import SIGKILL
from easygui import buttonbox,msgbox
import wifi
ask=False
def ok(event=None):
    global ta,en
    global user,ai
    global ask,wifi
    user=en.get()
    if user:
        ta.insert(tk.END,'\n')
        ta.insert(tk.END,user)
        ta.insert(tk.END,'\n')
        en.delete(0,tk.END)
        if ('清除' in user or '新' in user) and ('对话' in user or '聊天' in user):
            if not wifi.test():
                ta.insert(tk.END,'\n')
                ta.insert(tk.END,'断网了,无法开启新对话')
                ta.insert(tk.END,'\n')
            try:
                w.chat_clear()
                ta.insert(tk.END,'\n')
                ta.insert(tk.END,'已开启新对话')
                ta.insert(tk.END,'\n')
            except BaseException as e:
                ta.insert(tk.END,'\n')
                ta.insert(tk.END,'开启新对话失败:%s'% e)
                ta.insert(tk.END,'\n')
            return
        if 'token' in user and '设置' in user and ':' in user:
            token=user.split(':')[1]
            w.token_set(token)
            return
        ta.insert(tk.END,'AI回答中.')
        root.update()
        def task():
            global user,ai,wifi
            if not wifi.test():
                ta.insert(tk.END,'\n')
                ta.insert(tk.END,'断网了,无法回答该问题')
                ta.insert(tk.END,'\n')
            try:
                ai=w.chat('请回答用户:"%s",不要有markdown富文本,也不要用```这种方式表示代码区域,就像平常用户问你那样回答就行,语气要温柔点'% user)
            except BaseException as e:
                ai='回答时出现错误:%s'% e
        th=thread.Thread(target=task)
        th.start()
        ask=True
        while th.is_alive():
            ta.delete('end-1l',tk.END)
            ta.insert(tk.END,'\n')
            ta.insert(tk.END,'AI回答中.')
            root.update()
            sleep(0.2)
            ta.delete('end-1l',tk.END)
            ta.insert(tk.END,'\n')
            ta.insert(tk.END,'AI回答中..')
            root.update()
            sleep(0.2)
            ta.delete('end-1l',tk.END)
            ta.insert(tk.END,'\n')
            ta.insert(tk.END,'AI回答中...')
            root.update()
            sleep(0.2)
        ask=False
        ta.delete('end-1l',tk.END)
        ta.insert(tk.END,'\n\n')
        ta.insert(tk.END,ai)
        ta.insert(tk.END,'\n')
def kill():
    if ask:
        choice=buttonbox('⚠︎重要提示\nAI还没有结束回答\n你要强制结束吗',title='重要提示',choices=['确定','取消'])
        if '取' in choice:
            return
    os.kill(os.getpid(),SIGKILL)
root=tk.Tk()
ta=scrolledtext.ScrolledText(root,wrap=tk.NONE,width=75,height=30,font=(None,15),highlightbackground='gray',highlightcolor='red')
ta.pack(padx=10,pady=10,fill=tk.BOTH,expand=True)
en=tk.Entry(root,highlightbackground='gray',highlightcolor='red')
en.pack(padx=10,pady=10,fill=tk.X)
en.bind('<Return>',ok)
root.protocol('WM_DELETE_WINDOW',kill)
root.mainloop()