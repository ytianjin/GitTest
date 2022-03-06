import requests
from lxml import etree
import re


url = 'https://desk.zol.com.cn/meinv/'
headers = {'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
resps_1 = requests.get(url=url)
resps_2 = etree.HTML(resps_1.text)
resps = resps_2.xpath('//div//li[@class="photo-list-padding"]//a/@href')
for resp in resps:
    data_1 = f'https://desk.zol.com.cn{resp}'
    try:
        data_2 = requests.get(url=data_1)
    except:
        continue
    datas_1 = etree.HTML(data_2.text)
    datas = datas_1.xpath('//div[@class="photo-set-list"]//li/a/@href')
    for data in datas:
        soups_1 = f'https://desk.zol.com.cn/{data}'
        soups_2 = requests.get(url=soups_1).text
        data_1 = re.findall('<img id="bigImg" src="(.*?)" width', soups_2)
        for pics in data_1:
            title = pics.split('/')[-1]
            print('正在下载', title)
            pic = requests.get(url=pics).content
            with open('D:/pics/' + title, mode="wb") as f:
                f.write(pic)
                print('下载完成\n')