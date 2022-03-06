import requests
import time
import parsel

url = 'https://zhainima.com/sf'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get(url=url, headers=headers, timeout=10)
resps = response.text
selector = parsel.Selector(resps)
resps_1 = selector.xpath('//div[@class="post-module-thumb"]//a/@href').getall()
for resp in resps_1:
    pics = requests.get(url=resp, headers=headers).text
    pics1 = parsel.Selector(pics)
    pic1= pics1.xpath('//div[@class="entry-content"]//img/@src').getall()
    for pic in pic1:
        title = pic.split('/')[-1]
        print('正在下载', title)
        dic = requests.get(url=pic, headers=headers).content
        with open('D:/pic/' + title, mode="wb") as f:
            f.write(dic)
            time.sleep(5)
            print('下载完成\n')