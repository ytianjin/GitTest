import time
import re
import requests
from lxml import etree

url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
def outer(func):  #(1)
    def inner():   #(4)
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        response1 = response.text
        print(response1)
        # print('1,2,3')  #（6）
        r = func()      #（8）
        # datas1 = requests.get(url = resp).text
        # datas = etree.HTML(datas1)
        # data = datas.xpath('//div[@class="pages"]/ul/li/a/ @href')
        # print(data)
        print('4,5,6')  #（10 ）
        return r       #（9）
    return inner()  #(5)

@outer              # (2)
def f1(response1):  #(3)
    resps = etree.HTML(response1)
    resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
    for resp1 in resps1:
        resp = f'https://www.tupianzj.com/{resp1}'
        print(resp)          
    # print('0,0,0')  #（7）