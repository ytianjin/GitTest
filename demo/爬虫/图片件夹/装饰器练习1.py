import time
import re
import requests
from lxml import etree


url = 'https://www.27270.net/game/cosplaymeitu/'


def get_url(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
    response = requests.get(url=url, headers=headers)
    return response
resp1= 0
def get_resps(c,a):
    pags = requests.get(url=c).text
    html = etree.HTML(pags)
    datas = html.xpath(a)
    def inner():
        res = a()
        del datas[0],datas[0],datas[-1]
        data = datas.pop(0).split('_')[0] + '.html'
        datas.append(data)
        for pags1 in datas:
            pag = f'https://www.27270.net/game/cosplaymeitu/{resp1}/{pags1}'
            print(pag)
        # get_resp(c = pag,a = '//div[@class="articleV4Body"]/p/a/img/@src')
    return inner

def main():
    global resp1
    response = get_url(url).text
    resps = re.findall((r'<a href="(.*?)" title=.*? target="_blank">'), response)
    for resp in resps:
        resp1 = resp.split('/')[-2]
        get_resps(c = resp,a = '//div[@class="page-tag oh"]//a/@href')


main()

# get_resp(c = resp,a = '//div[@class="page-tag oh"]//a/@href')