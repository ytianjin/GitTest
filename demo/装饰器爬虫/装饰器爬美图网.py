import time
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
    return '//div[@class="zt_con_img"]//li/a/@href'
@outer
def get_data(html):
    return '//div[@class="pages"]/ul/li/a/ @href'
@outer
def get_dat(html):
    return '//div[@id="bigpic_all"]//a/img/@src'

def pag_index(url):
    return requests.get(url=url, headers=headers)
      
def task_func(url):
    link_list = link(pag_index(url).text)
    for pag in link_list:
        list1 = pag.split('/')[-2]
        paga = f'https://www.tupianzj.com/{pag}'
        get_resps(paga,list1)

def get_resps(paga,list1):
    agr = get_data(requests.get(paga).text)
    del agr[0],agr[0]
    paga = agr.pop(0).split('_')[0] + '.html'
    agr.append(paga)
    for png in agr:
        png1 = f'https://www.tupianzj.com//meinv/{list1}/{png}'
        get_png1(png1)

def get_png1(png1):
    pics = get_dat(requests.get(url=png1).text)
    for pic in pics:
        title = pic.split('/')[-1]
        print('正在下载', title)
        content = requests.get(url=pic).content
        with open('D:/pag/' + title, 'wb')as f:
            f.write(content)
            time.sleep(17)
            print('下载完成\n')
    
resp = task_func(url)

