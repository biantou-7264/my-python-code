import tkinter as tk
import tts
root=tk.Tk()
def hey():
    tts.speak('小美小美!')
def on():
    tts.speak('打开风扇')
def off():
    tts.speak('关闭风扇')
def small():
    tts.speak('调小风速')
def big():
    tts.speak('调大风速')
def youfan():
    tts.speak('自选风')
def fanfan():
    tts.speak('自然风')
def cool():
    tts.speak('打开清凉风')
def nocool():
    tts.speak('关闭清凉风')
def dongon():
    tts.speak('打开摆风')
def dongoff():
    tts.speak('关闭摆风')
def pnon():
    tts.speak('打开负离子')
def pnoff():
    tts.speak('关闭负离子')
def wind():
    global n
    tts.speak('调到%s挡风'% n.get())
def ton():
    global p
    tts.speak('%s小时后开机'% p.get())
def toff():
    global p
    tts.speak('%s小时后关机'% p.get())
def tc():
    tts.speak('取消定时!')
def von():
    tts.speak('打开语音')
def voff():
    tts.speak('关闭语音')
def vp():
    tts.speak('调大音量')
def vm():
    tts.speak('调小音量')
a=tk.Button(root,text='唤醒',command=hey,font=(None,20))
a.grid(row=0,column=0)
b=tk.Button(root,text='打开风扇',command=on,font=(None,20))
b.grid(row=1,column=0)
c=tk.Button(root,text='关闭风扇',command=off,font=(None,20))
c.grid(row=1,column=1)
d=tk.Button(root,text='调大风速',command=big,font=(None,20))
d.grid(row=2,column=0)
e=tk.Button(root,text='调小风速',command=small,font=(None,20))
e.grid(row=2,column=1)
f=tk.Button(root,text='自选风',command=youfan,font=(None,20))
f.grid(row=3,column=0)
g=tk.Button(root,text='自然风',command=fanfan,font=(None,20))
g.grid(row=3,column=1)
h=tk.Button(root,text='冷风开',command=cool,font=(None,20))
h.grid(row=4,column=0)
i=tk.Button(root,text='冷风关',command=nocool,font=(None,20))
i.grid(row=4,column=1)
j=tk.Button(root,text='打开摆风',command=dongon,font=(None,20))
j.grid(row=5,column=0)
k=tk.Button(root,text='关闭摆风',command=dongoff,font=(None,20))
k.grid(row=5,column=1)
l=tk.Button(root,text='打开负离子',command=pnon,font=(None,20))
l.grid(row=6,column=0)
m=tk.Button(root,text='关闭负离子',command=pnoff,font=(None,20))
m.grid(row=6,column=1)
no=tk.Label(root,text='风速',font=(None,20))
no.grid(row=7,column=0)
n=tk.Entry(root,font=(None,20),width=10)
n.grid(row=7,column=1)
o=tk.Button(root,text='确定',command=wind,font=(None,20))
o.grid(row=7,column=2)
no=tk.Label(root,text='定时',font=(None,20))
no.grid(row=8,column=0)
p=tk.Entry(root,font=(None,20),width=10)
p.grid(row=8,column=1)
q=tk.Button(root,text='开',command=ton,font=(None,20))
q.grid(row=8,column=2)
r=tk.Button(root,text='关',command=toff,font=(None,20))
r.grid(row=8,column=3)
s=tk.Button(root,text='取消',command=tc,font=(None,20))
s.grid(row=8,column=4)
t=tk.Button(root,text='开语音',command=von,font=(None,20))
t.grid(row=9,column=0)
u=tk.Button(root,text='关语音',command=voff,font=(None,20))
u.grid(row=9,column=1)
v=tk.Button(root,text='音量+',command=vp,font=(None,20))
v.grid(row=9,column=2)
w=tk.Button(root,text='音量-',command=vm,font=(None,20))
w.grid(row=9,column=3)
root.mainloop()