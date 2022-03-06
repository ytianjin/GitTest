import requests
from lxml import etree


url = 'http://www.netbian.com/2560x1440/index_3.htm'
response = requests.get(url=url)
reso = response.text
resp = etree.HTML(reso)
resps = resp.xpath('//div[@class="list"]//li/a/@href')
for soup in resps:
    soups = f'http://www.netbian.com{soup}'
    resp_1 = requests.get(url=soups)
    resp_1.encoding = resp_1.apparent_encoding
    resp_2 = etree.HTML(resp_1.text)
    title = resp_2.xpath('//div[@class="pic"]//a/img//@title')
    pics = resp_2.xpath('//div[@class="pic"]//a/img//@src')
    for title_1, pic in zip(title, pics):
        print('正在下载', title_1)
        pic_url = requests.get(url=pic).content
        with open('D:/pics/' + title_1, mode="wb") as f:
            f.write(pic_url)
            print('下载完成\n')




    """
  //div[@class="list"]//li/a/@href
  http://www.netbian.com/desk/23849.htm
    """