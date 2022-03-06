import time
import requests
from lxml import etree

class Getmasge:

    def __init__(self):
        self.url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        }
    def get_page_index(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.encoding = response.apparent_encoding
        return response

    def get_png1(self,png1):
        agrs = requests.get(url=png1).text
        agr = etree.HTML(agrs)
        agr_url = agr.xpath('//div[@id="bigpic_all"]//a/img/@src')
        for agl in agr_url:
            title = agl.split('/')[-1]
            print('正在下载', title)
            content = requests.get(url=agl).content
            with open('D:/pag/' + title, 'wb')as f:
                f.write(content)
                time.sleep(17)
                print('下载完成\n')

    def get_resps(self,resp,list1):
        datas1 = requests.get(url = resp).text
        datas = etree.HTML(datas1)
        data = datas.xpath('//div[@class="pages"]/ul/li/a/ @href')
        del data[0],data[0]
        paga = data.pop(0).split('_')[0] + '.html'
        data.append(paga)
        for png in data:
            png1 = f'https://www.tupianzj.com//meinv/{list1}/{png}'
            self.get_png1(png1)

    def main(self):
        response = self.get_page_index().text
        resps = etree.HTML(response)
        resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
        for resp1 in resps1:
            list1 = resp1.split('/')[-2]
            resp = f'https://www.tupianzj.com/{resp1}'
            self.get_resps(resp,list1)
               # https://www.tupianzj.com/meinv/20211224/236579.html           

if __name__ =='__main__':
    getmasge = Getmasge()
    getmasge.main()