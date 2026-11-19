from random import randint


def sort(arr):
    while True:
        length = len(arr)
        for i in range(length - 1):
            a = arr[i]
            b = arr[i + 1]
            if a > b:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        c = 0
        no = False
        for i in arr:
            if i >= c:
                c = i
            if i < c:
                no = True
        if not no:
            return arr


arr = []
for i in range(5000):
    arr.append(randint(0, 1000))
print(sort(arr))
