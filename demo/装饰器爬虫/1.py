import requests
from lxml import etree


url = url = 'https://www.tupianzj.com/meinv/mm/meituwang/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}



def outer(fn):
    def inner(html):
        tree = etree.HTML(html)
        res = tree.xpath(fn(html))
        return res
    return inner

@outer
def link(html):
    return  '//div[@class="zt_con_img"]//li/a/@href'    #'//div[@class="zt_con_img"]//li/a/@href'



def pag_index(url):
    return requests.get(url=url, headers=headers)
    
def task_func(url):
    link_list = link(pag_index(url).text)      # resps = etree.HTML(response)
    print(link_list)                         #   resps1 = resps.xpath('//div[@class="zt_con_img"]//li/a/@href')
    

resp = task_func(url)