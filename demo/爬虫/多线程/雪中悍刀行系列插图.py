import time
import os
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


# https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837
if not os.path.exists('D:/多线程异步/'):
    os.mkdir('D:/多线程异步/')
headers = {
    'Host': 'www.zcool.com.cn',
    'Referer': 'https://www.zcool.com.cn/work/ZMjU4MjMzNDg=html.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
session = requests.Session()

def get_url(url):
    response = session.get(url=url, headers=headers)
    return response


def get_data(data):
    datas = data['data']['allImageList']
    for data in datas:
        data_url = data['url']
        yield data_url

def dowloand(title, data):
    print('正在下载', title)
    url = session.get(url=data).content
    with open('D:/多线程异步/' + title, 'wb')as f:
        f.write(url)
        print('下载完成\n')


def main():
    pool = ThreadPoolExecutor(max_workers=5)
    response = get_url('https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837')
    datas = get_data(response.json())
    for i, data in enumerate(datas):
        title = str(i) + '.jpg'
        pool.submit(dowloand, title, data)
    pool.shutdown()   

if __name__ == '__main__':
    main()