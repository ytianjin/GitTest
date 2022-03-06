import time
import re
import requests
from lxml import etree

url = 'https://www.27270.net/game/cosplaymeitu/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
resp = 0
resp1 = 0
def func():
    # print('我是func函数')   # 等二步打印:我是func函数
    pags = requests.get(url=resp).text
    html = etree.HTML(pags)
    datas = html.xpath('//div[@class="page-tag oh"]//a/@href')
    del datas[0],datas[0],datas[-1]
    data = datas.pop(0).split('_')[0] + '.html'
    datas.append(data)
    for pags1 in datas:
        pag = f'https://www.27270.net/game/cosplaymeitu/{resp1}/{pags1}'
        print(pag)
    value = (11,22,33,44)   # 等三步打印:11,22,33,44
    return value

def outer(a):   # 这里给予一个a的形参也是:func = outer(func)传递func的函数进去 
    global resp1, resp
    # print("before")     # 等一步打印:before
    response = requests.get(url=url, headers=headers).text
    resps = re.findall((r'<a href="(.*?)" title=.*? target="_blank">'), response)
    for resp in resps:
        print(resp)
        print('----------')
        resp1 = resp.split('/')[-2]
    def inner():
        res = a()   # 这里相当于是调用了func的函数
        print("after")
        return res
        
    return inner

func = outer(func)

result = func()
print(result)