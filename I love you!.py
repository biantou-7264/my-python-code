import colortext as ct
from time import sleep

while True:
    for i in ct.colors.keys():
        print(ct.change('\rI love you!', i), end='')
        sleep(0.5)
