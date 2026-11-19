import subprocess as sp
from time import sleep

a = 'Finder,Dock,SystemUIServer,ControlCenter,WindowManager,NotificationCenter,MenuBarAgent'.split(',')

while True:
    for i in a:
        try:
            sp.run(['killall', i])
        except Exception:
            pass
    sleep(1)
