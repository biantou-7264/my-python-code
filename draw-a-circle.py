import pyautogui
import math
import time


def draw_circle(radius=200, duration=2, center_x=None, center_y=None):
    """
    使用pyautogui控制鼠标画圆

    参数:
        radius: 圆的半径（像素）
        duration: 画圆所需时间（秒）
        center_x: 圆心x坐标，None表示使用当前鼠标位置
        center_y: 圆心y坐标，None表示使用当前鼠标位置
    """

    # 如果没有指定圆心，使用当前鼠标位置
    if center_x is None or center_y is None:
        current_pos = pyautogui.position()
        center_x = current_pos.x
        center_y = current_pos.y

    # 计算需要移动的步数（点数越多，圆越平滑）
    steps = 500

    # 移动到起始点（圆的右侧起点）
    start_x = center_x + radius
    start_y = center_y
    pyautogui.moveTo(start_x, start_y, duration=0.1)

    # 按下鼠标左键开始绘制
    pyautogui.mouseDown()

    # 计算每个点之间的时间间隔
    interval = duration / steps

    # 画圆
    for i in range(steps + 1):
        # 计算角度（从0到2π）
        angle = 2 * math.pi * i / steps

        # 计算圆上的点坐标
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # 移动鼠标到计算的位置
        pyautogui.moveTo(x, y, duration=interval)

    # 释放鼠标左键
    pyautogui.mouseUp()


if __name__ == "__main__":
    pyautogui.PAUSE = 0
    # 画单个圆
    radius = 150  # 半径
    print("请在3秒内切换到绘图软件...")
    time.sleep(3)
    draw_circle(radius=radius, duration=0)
    print("画圆完成！")
