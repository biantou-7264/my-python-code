# 导入库
# 未安装会自动安装
print('导入库......')
import subprocess as sub
import sys
import time

sts = float(time.perf_counter())
try:
    import pyautogui as pg
except:
    print('安装pyautogui......')
    sub.run([sys.executable, '-m', 'pip', 'install', 'pyautogui', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '10'], capture_output=True)
    print('安装完成')
    import pyautogui as pg
print('pyautogui导入完成')
try:
    from pyperclip import copy
except:
    print('安装pyperclip......')
    sub.run([sys.executable, '-m', 'pip', 'install', 'pyperclip', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '10'], capture_output=True)
    print('安装完成')
    from pyperclip import copy
print('pyperclip导入完成')
try:
    from pynput import keyboard
except:
    print('安装pynput......')
    sub.run([sys.executable, '-m', 'pip', 'install', 'pynput', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', '--retries', '10'], capture_output=True)
    print('安装完成')
    from pynput import keyboard
print('pynput导入完成')
import tkinter as tk
import msgbox
from tkinter import simpledialog as enbox

print('tkinter导入完成')

# 初始化变量
print('初始化变量......')
sp = 0  # 速度
print('sp初始化完成')
r = False  # 刷屏开始停止
print('r初始化完成')
ic = False  # 最小化
print('ic初始化完成')
nic = False  # 最小化的debug变量
print('nic初始化完成')
nup = False  # was按下up
print('nup初始化完成')
ndn = False  # was按下down
print('ndn初始化完成')
nhp = False
print('nhp初始化完成')
pg.PAUSE = 0.03 * sp
print('PAUSE初始化完成')
pg.FAILSAFE = True
print('FAILSAFE初始化完成')
nowquit = False
print('nowquit初始化完成')
nq = False
print('nq初始化完成')
nta = False
print('nta初始化完成')
nres = False
print('nres初始化完成')
cli = False
print('cli初始化完成')

# 定义函数
print('初始化函数......')


def s(k):  # 按下按键时的函数
    global r, ic, cv, opt, opin, nup, ndn, nhp, sp, nq, nta, nres  # 这些变量需要修改

    if k == keyboard.Key.alt:
        # 开始/停止刷屏
        if not r:
            r = True
        else:
            r = False

    if k == keyboard.Key.esc:
        # 停止刷屏
        r = False

    if k == keyboard.Key.ctrl:
        # 显示隐藏窗口
        if not ic:
            ic = True
        else:
            ic = False

    # 上下
    if k == keyboard.Key.up:
        nup = True
    if k == keyboard.Key.down:
        ndn = True

    if k == keyboard.Key.tab:
        # 切换
        nta = True

    # 调整刷屏速度
    if k == keyboard.Key.left:
        if not ic:
            if sp <= 0:
                sp = 0
                return
            sp -= 0.1
    if k == keyboard.Key.right:
        if not ic:
            sp += 0.1

    if k == keyboard.Key.f1:
        # 显示帮助
        nhp = True

    if k == keyboard.Key.f10:
        # 退出程序
        nq = True

    if k == keyboard.Key.f5:
        # 重置
        nres = True


print('s初始化完成')


def ff():  # 窗口获得焦点
    root.focus_force()


print('ff初始化完成')


def up():  # 向上
    if not ic:
        opin = opt.index(cv.get())  # 获得目前索引
        if opin > 0:
            opin -= 1  # 向上移动要-1
        cv.set(opt[opin])


print('up初始化完成')


def dn():  # 向下
    if not ic:
        opin = opt.index(cv.get())  # 获得目前索引
        if opin != (len(opt) - 1):
            opin += 1  # 向下移动要+1
        cv.set(opt[opin])


print('dn初始化完成')


def tab():  # 切换
    if not ic:
        opin = opt.index(cv.get())  # 获得目前索引
        if opin != (len(opt) - 1):  # 没到最后
            opin += 1  # 向下移动
        else:
            opin = 0  # 第一项
        cv.set(opt[opin])


print('tab初始化完成')


def cr():  # 创建窗口
    global cv, root, opt, opin, sp, tl, ras, rasl, raslc, lcols, cols, mcols, enras  # 需要在主程序调用的变量
    print('创建root窗口......')
    root = tk.Tk()
    root.title('选择刷屏内容')

    print('初始化变量......')
    cv = tk.StringVar(value='')
    # opt=刷屏内容
    # cols=未选中颜色
    # mcols=鼠标悬停颜色
    # lcols=选中颜色
    opt = ['老师上课玩手机!', 'A', 'B', 'C', 'D', '大家好,我在刷屏', '老师好', '1', '第一', '你好', '接接接', '666', '  ', '⚠︎该用户发表违规言论，已经禁言', '▚▛▜▝▞▟■□▢▣▤▥▦▧', 'ȸ҉۞؋؊؉؈ʬʫʭ˥ˤˣˢˡˠ˟', 'ꙮ҈҉֍֎؎؏٭۞۩܀܁܂༓༔༕༖︴', 'ꙮ꙯꙰꙱꙲꙳ꙴꙵꙶꙷꙸꙹꙺꙻ꙼꙽꙾ꙿ', '߷߸߹ߺ߽߾߿ࠀࠁࠂࠃࠄࠅࠆࠇ', '不知道']
    cols = ['#7f0000', '#643200', '#646400', '#006400', '#000064', '#500064', '#800067'] * 5
    mcols = ['#b60000', '#c54400', '#c3c300', '#00b300', '#6464c8', '#c300c3', '#c800f7'] * 5
    lcols = ['#ff0000', '#ff6400', '#ffff00', '#00ff00', '#6464ff', '#c800ff', '#ff00f0'] * 5
    root.configure(bg='#c8c8c8')  # 窗口颜色
    ras = {}  # 按钮字典 格式(按钮:颜色)
    rasl = []  # 按钮列表
    raslc = []  # 按钮内容列表
    enras = []  # 碰到鼠标的按钮

    print('创建组件......')
    for i, o in enumerate(opt):  # 遍历刷屏内容创建按钮
        print('创建%d号组件' % i)
        # o变量为当前遍历到选项
        # i变量为当前遍历索引
        radio = tk.Radiobutton(root, text=o, variable=cv, value=o, bg=cols[i], indicatoron=0, fg='#c8c8c8', bd=0, cursor='pointinghand', font=('圆体-简', 20))
        radio.pack(anchor='w', fill=tk.BOTH, expand=True)
        print('配置%d号组件' % i)
        radio.number = i
        radio.context = o
        ras[radio] = cols[i]
        rasl.append(radio)
        raslc.append(o)
        # 绑定事件
        radio.bind('<MouseWheel>', whr)
        radio.bind('<Enter>', ren)
        radio.bind('<Leave>', rle)
        radio.bind('<Button-1>', pre)
        radio.bind('<ButtonRelease-1>', rel)

    print('初始化变量......')
    cv.set('老师上课玩手机!')  # 默认第0项
    opin = 0  # 选中索引
    print('创建组件......')
    tl = tk.Label(root, text='刷屏延迟倍数=1', bg='#323232', fg='#c8c8c8', cursor='text', font=('圆体-简', 20))
    tl.pack(anchor='w', fill=tk.BOTH, expand=True)
    print('绑定事件......')
    tl.bind('<Button-1>', settl)
    tl.bind('<MouseWheel>', wht)
    tl.bind('<Enter>', ten)
    tl.bind('<Leave>', tle)
    sp = 1


print('cr初始化完成')


def pre(event):  # 按下鼠标
    global cli
    cli = True
    radio = event.widget
    cv.set(radio.context)


def rel(event):  # 放开鼠标
    global cli
    cli = False
    radio = event.widget
    cv.set(radio.context)


def whr(event=None):  # 在选项按钮中滚动
    if event.delta > 5:  # 向上滚动
        up()
    if event.delta < -5:  # 向下滚动
        dn()


print('whr初始化完成')


def wht(event=None):  # 在刷屏速度文字滚动
    global sp
    if event.delta > 5:
        if sp <= 0:  # 这里防止小于0
            sp = 0
            return
        sp -= 0.1
    if event.delta < -5:
        sp += 0.1


print('wht初始化完成')


def ren(e):  # 鼠标进入单选框
    global cv, enras, cli
    radio = e.widget
    rac = radio.context
    i = radio.number
    enras.append(e.widget)
    if cv.get() != rac:
        radio['fg'] = '#323232'  # 选中后字体变黑
        radio['bg'] = mcols[i]
    if cli:
        cv.set(rac)


print('ren初始化完成')


def rle(e):  # 鼠标退出单选框
    global cv, enras
    radio = e.widget
    rac = radio.context
    i = radio.number
    try:
        enras.remove(e.widget)
    except:
        pass
    if cv.get() != radio.context:
        radio['fg'] = '#c8c8c8'  # 取消选中后字体变白
        radio['bg'] = cols[i]


print('rle初始化完成')


def ten(e):  # 鼠标进入延迟文字
    global cv, enras
    t = e.widget
    t['fg'] = '#323232'  # 选中后字体变黑
    t['bg'] = '#c8c8c8'  # 选中后背景变白


print('ten初始化完成')


def tle(e):  # 鼠标退出延迟文字
    global cv
    t = e.widget
    t['fg'] = '#c8c8c8'  # 取消选中后字体变白
    t['bg'] = '#323232'  # 取消选中后字体变黑


print('tle初始化完成')


def settl(event=None):  # 输入速度
    global sp
    en = enbox.askfloat('设置', '输入要设置的刷屏延迟倍数')
    if en is not None:
        sp = en


print('setll初始化完成')


def cp():  # 窗口更新
    global nowquit, ras, cv, lcols, sp, enras, cli, mcols
    if sp < 0:  # 防止小于0  后面不打本条注释
        sp = 0
    try:
        if not nowquit:
            copy(cv.get())  # 拷贝选中内容
            root.geometry('400x750+0+0')  # 防止调节窗口大小
            tl.config(text='刷屏延迟倍数=%.1f' % sp)  # 更新

            pg.PAUSE = 0.03 * sp  # 调节速度
            pg.FAILSAFE = True  # 保证安全

            root.attributes('-fullscreen', False)  # 防止全屏

            c = 0
            for r in ras.keys():  # 检查按钮选中
                if r['text'] == cv.get():  # 选中
                    a = lcols[c]  # 高亮效果颜色
                    r['bg'] = a
                    r['fg'] = '#323232'  # 选中后文字变黑
                else:
                    if r not in enras:
                        a = ras[r]  # 获取原本颜色
                        r['bg'] = a
                        r['fg'] = '#c8c8c8'  # 未选中文字变白
                c += 1
    except:
        pass

    if not nowquit:
        if sp < 0:
            sp = 0
        root.after(10, cp)  # 继续更新


print('cp初始化完成')


def help():  # 显示帮助消息F1
    msgbox.info(root, '帮助内容\n按control键显示隐藏窗口\n按alt开始/停止刷屏\n按esc停止刷屏\n按上下键切换内容(需要显示窗口)\n按左右键可以调整刷屏延迟(刻度0.1)(需要显示窗口)\n按f10退出', '我知道了')


print('help初始化完成')


def safequit():  # 退出
    global nowquit, l, root
    for i in root.winfo_children():  # 清空窗口
        i.pack_forget()
    nowquit = True
    l.stop()

    print('等待事件结束......')
    for i in range(50):  # 0.5秒后事件肯定结束
        pg.sleep(0.01)
        root.update()  # 让事件继续向后并且退出


print('safequit初始化完成')

print('创建监听者......')
l = keyboard.Listener(on_press=s)  # 创建监听键盘者
print('启动监听者......')
l.start()  # 启动

print('创建窗口......')
cr()
print('初始化界面......')
cp()

print('绑定窗口管理器协议......')
root.protocol('WM_DELETE_WINDOW', safequit)  # 安全退出

print('成功进入主循环')
nt = float(time.perf_counter())  # 计算启动时间
print('本次启动用时%.3f秒' % (nt - sts))

while not nowquit:
    if sp < 0:
        sp = 0
    root.update()

    if r:
        if sp < 0:
            sp = 0
        pg.click()  # 点击聊天框

        if sp < 0:
            sp = 0
        if sp >= 0:
            pg.sleep(0.02 * sp)

        pg.hotkey('command', 'v')  # 暂停刷屏内容
        pg.write('\n')  # 回车发送
        print('单次刷屏完成')

        if sp < 0:
            sp = 0
        if sp >= 0:
            pg.sleep(0.02 * sp)

    if sp < 0:
        sp = 0

    if ic:
        nic = True
        root.iconify()
    else:
        ff()
        root.deiconify()
        nic = False

    # 是否要触发事件
    if nup:
        up()
        nup = False
    if ndn:
        dn()
        ndn = False

    if nhp:
        ic = True
        help()
        nhp = False

    if nq:
        safequit()
        nq = False

    if nta:
        tab()
        nta = False

    if nres:
        sp = 1
        opin = 0
        cv.set(opt[opin])
        r = False
        nres = False

sys.exit(0)  # 退出程序,防止卡死
