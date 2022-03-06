import requests
from lxml import etree


url = url = 'https://www.tupianzj.com/meinv/mm/meituwang/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

def outer(fn):
        def inner(sex):
            tree = etree.HTML(fn)
            res = tree.xpath(sex)
            return res
        return inner

def link():
    return '//div[@class="zt_con_img"]//li/a/@href'


def pag_index():
    return requests.get(url=url, headers=headers).text

fn = outer(pag_index())
res = fn(link())
print(res)
