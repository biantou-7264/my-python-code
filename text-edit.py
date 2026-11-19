import tkinter as tk
from tkinter import filedialog, scrolledtext, Menu
from easygui import msgbox, buttonbox
from subprocess import run
from os import remove, kill, getpid
import random as r
import re
import webbrowser as web
import sys
from signal import SIGKILL

fd = filedialog
st = scrolledtext
fp = ''
write = False
edit = False
root = tk.Tk()
root.title('文本编辑-初始化')
root.update()


def new(event=None):
    global fp, edit
    if edit:
        choice = buttonbox('⚠︎重要提示\n文件还没有保存\n你要保存它吗', title='重要提示', choices=['保存', '不保存'])
        if '不' not in choice:
            save()
    fp = ''
    ta.delete('1.0', tk.END)


def openfile(event=None):
    global fp, root, edit
    afp = filedialog.askopenfilename(title='选择文件', filetypes=[('文本文档', '*.txt'), ('[不太兼容]富文本文档', '*.rtf'), ('代码文件', '*.py *.java *.c *.h *.cpp *.cs *.go *.rs *.kt *.kts *.swift *.html *.css *.js *.coffee *.ts *.php *.lua'), ('所有文件', '*.*')])
    if not afp:
        msgbox('你取消了文件选择', title='提示', ok_button='好的')
        return
    if edit:
        choice = buttonbox('⚠︎重要提示\n文件还没有保存\n你要保存它吗', title='重要提示', choices=['保存', '不保存'])
        if '不' not in choice:
            save()
    try:
        print(fp)
        fs1 = run(['wc', '-l', afp], capture_output=True, text=True)
        fs = int(fs1.stdout.split()[0])
        print(fs)
        f = open(afp, 'r')
        ta.delete('1.0', tk.END)
        root.title('正在打开文件')
        root.update()
        c = 0
        ii = 0
        for i in f:
            ta.insert(tk.END, i)
            c += 1
            ii += 1
            if c > 10000:
                c = 0
                jd = (ii / fs) * 100
                root.title(str(jd) + '%')
                root.update()
        f.close()
        print(edit)
        fp = afp
    except FileNotFoundError as e:
        msgbox('打开文件时出现问题\n%s:%s\n这是一个bug\n请尝试重新打开' % (type(e), e), title='错误', ok_button='知道了')
    except UnicodeDecodeError:
        try:
            run(['open', fp])
        except BaseException as e:
            msgbox('打开文件时出现问题\n%s:%s\n请尝试重新打开' % (type(e), e), title='错误', ok_button='知道了')
    except BaseException as e:
        choice = buttonbox('打开文件时出现问题\n%s:%s\n请尝试重新打开' % (type(e), e), title='错误', choices=['关闭', '使用系统打开'])
        if '系统' in choice:
            try:
                run(['open', fp])
            except BaseException as e:
                msgbox('打开文件时出现问题\n%s:%s\n请尝试重新打开' % (type(e), e), title='错误', ok_button='知道了')
        f.close()
        raise e
    et()


def save(event=None):
    global fp, edit
    if not fp:
        afp = filedialog.asksaveasfilename(title='选择文件名称和保存位置', defaultextension='.txt', filetypes=[('文本文档', '*.txt'), ('[不太兼容]富文本文档', '*.rtf'), ('代码文件', '*.py *.java *.c *.h *.cpp *.cs *.go *.rs *.kt *.kts *.swift *.html *.css *.js *.coffee *.ts *.php *.lua'), ('所有文件', '*.*')])
        if not afp:
            msgbox('你取消了保存名称和位置选择', title='提示', ok_button='好的')
            return
        fp = afp
    try:
        f = open(fp, 'w')
        f.write(ta.get('1.0', 'end-1c'))
        f.close()
        edit = False
        et()
    except PermissionError:
        msgbox('保存文件时出现问题\n%s:%s\n你没有权限保存\n请获得权限后再保存' % (type(e), e), title='错误', ok_button='知道了')
    except BaseException as e:
        msgbox('保存文件时出现问题\n%s:%s\n请尝试重新保存' % (type(e), e), title='错误', ok_button='知道了')
        f.close()


