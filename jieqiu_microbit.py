from microbit import *  # noqa
import music, random

bx = 2
sound = True
sco = 0
bright = 9

for _ in range(10):
    sleep(100)
    if button_a.is_pressed():
        music.pitch(1000, 100)
        while True: sleep(60000)

music.pitch(1000, 1000)

while True:
    x = random.randint(0, 4)
    display.set_pixel(bx, 4, bright)
    for y in range(5):
        if y > 0:
            display.set_pixel(x, y - 1, 0)
        display.set_pixel(x, y, bright)
        for _ in range(50):
            sleep(10)
            if button_a.is_pressed() and bx > 0:
                display.set_pixel(bx, 4, 0)
                bx -= 1
                display.set_pixel(bx, 4, bright)
                sleep(100)
            if button_b.is_pressed() and bx < 4:
                display.set_pixel(bx, 4, 0)
                bx += 1
                display.set_pixel(bx, 4, bright)
                sleep(100)
            if accelerometer.is_gesture('shake'):
                display.clear()
                if sound: music.pitch(1000, 200)
                img = '00000:0%d0%d0:0%d0%d0:0%d0%d0:00000' % (bright, bright, bright, bright, bright, bright)
                display.show(Image(img))
                while not button_a.is_pressed() and not button_b.is_pressed():
                    sleep(6)
                sleep(300)
                if pin_logo.is_touched():
                    music.pitch(1000, 10)
                    if button_a.is_pressed():
                        if bright == 0:
                            bright = 9
                        else:
                            bright -= 1
                        music.pitch(600, 100)
                    if button_b.is_pressed():
                        music.pitch(600, 100)
                        sound = not sound
                display.clear()
                if sound: music.pitch(1000, 200)
                display.set_pixel(bx, 4, bright)
    if bx == x:
        sco += 1
        if sound:
            music.pitch(1000, 100)
    else:
        if sound:
            music.pitch(600, 100)
    sleep(100)
    display.clear()
