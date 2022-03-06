import time
import requests
from lxml import etree
from requests.api import post

url = 'https://www.pearvideo.com/category_6'
response = requests.get(url)
html = response.text
resps = etree.HTML(html)
resps_1 = resps.xpath('//div[@class="vervideo-bd"]/a/@href')
for resp in resps_1:
    resp_1 = resp.split('_')[-1]
   # datas_1 = f'https://www.pearvideo.com/videoStatus.jsp?contId={resp_1}'
    datas_1 = 'https://www.pearvideo.com/videoStatus.jsp?contId=%s' % resp_1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                'Referer': 'https://www.pearvideo.com/video_%s' % resp_1
    }
    data_2 = requests.get(url=datas_1, headers=headers).json()
    soups = data_2['videoInfo']['videos']['srcUrl']
    cont = 'cont-' + resp_1
    soups_1 = soups.replace(soups.split('-')[0].split('/')[-1], cont)
    name = soups_1.split('/')[-1]
    print('正在下载',name)
    soup = requests.get(soups_1).content
    with open("D:/pics/" + name, mode="wb") as f:
          f.write(soup)
          print('下载完成\n',name)
          time.sleep(5)