def moveto(event=None):
    global fp
    if not fp:
        msgbox('该文件不存在\n请重新打开该文件', title='提示', ok_button='好的')
        return
    try:
        afp = filedialog.asksaveasfilename(title='选择保存位置', initialfile=fp, filetypes=[('文本文档', '*.txt'), ('[不太兼容]富文本文档', '*.rtf'), ('代码文件', '*.py *.java *.c *.h *.cpp *.cs *.go *.rs *.kt *.kts *.swift *.html *.css *.js *.coffee *.ts *.php *.lua'), ('所有文件', '*.*')])
        f = open(afp, 'w')
        f.write(ta.get('1.0', 'end-1c'))
        f.close()
        remove(fp)
        fp = afp
    except PermissionError:
        msgbox('移动文件时出现问题\n%s:%s\n你没有权限保存\n请获得权限后再移动' % (type(e), e), title='错误', ok_button='知道了')
    except BaseException as e:
        msgbox('移动文件时出现问题\n%s:%s\n请尝试重新移动' % (type(e), e), title='错误', ok_button='知道了')
        f.close()
        raise e


def saveto(event=None):
    global fp
    if not fp:
        msgbox('该文件不存在\n请重新打开该文件', title='提示', ok_button='好的')
        return
    try:
        afp = filedialog.asksaveasfilename(title='选择保存位置', initialfile=fp, filetypes=[('文本文档', '*.txt'), ('[不太兼容]富文本文档', '*.rtf'), ('代码文件', '*.py *.java *.c *.h *.cpp *.cs *.go *.rs *.kt *.kts *.swift *.html *.css *.js *.coffee *.ts *.php *.lua'), ('所有文件', '*.*')])
        f = open(afp, 'w')
        f.write(ta.get('1.0', 'end-1c'))
        f.close()
        choice = buttonbox('你需要打开另一个文件吗?', title='提示', choices=['取消', '确定'])
        if '定' in choice:
            fp = afp
    except PermissionError:
        msgbox('移动文件时出现问题\n%s:%s\n你没有权限保存\n请获得权限后再移动' % (type(e), e), title='错误', ok_button='知道了')
    except BaseException as e:
        msgbox('移动文件时出现问题\n%s:%s\n请尝试重新移动' % (type(e), e), title='错误', ok_button='知道了')
        f.close()


def delete(event=None, yes=False, force=False):
    if not force:
        if not fp:
            msgbox('该文件不存在\n请重新打开该文件', title='提示', ok_button='好的')
            return
    if yes:
        choice = '真的确定,非常确定,不取消'
    else:
        choice = buttonbox('⚠︎重要提示\n删除文件后无法恢复\n你真的要删除该文件吗?', title='警告', choices=['取消', '确定'])
    if '定' in choice:
        if yes:
            choice = '确定确定必须确定,不许取消'
        else:
            choice = buttonbox('⚠︎重要提示\n这是最后一次警告\n你真的要删除该文件吗?', title='最后一次警告', choices=['取消', '确定'])
        if '定' in choice:
            try:
                remove(fp)
                fp = ''
                msgbox('文件已经删除了', title='提示', ok_button='好的')
            except PermissionError:
                msgbox('删除文件时出现问题\n%s:%s\n你没有权限删除\n请获得权限后再删除' % (type(e), e), title='错误', ok_button='知道了')
            except BaseException as e:
                msgbox('删除文件时出现问题\n%s:%s\n请尝试重新删除' % (type(e), e), title='错误', ok_button='知道了')


