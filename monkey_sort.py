import random

arr = []


def sort():
    global arr
    while True:
        random.shuffle(arr)
        no = False
        c = 0
        for i in arr:
            if i >= c:
                c = i
            if i < c:
                no = True
                break
        if not no:
            return


def create_arr(maxnum, listlen):
    global arr
    arr = []
    for _ in range(listlen):
        arr.append(random.randint(0, maxnum))


create_arr(int(input('maxnum:')), int(input('listlen:')))
sort()
print(arr)
