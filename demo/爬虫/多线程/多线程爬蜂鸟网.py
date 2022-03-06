import time
import requests
from lxml import etree
from queue import Queue
from threading import Thread
# 多线程类
class Downlod_image(Thread):
    def __init__(self, queue, html_queue):
        Thread.__init__(self)
        self.queue = queue
        self.html_queue = html_queue
    def run(self):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
        while not self.queue.empty():
            url = self.queue.get()
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                self.html_queue.put(response.text)
class Downlod_html(Thread):
    def __init__(self, html_queue):
        Thread.__init__(self)
        self.html_queue = html_queue  
    def run(self):
        while not self.html_queue.empty():
        # e = self.html_queue.get()
            for tree in etree.HTML(self.html_queue.get()).xpath('//div[@class="bbsListAll bbsList  module1200 yinying clearfix"]//li//h3//a/@href'):
                data = f'http://bbs.fengniao.com/{tree}'
                url = requests.get(data).text
                for tree in etree.HTML(url).xpath('//div[@class="img"]//a/img/@src'):
                    outer = requests.get(tree).content
                    with open('D:/abc/%s.jpg'%time.time(), "wb")as f:
                        f.write(outer)
                        time.sleep(3)     

if __name__ == '__main__':
    queue= Queue()
    html_queue = Queue()
    url = 'http://bbs.fengniao.com/forum/forum_101.html'
    queue.put(url)
    list = []
    for i in range(0, 5):
        worker = Downlod_image(queue, html_queue)
        list.append(worker)
        worker.start()
    for i in list:
        i.join()
    list1 = []
    for i in range(0, 5):
        parse = Downlod_html(html_queue)
        list1.append(parse)
        parse.start()
    for i in list1:
        i.join() 

        


    