import os, subprocess

root_path = '/Users/luojingfeng/Desktop/test'

for i in range(1, 10):
    os.mkdir(os.path.join(root_path, str(i)))
    for j in range(1, 10):
        path = os.path.join(root_path, str(i))
        os.mkdir(os.path.join(path, str(j)))
    for j in range(1, 10):
        for k in range(1, 10):
            path = os.path.join(root_path, str(i), str(j))
            os.mkdir(os.path.join(path2, str(k)))
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                path = os.path.join(root_path, str(i), str(j), str(k))
                os.mkdir(os.path.join(path3, str(l)))

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if i != 7 and j != 2 and k != 6 and l != 4:
                    with open(os.path.join(root_path, str(i), str(j), str(k), str(l), '密码错误'), 'w') as file:
                        file.write('密码错误')

subprocess.run(['tree', root_path])
