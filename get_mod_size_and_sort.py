import subprocess
import re

# 1. 调用pip获取所有已安装包的信息，用--format=freeze输出方便处理
result = subprocess.run(['pip', 'list', '--format=freeze'], capture_output=True, text=True)
packages = result.stdout.splitlines()
print('库读取成功,开始计算')

package_info = []
# 2. 逐个查每个包的安装大小
total_percent = len(packages)
for count, pkg in enumerate(packages):
    # 拆分包名，跳过空行
    if not pkg or '==' not in pkg:
        continue
    pkg_name = pkg.split('==')[0]

    # 调用pip show查看包详情，里面包含安装位置大小
    show_result = subprocess.run(['pip', 'show', pkg_name], capture_output=True, text=True)
    content = show_result.stdout

    # 提取大小信息（pip show里的Location是安装位置，我们算整个文件夹的大小）
    match_location = re.search(r'Location: (.*)', content)
    if match_location:
        location = match_location.group(1)
        # 计算文件夹总大小
        total_size = 0
        import os

        for dirpath, dirnames, filenames in os.walk(location):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
                # 转成更易读的MB单位
        size_mb = round(total_size / (1024 * 1024), 2)
        package_info.append((pkg_name, size_mb))
        percent = round((count / total_percent) * 100, 2)
        print(f'已计算:{pkg_name},当前进度{percent}%')

    # 3. 按照大小从大到小排序
package_info.sort(key=lambda x: x[1], reverse=True)

# 4. 输出结果
print("-" * 45)
print("已安装库 按大小从大到小排序：")
print(f"{'库名':<30} {'大小(MB)':>10}")
print("-" * 45)
for name, size in package_info:
    print(f"{name:<30} {size:>10}")
