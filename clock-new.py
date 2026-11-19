# 这是一个时钟项目
# 制作者:biantou
# 制作日期:2026/5/22
# 特别鸣谢:DeepSeek(AI)
import tkinter as tk
from datetime import datetime
import math
from tkinter import messagebox as mb

# <-----设置区----->
# 设置报时功能
# 说明:True可以设置开启,False可以设置关闭
report_time = True


# -----------------


def get_time():  # 获取时间
    now = datetime.now()
    return now.hour, now.minute, (now.microsecond / 1000 / 1000) + now.second


def draw():  # 绘制界面
    global line_hour, line_min, line_sec, hour, minute, second, time_text
    hour, minute, second = get_time()  # 先获取一下时间
    if minute == 0 and math.floor(second) == 0 and report_time:  # 报时检测
        mb.showinfo('提示', '现在是%s(%d)点整' % (time_to_text[int(hour)], hour))  # 显示提示
    # 删除旧图形
    canvas.delete(line_hour)
    canvas.delete(line_min)
    canvas.delete(line_sec)
    canvas.delete(time_text)
    # 绘制时针
    angle = (hour * 30) + (minute * 0.5) + (second * 0.00833333333333333333)
    x, y = calculation_angle_xy(angle, 250, 250, 100)
    line_hour = canvas.create_line(250, 250, x, y, width=5, fill='white')
    # 分针
    angle = (minute * 6) + (second * 0.1)
    x, y = calculation_angle_xy(angle, 250, 250, 150)
    line_min = canvas.create_line(250, 250, x, y, width=5, fill='white')
    # 秒针
    angle = second * 6
    x, y = calculation_angle_xy(angle, 250, 250, 200)
    line_sec = canvas.create_line(250, 250, x, y, width=5, fill='white')
    # 时间文字
    time_text = canvas.create_text(250, 540, text='%s:%s:%s' % format_time(hour, minute, second), font=('Arial', 70), fill='white', anchor='center')
    root.after(10, draw)  # 重新绘制


def calculation_angle_xy(angle, start_x, start_y, length):  # 计算线条结束xy
    # 说明:本函数由AI生成
    angle_rad = math.radians(angle - 90)
    end_x = start_x + length * math.cos(angle_rad)
    end_y = start_y + length * math.sin(angle_rad)
    return end_x, end_y


def format_time(hour, minute, second):  # 格式化显示时间
    hour = str(hour)
    minute = str(minute)
    second = str(math.floor(second))

    # 此处可以把一位数字前面加上0,比如6变成06
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second

    return hour, minute, second


hour, minute, second = get_time()
root = tk.Tk()
root.title('时钟')

canvas = tk.Canvas(root, width=500, height=600, bg='black')
canvas.pack()

clock_face = canvas.create_oval(20, 20, 480, 480, width=5, fill='black', outline='white')  # 钟面
clock_center_circle = canvas.create_oval(240, 240, 260, 260, width=0, fill='white')  # 钟中间那个圆形
numbers = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 这里手动写了一个钟上的文字列表
time_to_text = ['半夜十二点', '凌晨一点', '凌晨二点', '凌晨三点', '凌晨四点', '早上五点', '早上六点', '早上七点', '早上八点', '早上九点', '早上十点', '中午十一点', '中午十二点', '下午一点', '下午二点', '下午三点', ' 下午四点', '下午五点', '傍晚六点', '晚上七点', '晚上八点', '晚上九点', '晚上十点', '晚上十一点']  # 把数字转换成文字的列表
for angle, text in enumerate(numbers):  # 创建钟上面的字
    x, y = calculation_angle_xy(angle * 30, 250, 250, 200)
    canvas.create_text(x, y, text=str(text), font=('Arial', 30), fill='white')

for angle in range(60):  # 创建刻度
    x, y = calculation_angle_xy(angle * 6, 250, 250, 220)
    canvas.create_text(x, y, text='·', font=('Arial', 30), fill='white')

# 时针
angle = (hour * 30) + (minute * 0.5) + (second * 0.00833333333333333333)
x, y = calculation_angle_xy(angle, 250, 250, 100)
line_hour = canvas.create_line(250, 250, x, y, width=5, fill='white')
# 分针
angle = (minute * 6) + (second * 0.1)
x, y = calculation_angle_xy(angle, 250, 250, 150)
line_min = canvas.create_line(250, 250, x, y, width=5, fill='white')
# 秒针
angle = second * 6
x, y = calculation_angle_xy(angle, 250, 250, 200)
line_sec = canvas.create_line(250, 250, x, y, width=5, fill='white')
# 时间文字
time_text = canvas.create_text(250, 540, text='%s:%s:%s' % format_time(hour, minute, second), font=('Arial', 70), fill='white', anchor='center')

root.focus_force()
root.after(100, draw)  # 开始绘制

root.mainloop()
