import os, subprocess
from time import sleep

apps = []


def find_app(folder):
    apps = []
    for root, subs, files in os.walk(folder):
        for name in subs:
            if name.endswith('.app'):
                path = os.path.join(root, name)
                apps.append(path)
    return apps


for path in find_app('/Applications'):
    apps.append(path)
for path in find_app('/System/Applications'):
    apps.append(path)

print('已加载所有软件:')
for app in apps:
    print(app)
print('免责声明:运行本程序后造成的一切损失由使用者承担!')
input('按回车开始')

for count in range(3, -1, -1):
    print(count)
    sleep(1)

print('开始!')

for app in apps:
    try:
        res = subprocess.run(['open', app])
        print('打开%s完成,退出代码%d' % (app, res.returncode))
        sleep(0.5)
    except BaseException as e:
        print('%s打开失败:%s:%s' % (app, type(e).__name__, e))
