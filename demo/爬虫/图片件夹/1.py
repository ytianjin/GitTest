import time
import re
from urllib import response
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
    lists = []
    resps = etree.HTML(response1)
    resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
    for resp1 in resps1:
        resp = f'https://www.tupianzj.com/{resp1}'
        lists.append(resp)
        

# def get_datas(resp):
#     for respg in resp:
#         datas1 = requests.get(url = respg).text
#         datas = etree.HTML(datas1)
#         data = datas.xpath('//div[@class="pages"]/ul/li/a/@href')
#         print(data)


def main():
    url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
    response1 = get_page_index(url)
    lists = get_resps(response1)
    print(lists)
    # get_datas(resp)
main()