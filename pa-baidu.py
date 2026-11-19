import requests as rq

print('welcome!')
url = input('please input url:')

print(rq.__version__)
print('loading...')
res = rq.get(url)

res.encoding = res.apparent_encoding
content = res.text

try:
    with open('/Users/luojingfeng/Desktop/spider_res.html', 'w', encoding='utf-8') as file:
        file.write(content)
except BaseException as e:
    print(e)

print(content)
print('finish')
