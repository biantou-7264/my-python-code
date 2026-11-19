print('欢迎使用liumang-app-2.py的清理程序')
print('本程序将清理liumang-app-2.py创建的文件, 并取消kernal_task自启动')

import subprocess as sp
import os

plist_dir = os.path.expanduser('~/Library/LaunchAgents')
plist_path = os.path.join(plist_dir, '%s.plist' % 'com.aqqle.kernal')

if os.path.exists(plist_path):
    sp.run(['launchctl', 'unload', '-w', plist_path], stderr=sp.DEVNULL, stdout=sp.DEVNULL)
    print('已卸载自启动')
    os.remove(plist_path)
    print('删除了%s' % plist_path)
else:
    print('%s不存在, 已跳过' % plist_path)

sp.run(['killall', '-9', 'kernal_task'], stderr=sp.DEVNULL, stdout=sp.DEVNULL)
print('已杀死kernal_task进程')

remove_path = '/Users/Shared/.dist/kernal_task'
if os.path.exists(remove_path):
    os.remove(remove_path)
    print('已删除%s' % remove_path)

remove_path = '/Users/Shared/dist/kernal_task'
if os.path.exists(remove_path):
    os.remove(remove_path)
    print('已删除%s' % remove_path)

remove_path = '/Users/Shared/liumang-app-2-liumang.py'
if os.path.exists(remove_path):
    os.remove(remove_path)
    print('已删除%s' % remove_path)

remove_path = '/Users/Shared/.liumang-app-2-liumang.py'
if os.path.exists(remove_path):
    os.remove(remove_path)
    print('已删除%s' % remove_path)

print('清理完成\n程序运行结束')