def 饿啊():
    choice = buttonbox('毁文件后无法恢复\n你真的要毁掉该文件吗?', title='警告', choices=['取消', '确定'])
    if '定' in choice:
        choice = buttonbox('这是最后一次警告\n你真的要毁掉该文件吗?', title='最后一次警告', choices=['取消', '确定'])
        if '定' in choice:
            try:
                a1 = 'ȻȼȾȿɁɂɃɄɅɆɇɈɉɊɋɌɍɎɏⱠⱡⱢⱣⱤⱥⱦⱧⱨⱩⱪⱫⱬⱭⱮⱯⱰⱱⱲⱳⱴⱵⱶⱷ꜠꜡ꜢꜣꜤꜥꜦꜧꜨꜩꜪꜫꜬꜭꜮꜯꜰꜱꜲꜳꜴꜵꜶꜷꜸꜹꜺꜻꜼꜽﬓﬔﬕﬖﬗ﬘﬙﬚﬛﬜יִﬞײַﬠﬡﬢﬣﬤﬥﬦﬧ〆〒〠〡〢〣〤〥〦〧〨〩〪〭〮〯〫〬 '
                a2 = '⁄€‹›ﬁﬂ‡°·‚—±Œ„´‰ˇ¨ˆØ∏”’»ÅÍÎÏ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿⊈∆∆ℇℏ∀⊈⨒∳∟∟√⅋⊎≞≏⋞⋛⋋⋓⋋⋎⋜⋤⋣⋛⋇⊿⊽⋌⋮⨼⨺⩁⩹⩺⪻⟛"¨‰¦❡❣❢៛௹₮$฿₸₶₤₲₰₢₢﷼$☠︎♲♳⛔︎✉︎☣︎ⅅ𝐺𝑍⦉'
                a3 = 'ཀཁགངཅཆཇཉཏཐདནཔཕབམཙཚཛཝཞཟའཡརལཤསཧཨཀྲཀྱཀླགྲགྱᚠᚢᚦᚨᚱᚲ ᛒᛖᛁᛏᛊ ᛏᚨᚲᛖ ᚺᛖᚱᛖꯃꯤꯇꯝꯂꯩꯕꯃꯥꯂꯦꯝꯑꯁꯤꯃꯄꯨꯡꯐꯥꯎꯕ𐤀𐤁𐤂𐤃𐤄𐤅𐤆𐤇𐤈𐤉𐤊𐤋غظضذخثتشرقصفعسنملكيطحزوهدجبأختصغضفعهيبلامنقشزرذدجطكظغطكمنتالبيسشضذخثزعلقهوج'
                a4 = 'ɐqɔpǝɟƃɥıɾʞןɯuodbɹsʇnʌʍxʎz〔ﾉ｀Д´〕ﾉ＝○┳┻┻━┳━━┓【╰☆╮⊙▽⊙╰☆╮】★~(◠﹏◠)~★ƻӜӋԒↁↇϪϮϴᴥᴖᴗ⅌⅂Ⅎ⅄ȻɃΞ٭꧁༒☬♛∞♾️⚡ȻȼɄ฿'
                a5 = ' ( o.o ) > ^ < / __ ( @___ / O / (_____/ /_____/ U ><((((> / / / | | | | | | /| |______ _/|_||_`-.__ (___________()--o :-) : - D ; - ) :-( T_T :-( (°o°) O.O / /  / /------ (o) (o) * *** ***** ******* | | * * * *** * * * ♥♥♥ ♥♥♥♥♥ ♥♥♥♥♥♥♥ ♥♥♥♥♥ ♥♥♥ ♥ .d88b. .8P Y8. 88 88 `8b d8`Y88P. . ... ..... ......... ........... ......... ..... ... . . ✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧ ═════════════════ ■■■■■■■■■■■■■■■ # % @ W * + o x . - ~ '
                a = a1 + a2 + a3 + a4 + a5
                b = ''
                h = ta.get(1.0, 'end-1c')
                if len(h) > 5000000:
                    choice = buttonbox('要毁的文件很长(%s个字符)\n可能需要很长的时间\n确定要继续吗' % len(h), title='提示', choices=['取消', '确定'])
                    if '消' in choice:
                        return
                for j in h:
                    if j == '\n':
                        b += '\n☞\n'
                    else:
                        b = b + r.choice(a)
                ta.delete('1.0', tk.END)
                for i in b.splitlines():
                    ta.insert(tk.END, i)
                    ta.insert(tk.END, '\n')
                msgbox('文件已经毁掉了', title='提示', ok_button='好的')
            except PermissionError:
                msgbox('毁掉文件时出现问题\n%s:%s\n你没有权限修改\n请获得权限后再毁文件' % (type(e), e), title='错误', ok_button='知道了')
            except BaseException as e:
                msgbox('毁掉文件时出现问题\n%s:%s\n请尝试重新毁文件' % (type(e), e), title='错误', ok_button='知道了')


def staw(event):
    global write
    write = True


def stow(event):
    global write
    write = True


def onkey(event):
    global write, edit
    if write:
        nw = [16, 4, 8, 64, 0, 2, 1, 96]
        if event.state in nw:
            if event.keycode != 889192475 and event.state == 0:
                edit = True
                et()
        else:
            edit = True
            et()


def et():
    if edit:
        root.title('文本编辑-%s-⚠︎该文件未保存' % fp)
    else:
        root.title('文本编辑-%s' % fp)
    root.after(300, et)


