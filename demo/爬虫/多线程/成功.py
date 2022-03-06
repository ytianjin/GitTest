import os
import time
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
if not os.path.exists('D:/蜂鸟网/'):
    os.mkdir('D:/蜂鸟网/')
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
def get_reques(url):
     response = requests.get(url=url, headers=headers)
     return response

def get_data(data):
    for tree in etree.HTML(data).xpath('//div[@class="bbsListAll bbsList  module1200 yinying clearfix"]//li//h3//a/@href'):
        tre = f'http://bbs.fengniao.com/{tree}'
        resp = requests.get(url = tre, headers=headers).text
        for tree in etree.HTML(resp).xpath('//div[@class="img"]//a/img/@src'):
            yield tree

def dowload(title, data):
    print('正在下载', title)
    with open('D:/蜂鸟网/' + title, "wb")as f:
        f.write(data)
        print('下载完成' + title,'\n')

def main():
    pool = ThreadPoolExecutor(max_workers=5)
    response = get_reques('http://bbs.fengniao.com/forum/forum_101.html')
    urls = get_data(response.text)
    for i, url in enumerate(urls):
        title = str(i) + '.jpg'
        resp = get_reques(url)
        pool.submit(dowload, title, resp.content)
    pool.shutdown()

if __name__ == '__main__':
    main()