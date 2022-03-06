import requests
from lxml import etree

class GetMsge():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    url = 'https://www.tupianzj.com/meinv/mm/meituwang/'

    def get_url(self):
        self.response = requests.get(url=self.url, headers=self.headers).text
        tree = etree.HTML(self.response)
        lin = tree.xpath('//div[@class="zt_con_img"]//li/a/@href')
        pic = ('https://www.tupianzj.com%s' % agr for agr in lin)

getmsg = GetMsge()
getmsg.get_url()
