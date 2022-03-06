import time
import re
import requests
from lxml import etree


def get_page_index(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    response1 = response.text
    return response1

def get_resps(response1):
    resps = etree.HTML(response1)
    resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
    for resp1 in resps1:
        resp = f'https://www.tupianzj.com/{resp1}'
        get_datas(resp)
        
        

def get_datas(resp): 
        datas1 = requests.get(url = resp).text
        datas = etree.HTML(datas1)
        data = datas.xpath('//div[@class="pages"]/ul/li/a/ @href')
        print(data)


def main():
    url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
    response1 = get_page_index(url)
    resp = get_resps(response1)
    
main()

# //div[@class="zt_con_img"]//li/a/@href
# /html/body/div[2]/div/div/div[2]/div[2]/div[3]/ul/li[4]/a
# //div[@class="pages"]/ul/li/a/@href