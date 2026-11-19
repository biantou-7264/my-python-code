import subprocess as sp
import tkinter as tk
import traceback
from datetime import datetime

check_timers = []


class WifiControler:
    def on(self, en):
        try:
            sp.run(['/usr/sbin/networksetup', '-setairportpower', en, 'on'])
        except Exception:
            print('\033[31m')
            print('[ERROR] on wifi failed!')
            print(traceback.format_exc())
            print('\033[0m')

    def off(self, en):
        try:
            sp.run(['/usr/sbin/networksetup', '-setairportpower', en, 'off'])
        except Exception:
            print('\033[31m')
            print('[ERROR] off wifi failed!')
            print(traceback.format_exc())
            print('\033[0m')

    def get(self, en):
        try:
            result = sp.run(['/usr/sbin/networksetup', '-getairportpower', en], capture_output=True, text=True)
            return 'On' in result.stdout
        except Exception:
            print('\033[31m')
            print('[ERROR] on wifi failed!')
            print(traceback.format_exc())
            print('\033[0m')
            return False


def check():
    if on.get():
        try:
            check_timers.append(root.after(4000, check))
            while True:
                if len(check_timers) > 1:
                    root.after_cancel(check_timers.pop(0))
                else:
                    break
            print('\033[34mchecking...\033[0m')
            wifi_status = wifi_controler.get(en.get())
            if not wifi_status:
                wifi_controler.on(en.get())
                print('\033[32mtry to on wifi\033[0m')
            last_check_time.set(get_time())
            print('\033[32mcheck-up time %s\033[0m' % last_check_time.get())
        except Exception:
            print('\033[31m')
            print('[ERROR] check failed!')
            print(traceback.format_exc())
            print('\033[0m')


def get_time():
    now = datetime.now()
    if now.hour < 10:
        hour = '0%d' % now.hour
    else:
        hour = str(now.hour)
    if now.minute < 10:
        minute = '0%d' % now.minute
    else:
        minute = str(now.minute)
    if now.second < 10:
        second = '0%d' % now.second
    else:
        second = str(now.second)
    return '%s:%s:%s' % (hour, minute, second)


def on_checkbutton_change():
    print('\033[34mon button checked\033[0m')
    if on.get():
        check_timers.append(root.after(10, check))
    print('\033[32mon status: %s\033[0m' % ('on' if on.get() else 'off'))


wifi_controler = WifiControler()

root = tk.Tk()
root.title('wifi watchdog')

on = tk.BooleanVar(value=True)
en = tk.StringVar(value='en0')
last_check_time = tk.StringVar(value='00:00:00')

tk.Label(root, text='wifi watchdog', font=('Arial', 30)).pack(padx=10, pady=10)
tk.Checkbutton(root, text='on', variable=on, font=('Arial', 20), command=on_checkbutton_change).pack(padx=10, pady=10, ipadx=40)
en_frame = tk.Frame(root)
tk.Label(en_frame, text='en:', font=('Arial', 20)).pack(padx=10, pady=10, side=tk.LEFT)
tk.Entry(en_frame, textvariable=en, font=('Arial', 20), highlightbackground='gray').pack(padx=10, pady=10, side=tk.LEFT)
en_frame.pack(padx=10, pady=10)
last_check_time_frame = tk.Frame(root)
tk.Label(last_check_time_frame, text='last check-up time: ', font=('Arial', 20)).pack(padx=10, pady=10, side=tk.LEFT)
tk.Label(last_check_time_frame, textvariable=last_check_time, font=('Arial', 20)).pack(padx=10, pady=10)
last_check_time_frame.pack(padx=10, pady=10)

root.after(10, check)
root.focus_force()
root.mainloop()
