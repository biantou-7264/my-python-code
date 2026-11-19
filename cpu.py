from psutil import cpu_percent


def cpu(interval=0.5):
    res = cpu_percent(interval=interval)
    return res


def show_cpu(interval=0.5):
    print('按ctrl+c退出')
    try:
        while True:
            print('\r%.1f' % cpu(interval=interval), end='')
    except KeyboardInterrupt:
        print('\n已退出')


if __name__ == '__main__':
    show_cpu()
