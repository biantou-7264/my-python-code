import tkinter as tk
from random import randint
from tkinter import messagebox as mb
import subprocess as sp
import sys

sp.run([sys.executable, '-m', 'pip', 'install', 'pyttsx3', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/'])

import pyttsx3 as tts

from threading import Thread

sp.run([sys.executable, '-m', 'pip', 'install', 'pyautogui', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple/'])

import pyautogui as pag

APP_NAME = '某某某工具'


def step1():
    win = tk.Toplevel()
    win.title('欢迎使用')
    tk.Label(win, text='欢迎使用%s' % APP_NAME, font=('Arial', 40)).pack(padx=20, pady=10)
    tk.Button(win, text='立即安装', font=('Arial', 20), command=lambda: step2(win)).pack(pady=10, padx=20, fill=tk.X)
    win.focus_force()


class step2:
    def __init__(self, win):
        win.destroy()
        self.win = tk.Toplevel()
        self.win.title('协议')
        self.a_ok = tk.BooleanVar(value=False)
        self.b_ok = tk.BooleanVar(value=False)
        self.c_ok = tk.BooleanVar(value=False)
        self.d_ok = tk.BooleanVar(value=False)
        self.e_ok = tk.BooleanVar(value=False)
        self.f_ok = tk.BooleanVar(value=False)
        self.ok_vars = [self.a_ok, self.b_ok, self.c_ok, self.d_ok, self.e_ok, self.f_ok]
        tk.Checkbutton(self.win, variable=self.a_ok, text='我同意《隐私协议》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Checkbutton(self.win, variable=self.b_ok, text='我同意《用户协议》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Checkbutton(self.win, variable=self.c_ok, text='我同意《儿童隐私安全协议》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Checkbutton(self.win, variable=self.d_ok, text='我同意《个人信息收集协议》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Checkbutton(self.win, variable=self.e_ok, text='我同意《数据跨境传输协议》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Checkbutton(self.win, variable=self.f_ok, text='我同意《社区服务条款》', font=('Arial', 30)).pack(pady=10, padx=20)
        tk.Button(self.win, text='确定', command=self.done, font=('Arial', 30)).pack(pady=10, padx=20)

    def done(self):
        for var in self.ok_vars:
            if not var.get():
                mb.showwarning('提醒', '请同意所有协议')
                return
        self.win.destroy()
        step3()


class step3:
    def __init__(self):
        self.win = tk.Toplevel()
        self.win.title('正在安装')
        self.text = tk.Label(self.win, text='正在安装... 0%%', font=('Arial', 30))
        self.text.pack(pady=10, padx=20)
        self.win.focus_force()
        self.win.after(1000, self.fake_insatall)

    def fake_insatall(self, progess=0):
        if progess > 100:
            self.win.after(10, self.done)
        self.text.config(text='正在安装... %d%%' % progess)
        progess += 1
        self.win.after(20, lambda: self.fake_insatall(progess))

    def done(self):
        self.win.destroy()
        step4()


def step4():
    quanxians = '摄像头,麦克风,定位服务,完全磁盘访问,文件与文件夹,蓝牙,本地网络,输入监控,无障碍,App管理,远程桌面,录屏与系统录音,硬件连接,终端,后台运行,系统服务,root,弹出式窗口,重定向,跟踪,剪贴板,修改系统设置,唤醒,电源测量,通知监听,通知,自动播放,共享数据,画中画,显示在最上层'.split(',')
    for quanxian in quanxians:
        while True:
            res = mb.askyesno('提醒', '%s想要%s' % (APP_NAME, quanxian))
            if res:
                break
    pag.move(1, 1)
    step5()


def step5():
    Thread(target=say_ads, daemon=True).start()
    while True:
        pag.move(randint(-10, 10), randint(-10, 10))
        win = tk.Toplevel(root)
        win.title('欢迎使用%s!!!' % APP_NAME)
        tk.Label(win, text='欢迎使用%s!!!' % APP_NAME, font=('Arial', 50)).pack()
        win.focus_force()
        win.update()


def say_ads():
    while True:
        engine = tts.init()
        engine.setProperty('rate', 200)
        engine.say('【信尔美】今日晚8点超品日秒杀！玛仕度肽天然双靶点，代谢全面获益～冷链运输多地次日达！领券减50元 3.cn/v/uyy79n 拒收请回复R')
        engine.runAndWait()


root = tk.Tk()
root.withdraw()

root.after(1000, step1)
root.mainloop()
