# 从pyobjc导入AppKit模块  
from AppKit import NSApplication, NSWindow, NSButton, NSMakeRect  
import objc  
  
# 1. 获取应用程序实例  
app = NSApplication.sharedApplication()  
  
# 2. 创建一个窗口（设置位置、大小、样式等）  
window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(  
    NSMakeRect(500, 300, 400, 200),  # (x, y, width, height)  
    14,  # 窗口样式：有标题栏、可关闭、可最小化等  
    2,   # 缓冲类型  
    False  
)  
window.setTitle_('我的第一个AppKit程序')  
  
# 3. 创建一个按钮  
button = NSButton.alloc().initWithFrame_(NSMakeRect(150, 80, 100, 30))  
button.setTitle_('点击我！')  
button.setButtonType_(0)  # 按钮类型：瞬时按下  
  
# 定义按钮点击后要执行的函数  
def button_clicked_(sender):  
    window.setTitle_('你好，世界！')  
  
# 将按钮的点击动作连接到我们定义的函数  
button.setTarget_(app)  
button.setAction_(objc.selector(button_clicked_, signature=b'v@:'))  
  
# 4. 把按钮添加到窗口上  
window.contentView().addSubview_(button)  
  
# 5. 显示窗口并运行程序  
window.makeKeyAndOrderFront_(None)  
app.run()  
