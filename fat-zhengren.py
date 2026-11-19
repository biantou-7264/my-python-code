# 发明者:biantou
# 发明项目:整人-胖
# 发明日期:2026年6月11日

# 这个项目会显示一个问胖不胖的界面
# 只要鼠标靠近“不胖”,这个“不胖”就会逃走,点到也没用
# “胖”可以点,点了会显示“没错”


mouse_x = 0
mouse_y = 0
no_fat_peng_mouse = False

import tkinter as tk
import math


def no_fat_run():
    coords = canvas.coords(no_fat)
    shape_x, shape_y = coords
    angle = get_angle(shape_x, shape_y)
    x, y = cal_angle_and_xy(angle, 5)
    for _ in range(20):  # 有一个移动动画
        canvas.move(no_fat, x, y * -1)
        root.update()
    coords = canvas.coords(no_fat)
    shape_x, shape_y = coords
    # 穿过边缘就回到中间
    if shape_x > 850:
        canvas.coords(no_fat, 400, 300)
    if shape_x < -50:
        canvas.coords(no_fat, 400, 300)
    if shape_y > 650:
        canvas.coords(no_fat, 400, 300)
    if shape_y < -50:
        canvas.coords(no_fat, 400, 300)


def mouse_move(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y


def get_angle(center_x, center_y):
    # 核心：算图形中心相对于鼠标的角度
    delta_x = center_x - mouse_x
    delta_y = center_y - mouse_y
    rad = math.atan2(delta_y, delta_x)
    angle = math.degrees(rad)
    # 返回正角度
    if angle < 0:
        angle += 360
    return angle


def cal_angle_and_xy(angle, distance):
    radian = math.radians(angle - 90)  # 获取弧度
    # 算公式
    dx = distance * math.cos(radian)
    dy = distance * math.sin(radian)
    return dx, dy


def no_fat_peng(event):  # nofat碰到鼠标
    global no_fat_peng_mouse
    no_fat_peng_mouse = True


def no_fat_nopeng(event):  # nofat没碰到鼠标
    global no_fat_peng_mouse
    no_fat_peng_mouse = False


def main_loop():
    if no_fat_peng_mouse:
        no_fat_run()
    root.after(10, main_loop)


def no_fat_click(event):
    no_fat_run()
    canvas.itemconfig(tip, text='加载失败!', fill='red')  # 点到也没用
    root.after(2000, tip_config_default)


def tip_config_default():
    canvas.itemconfig(tip, text='请选择', fill='black')


def fat_click(event):
    canvas.itemconfig(tip, text='加载成功!', fill='green')
    msg = tk.Toplevel(root)
    tk.Label(msg, bitmap='info').pack(anchor=tk.NW, padx=20, pady=20)
    tk.Label(msg, text='没错!\n你就是胖!', font=(None, 20), justify='left').pack(anchor=tk.NW, padx=20)
    tk.Button(msg, text='好的', command=msg.destroy, font=(None, 20), cursor='pointinghand').pack(side=tk.BOTTOM, pady=10)
    msg.geometry('600x400')


root = tk.Tk()
root.title('你胖不胖')

canvas = tk.Canvas(root, width=800, height=600, bg='#64c8ff')  # 天蓝色好看
canvas.pack()

title = canvas.create_text(400, 150, text='你胖不胖?', font=('Arial', 100, 'bold'), fill='black')
fat = canvas.create_text(200, 400, text='胖', font=('Arial', 100, 'bold'), fill='green')
no_fat = canvas.create_text(600, 400, text='不胖', font=('Arial', 100, 'bold'), fill='red')
tip = canvas.create_text(20, 550, text='请选择', font=('Arial', 30), anchor=tk.NW, fill='black')

canvas.tag_bind(no_fat, '<Enter>', no_fat_peng)
canvas.tag_bind(no_fat, '<Leave>', no_fat_nopeng)
canvas.tag_bind(no_fat, '<Button-1>', no_fat_click)
canvas.tag_bind(fat, '<Button-1>', fat_click)
canvas.bind('<Motion>', mouse_move)

root.after(100, main_loop)
root.focus_force()
root.mainloop()
