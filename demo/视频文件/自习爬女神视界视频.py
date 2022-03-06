import re
import time
import requests
import parsel

url = 'https://www.520mmtv.com/hd/rewu.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get(url=url, headers=headers)
resps = response.text
selector = parsel.Selector(resps)
lists = selector.xpath('//li[@class="i_list list_n2 cxudy-list-formatvideo"]/a/@href').getall()
for list in lists:
    pics = requests.get(url=list, headers=headers).text
    videos = re.findall('url: "(.*?)"',pics)
    for video in videos:
        title = video.split('/')[-1]
        print('正在下载',title)
        vide = requests.get(video).content
        with open('D:/mp4/' + title, mode="wb") as f:
            f.write(vide)
            print('下载完成\n',title)
            time.sleep(5)