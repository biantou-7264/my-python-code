# 制作者:biantou
# 制作项目:小明AI

# 本程序不用做商业用途

# ---设置区---
calculator_path = '/System/Applications/Calculator.app'
work_path = '/Applications/Pages.app'
# ------------

# 下方为程序区域
# 本程序无需安装库,请放心使用
import tkinter as tk
from time import sleep
from tkinter import scrolledtext as st
from datetime import datetime
from random import choice
import subprocess as sp
from tkinter import messagebox as mb

# 说明:这些笑话由AI提供,未验证版权问题
happy_speech = ['我把“懒”当成了一种生活态度，结果身体以为我出家了。',
                '每次下定决心早睡，手机就变成了一块磁铁，我的脸是铁做的。',
                '减肥是一辈子的事业，可惜我这个“老板”经常跑路。',
                '贫穷使我理智，因为每次想冲动消费，余额都会给我一记响亮的耳光。',
                '上帝是公平的，给了我丑的外表，一定会给我低的智商，以免显得不协调。',
                '我的人生就像一块豆腐，干啥都碎。',
                '上班的意义是什么？就是用我的精神内耗，换取老板的物质自由。',
                '别跟我谈理想，我的理想就是不工作还有钱拿。',
                '每次照镜子，我都会对里面的人说：“你要是再瘦点、好看点，咱俩就是绝配了。”']

