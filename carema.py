import minicv as cv

cap = cv.cap()

while True:
    cap.fast_show('cap')
    if cap.readkey(27):
        break

cap.close()
