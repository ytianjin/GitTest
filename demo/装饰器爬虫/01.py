from pydoc import html
import requests
from lxml import etree


url = url = 'https://www.tupianzj.com/meinv/mm/meituwang/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
def outer(func):
    a = '//div[@class="zt_con_img"]//li/a/@href'
    def inner():
        tree = etree.HTML(func)
        
        res = tree.xpath(a)
        return res
    return inner

def pag_index(html):
    return requests.get(url=url, headers=headers).text

agr = outer(pag_index(html))
lin = agr()
for i in lin:
    data = f'https://www.tupianzj.com{i}'
    print(data)
