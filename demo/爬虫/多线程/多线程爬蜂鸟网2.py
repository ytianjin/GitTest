import time
import requests
from lxml import etree
from queue import Queue
from threading import Thread

# 多线程类
class Downlod_image(Thread):
    # 重写构造函数
    def __init__(self, queue):
        # 需要重新调用多线程类中的初始化方法
        Thread.__init__(self)
        # 创建类属性
        self.queue = queue
            # 重写run方法    
    def run(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
        url = self.queue.get()
        session = requests.Session()
        response = session.get(url=url, headers=headers).text
        for tree in etree.HTML(response).xpath('//div[@class="bbsListAll bbsList  module1200 yinying clearfix"]//li//h3//a/@href'):
            datas = f'http://bbs.fengniao.com/{tree}'
            data = session.get(url=datas, headers=headers).text
            for tree in etree.HTML(data).xpath('//div[@class="img"]//a/img/@src'):
                outer = session.get(tree).content
                with open('D:/abc/%s.jpg'%time.time(), "wb")as f:
                    f.write(outer)
                    time.sleep(3)

if __name__ == '__main__':
    queue= Queue()
    url = 'http://bbs.fengniao.com/forum/forum_101.html'
    queue.put(url)
    for x in range(5):
        worker = Downlod_image(queue)
        worker.start()