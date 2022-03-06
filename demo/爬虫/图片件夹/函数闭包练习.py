from pickle import POP
import time
import re
import requests
from lxml import etree

url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
def get_page_index(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    return response
# list = []
def get_resps(resp):
    datas1 = requests.get(url = resp).text
    datas = etree.HTML(datas1)
    data = datas.xpath('//div[@class="pages"]/ul/li/a/ @href')
    del data[0],data[0]
    paga = data.pop(0).split('_')[0] + '.html' 
    data.append(paga) 
    # list.append(data)
    # print(list[-1][-1])



def main():
    response = get_page_index(url).text
    resps = etree.HTML(response)
    resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
    for resp1 in resps1:
        resp = f'https://www.tupianzj.com/{resp1}'
        get_resps(resp)

main()


"""
https://www.tupianzj.com/meinv/20220113/237116_2.html
https://www.tupianzj.com/meinv/20211208/236057_2.html
"""