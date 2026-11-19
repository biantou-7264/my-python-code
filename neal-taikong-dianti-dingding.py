import pyautogui as pag

pag.sleep(3)

for _ in range(10):
    pag.scroll(1000)

while True:
    pag.scroll(-200)
    pag.scroll(1000)
