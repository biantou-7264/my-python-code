from time import time

btime = time()
fps = 0
while True:
    fps += 1
    if time() - btime > 1:
        print(fps)
        btime = time()
        fps = 0