import pyautogui as pag

pag.size()
pag.PYAUTOGUI_UI_SCALE = 2
pag.sleep(2)

pos = pag.locateCenterOnScreen('/Users/luojingfeng/Desktop/ScreenShot_2026-06-11_183454_274.png', confidence=0.8)
print(pos)
pag.click(pos.x / 2, pos.y / 2)