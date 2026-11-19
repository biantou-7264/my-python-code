import requests
def test():
    wifi=False
    try:
        requests.get("https://www.baidu.com/",timeout=5)
        wifi=True
    except:
        pass
    try:
        if not wifi:
            requests.get("https://im.qq.com/index/#/",timeout=5)
            wifi=True
    except:
        pass
    try:
        if not wifi:
            requests.get("https://shequ.codemao.cn/",timeout=5)
            wifi=True
    except:
        pass
    try:
        if not wifi:
            requests.get("https://www.so.com/",timeout=5)
            wifi=True
    except:
        pass
    try:
        if not wifi:
            requests.get("https://www.python.org/",timeout=5)
            wifi=True
    except:
        pass
    return wifi
if __name__=='__main__':
    print(wifiTest())