luanma = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM[]\\;,./1234567890-=+~·`!@#$%^&*(){}|:"<>?')

# 说明:这些夸人句子由AI生成
kuakua = '你真好看，你太聪明了，你特别温柔，你非常靠谱，你总能带来欢笑，你让人如沐春风，你像星星一样闪亮，你的善良打动了所有人，你的努力让人佩服，你有一种独特的气质，你做事特别细致，你说话让人舒服，你是我见过最有趣的人，你总能把事情做得完美，你像阳光一样温暖，你总能照顾到每个人的情绪，你是个宝藏般的存在，你值得世间所有美好'.split('，')

sensitive_words = {'傻', '你妈', '屎', '死', '肏', '他妈', '屎', '尿', '笨', '蠢'}  # 说明:当前集合仅供敏感词识别,无不良引导!


def format_week(week):  # 把英语日期变成中文
    if week == 'Mon':
        return '星期一'
    elif week == 'Tue':
        return '星期二'
    elif week == 'Wed':
        return '星期三'
    elif week == 'Thu':
        return '星期四'
    elif week == 'Fri':
        return '星期五'
    elif week == 'Sat':
        return '星期六'
    elif week == 'Sun':
        return '星期日'
    else:
        return week


def quit_program(event=None):  # 退出程序的确定
    res = mb.askokcancel('提示', '你真的要退出吗?')
    if res:
        root.quit()


def answer(event):  # 回答
    user = entry.get()
    for i in sensitive_words:
        if i in user:
            res = mb.askokcancel('注意', '当前内容可能不太合适,确定发送?')
            if res:
                break
            else:
                return
    stdout('%s' % user)
    if '时间' in user or '几点' in user:  # 问时间
        now = datetime.now()
        time = now.strftime('现在是%H:%M:%S')
        stdout(time)
    elif '日期' in user or '几月' in user or '几日' in user:  # 问日期
        now = datetime.now()
        date = now.strftime('现在是%Y年%m月%d日') + format_week(now.strftime('%a'))
        stdout(date)
    elif '你好' in user or 'hello' in user or 'hi' in user or 'hey' in user or '哈喽' in user or '嗨' in user:  # 打招呼
        stdout('你好!')
    elif '笑话' in user:
        stdout(choice(happy_speech))
    elif '等于' in user:  # 用户想要帮他算数
        try:
            stdout('请自己算')
            res = sp.run(['open', calculator_path])  # 打开计算器
        except BaseException as e:
            stdout(e)
    elif '计算' in user:
        try:
            stdout('已打开计算器')
            res = sp.run(['open', calculator_path])
        except BaseException as e:
            stdout(e)
    elif '名字' in user:
        stdout('我是小明')  # “小明”是随便起的名字,本程序不商用本名字
    elif '乱码' in user:
        for _ in range(1000):
            stdout(choice(luanma), False)
    elif '猜数字' in user:
        try:
            stdout('猜数字游戏启动,本程序将会冻结')
            res = sp.run(['python3', '/Users/luojingfeng/Documents/guess-num.py'])  # 这是我的图形界面猜数字游戏
            stdout('程序退出,退出代码为%d' % res.returncode)
        except BaseException as e:
            stdout(e)
    elif '吃豆' in user:
        try:
            stdout('吃豆豆游戏启动,本程序将会冻结')
            res = sp.run(['python3', '/Users/luojingfeng/Documents/chidouren.py'])  # 这是我的吃豆人游戏
            stdout('程序退出,退出代码为%d' % res.returncode)
        except BaseException as e:
            stdout(e)
    elif '贪吃蛇' in user:
        try:
            stdout('贪吃蛇游戏启动,本程序将会冻结')
            res = sp.run(['python3', '/Users/luojingfeng/Documents/tanchishe.py'])  # 这是我的贪吃蛇游戏
            stdout('程序退出,退出代码为%d' % res.returncode)
        except BaseException as e:
            stdout(e)
    elif '打砖块' in user:
        try:
            stdout('打砖块游戏启动,本程序将会冻结')
            res = sp.run(['python3', '/Users/luojingfeng/Documents/dazhuankuai.py'])  # 这是我的打砖块游戏
            stdout('程序退出,退出代码为%d' % res.returncode)
        except BaseException as e:
            stdout(e)
    elif 'flappy' in user and 'bird' in user:
        try:
            stdout('flappy bird游戏启动,本程序将会冻结')
            res = sp.run(['python3', '/Users/luojingfeng/Documents/fly-bird.py'])  # 这是我的flappy bird游戏
            stdout('程序退出,退出代码为%d' % res.returncode)
        except BaseException as e:
            stdout(e)
    elif '夸' in user:  # 用户要夸他
        stdout(choice(kuakua))
    elif '关灯' in user:  # 关灯就是黑屏
        stdout('好的,按ESC开灯')
        sleep(0.5)
        black_screen = tk.Toplevel(root)
        black_screen.title('')  # macos在全屏模式下把鼠标移到顶部还是有标题,所以要清空
        black_screen.configure(bg='black')
        black_screen.attributes('-fullscreen', True)
        black_screen.overrideredirect(True)
        black_screen.bind('<Escape>', lambda event: black_screen.destroy())  # 退出黑屏(开灯)
    elif '退出' in user or '再见' in user or 'bye' in user or '拜拜' in user:
        quit_program()
    else:
        stdout('抱歉,暂时回答不了[%s]' % user)
    entry.delete(0, tk.END)


def stdout(text, next_line=True):  # 输出文字
    # 把next_line传入False或0即可关闭自动换行
    text_area.config(state=tk.NORMAL)  # 解锁文字区
    text_area.insert(tk.END, text)  # 输出
    if next_line:
        text_area.insert(tk.END, '\n')  # 换行
    text_area.see(tk.END)  # 自动滚屏
    text_area.config(state=tk.DISABLED)  # 锁定文字区
    root.update()  # 刷新


def work(event):
    root.iconify()
    sp.run(['open', work_path])


font_family = 'Arial'
font_size = 15
root = tk.Tk()
root.title('小明AI')
root.configure(bg='#323232')

text_area = st.ScrolledText(root, font=(font_family, font_size), fg='white', bg='black', highlightbackground='#646464', highlightcolor='white', state=tk.DISABLED, wrap=tk.WORD)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
entry = tk.Entry(root, font=(font_family, font_size), fg='white', bg='black', highlightbackground='#646464', highlightcolor='white')
entry.pack(padx=10, pady=10, fill=tk.X, expand=True)
entry.bind('<Return>', answer)

stdout('欢迎使用小明AI!')
stdout('在使用过程中,按下F10可以立刻最小化,并调出办公界面')

root.protocol('WM_DELETE_WINDOW', quit_program)
root.bind('<F10>', work)
root.bind('<Escape>', quit_program)
root.geometry('700x500')
root.focus_force()
root.mainloop()
