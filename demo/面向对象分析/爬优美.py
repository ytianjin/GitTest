
import time
from copy import copy
import time
import requests
from lxml import etree
#   //div[@class="TypeList"]//li/a/@href        https://www.umeitu.com/meinvtupian/meinvzipai/242823.htm    NewPages

class Masges:
    def __init__(self):
        self.url = 'https://www.umeitu.com/meinvtupian/meinvzipai/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }

    def get_url(self):
        response = requests.get(url=self.url, headers=self.headers).text
        # tree = etree.HTML(response).xpath('//div[@class="TypeList"]//li/a/@href')
        for tree in etree.HTML(response).xpath('//div[@class="TypeList"]//li/a/@href'):
            data = f'https://www.umeitu.com{tree}'
            self.get_data(data)

    def get_data(self,data):
        resps = requests.get(url=data).text
        tree = etree.HTML(resps).xpath('//div[@class="NewPages"]//a/@href')
        tre = copy(tree)[0]
        tad = tre.split('_')[0] + '.htm'  
        tree.insert(0,tad)  # insert  插入    clear() 方法清空列表
        # tree.append(tad)
        for agr in tree:
            pics = f'https://www.umeitu.com{agr}'
            self.doanlons(pics)

    def doanlons(self,pics):
        res = requests.get(url=pics).text
        # etree.HTML(res).xpath('//p/a/img/@src')
        # etree.HTML(res).xpath('//p/img/@src')
        for tree in etree.HTML(res).xpath('//p//img/@src'):
            title = tree.split('/')[-1]
            print('正在下载', title)
            pic = requests.get(url=tree).content
            with open('D:/youmei/' + title, "wb")as f:
                f.write(pic)
                time.sleep(7)
                print('下载完成\n')

if __name__ == '__main__':
    masges = Masges()
    masges.get_url()


    # http://kr.shanghai-jiuxin.com/file/2022/0102/6175ccfe49bac6b1c831944e7958ab40.jpg