def safequit():
    if edit:
        choice = buttonbox('⚠︎重要提示\n文件还没有保存\n你要保存它吗', title='重要提示', choices=['保存', '不保存'])
        if choice is None:
            return
        else:
            if '不' not in choice:
                save()
    root.destroy()
    root.quit()
    import sys
    sys.exit()


def openurl():
    textlist = ta.get('1.0', 'end-1c').splitlines()
    for i in textlist:
        urls = re.findall(r'https?://[^\s]+', i)
        for url in urls:
            web.open(url)


def tocode():
    textlist = ta.get('1.0', 'end-1c').splitlines()
    r = ''
    for i in textlist:
        for j in i:
            c = ord(j)
            for k in range(c):
                r += '​'
            r += '|'
        r += '\\'
    ta.delete('1.0', tk.END)
    ta.insert(tk.END, r)


def totext():
    code = ta.get('1.0', 'end-1c')
    ta.delete('1.0', tk.END)
    step1 = code.split('\\')
    ac = 0
    for i in step1:
        if ac != 0:
            ta.insert(tk.END, '\n')
        ac += 1
        a = i.split('|')
        for j in a:
            c = len(j)
            r = chr(c)
            ta.insert(tk.END, r)
    ta.delete('end-2c', tk.END)


def forcequit():
    sys.exit()


def killcommand():
    kill(getpid(), SIGKILL)


def autosave():
    global astv
    if fp != '' and asv.get():
        save()
    root.after(int(astv) * 1000, autosave)


def ast(time):
    global astv
    astv = time
    sm.entryconfig(12, label='当前间隔%d秒' % astv)


ta = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=100, height=40, font=('Arial', 15))
ta.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
mb = Menu(root)
fm = Menu(mb, tearoff=0)
fm.add_command(label='新建', command=new, accelerator='Command+N')
fm.add_command(label='打开', command=openfile, accelerator='Command+O')
fm.add_command(label='保存', command=save, accelerator='Command+S')
fm.add_command(label='移动', command=moveto)
fm.add_command(label='另存为', command=saveto)
fm.add_command(label='删除', command=delete)
mb.add_cascade(label='文件', menu=fm)
hm = Menu(mb, tearoff=0)
hm.add_command(label='一键打开urls', command=openurl)
hm.add_command(label='一键加密', command=tocode)
hm.add_command(label='一键解密', command=totext)
hm.add_command(label='毁文件[慎用!]', command=饿啊)
mb.add_cascade(label='工具', menu=hm)
sm = Menu(mb, tearoff=0)
asv = tk.BooleanVar(value=True)
astv = 20
sm.add_checkbutton(label='自动保存', variable=asv, command=autosave)
sm.add_command(label='设置间隔为1秒', command=lambda: ast(1))
sm.add_command(label='设置间隔为5秒', command=lambda: ast(5))
sm.add_command(label='设置间隔为10秒', command=lambda: ast(10))
sm.add_command(label='设置间隔为20秒', command=lambda: ast(20))
sm.add_command(label='设置间隔为60秒', command=lambda: ast(60))
sm.add_command(label='设置间隔为120秒', command=lambda: ast(120))
sm.add_command(label='设置间隔为180秒', command=lambda: ast(180))
sm.add_command(label='设置间隔为300秒', command=lambda: ast(300))
sm.add_command(label='设置间隔为600秒', command=lambda: ast(600))
sm.add_command(label='设置间隔为1200秒', command=lambda: ast(1200))
sm.add_command(label='设置间隔为3600秒', command=lambda: ast(3600))
sm.add_command(label='当前间隔%d秒' % astv, command=lambda: 0)
mb.add_cascade(label='自动保存', menu=sm)
om = Menu(mb, tearoff=0)
om.add_command(label='退出', command=safequit)
om.add_command(label='强制退出', command=forcequit)
om.add_command(label='结束进程', command=killcommand)
mb.add_cascade(label='选项', menu=om)
root.config(menu=mb)
root.bind('<Command-n>', new)
root.bind('<Command-o>', openfile)
root.bind('<Command-s>', save)
ta.bind('<FocusIn>', staw)
ta.bind('<FocusOut>', stow)
root.bind('<Key>', onkey)
root.protocol('WM_DELETE_WINDOW', safequit)
et()
autosave()
ta.insert(tk.END, '欢迎使用文本编辑!\n按command+n新建文件\n按command+o打开文件')
root.mainloop()
