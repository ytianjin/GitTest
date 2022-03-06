import time
import requests
from lxml import etree
import threading
# from multiprocessing.dummy import Pool
# lock = threading.Lock()
def main():
    # lock.acquire()   
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    session = requests.Session()
    url = 'http://bbs.fengniao.com/forum/forum_101.html'
    response = session.get(url=url, headers=headers).text
    for tree in etree.HTML(response).xpath('//div[@class="bbsListAll bbsList  module1200 yinying clearfix"]//li//h3//a/@href'):
        datas = f'http://bbs.fengniao.com/{tree}'
        data = session.get(url=datas, headers=headers).text
        for tree in etree.HTML(data).xpath('//div[@class="img"]//a/img/@src'):
            t = threading.Thread(target=dowlond, args=(tree,))
            t.start()
            # for i in range(5):
            #     t = threading.Thread(target=dowlond,args=(tree,i))
            #     t.start()
            
def dowlond(tree):
    outer = requests.get(tree).content
    with open('D:/abc/%s.jpg'%time.time(), "wb")as f:
        f.write(outer)
        # lock.release()
        time.sleep(3)

if __name__ == '__main__':
    main()
    

        
