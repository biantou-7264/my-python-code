import tkinter as tk
import os
import sys
from subprocess import run
from easygui import msgbox,buttonbox
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading
from time import time
re_btn=0
rethread=0
delthread=0
sysapp=False
syav=0
root=tk.Tk()
box=tk.Listbox(root,font=(None,20))
box.pack(fill=tk.BOTH,expand=True)
root.geometry('400x600')
def re(debug=0):
    global apps,appnames,re_btn,rethread
    apps=[]
    appnames=[]
    def task():
        global rethread,syav,sysapp
        if syav!=0:
            sysapp=syav.get()
        if sysapp:
            for root1,dirs,files in os.walk('/'):
                for file in dirs:
                    if file.endswith('.app'):
                        path=os.path.join(root1,file)
                        apps.append(path)
                        appnames.append(file)
        else:
            for root1,dirs,files in os.walk('/Applications'):
                for file in dirs:
                    if file.endswith('.app'):
                        path=os.path.join(root1,file)
                        apps.append(path)
                        appnames.append(file)
            for root1,dirs,files in os.walk('/System/Applications'):
                for file in dirs:
                    if file.endswith('.app'):
                        path=os.path.join(root1,file)
                        apps.append(path)
                        appnames.append(file)
        box.delete(0,tk.END)
        for i in appnames:
            box.insert(tk.END,i)
        re1.config(state=tk.NORMAL)
        rethread=0
    rethread=threading.Thread(target=task)
    rethread.start()
    if re1!=0:
        re1.config(state=tk.DISABLED)
def locate():
    global apps
    index=box.curselection()
    if len(index)>0:
        index=index[0]
    else:
        return
    path=apps[index]
    res=run(['open','-R',path],capture_output=True,text=True)
    if res.returncode!=0:
        msgbox('显示文件位置时出现问题\n请尝试重新打开',title='错误',ok_button='知道了')
def delete():
    global apps,appnames,dele,delthread,index
    index=box.curselection()
    if len(index)>0:
        index=index[0]
    else:
        return
    path=apps[index]
    name=appnames[index]
    choice=buttonbox('⚠︎重要提示\n你确定要删除%s吗?'% name,title='重要提示',choices=['确定','取消'])
    if '取' in choice:
        return 'cancel'
    def task():
        res=run(['rm','-rf',path],capture_output=True,text=True)
        dele.config(state=tk.NORMAL)
        if res.returncode==0:
            root.after(0,deleok)
        else:
            root.after(0,deleno)
    delthread=threading.Thread(target=task)
    delthread.start()
    dele.config(state=tk.DISABLED)
def deleok():
    global delthread
    msgbox('删除成功!',title='提示',ok_button='知道了')
    delthread=0
    re()
def deleno():
    global delthread
    msgbox('删除失败\n请尝试重新删除',title='错误',ok_button='知道了')
    delthread=0
def quite():
    at=time()
    global rethread,delthread
    if rethread!=0:
        while True:
            if time()-at>20:
                break
            if rethread==0:
                break
            root.update()
    if delthread!=0:
        while True:
            if time()-at>20:
                break
            if delthread==0:
                break
            root.update()
    observer.stop()
    observer.join()
    sys.exit()
re()
loc=tk.Button(root,text='显示文件所在位置',command=locate,font=(None,20))
loc.pack()
dele=tk.Button(root,text='删除选中的文件',command=delete,font=(None,20))
dele.pack()
re_btn=tk.Button(root, text='立即刷新列表', command=re, font=(None, 20))
re_btn.pack()
syav=tk.BooleanVar()
sya=tk.Checkbutton(root,text='显示整个系统的软件',variable=syav,onvalue=True,offvalue=False,font=(None,20))
sya.pack()
qu=tk.Button(root,text='安全退出程序',command=quite,font=(None,20))
qu.pack()
root.bind('<F5>',re)
root.protocol('VM_DELETE_WINDOW',quite)
event_handler=PatternMatchingEventHandler(patterns=['*'],ignore_patterns=None,ignore_directories=False,case_sensitive=True)
event_handler.on_created=re
event_handler.on_modified=re
event_handler.on_deleted=re
event_handler.on_moved=re
observer=Observer()
observer.schedule(event_handler,'.',recursive=True)
observer.start()
root.focus_force()
root.mainloop()