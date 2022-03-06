import requests
from lxml import etree

url = 'https://www.kanxiaojiejie.com/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
resps = etree.HTML(response.text)
dics = resps.xpath('//div//a[@class="entry-thumbnail"]/@href')
for dic in dics:
    resp_1 = requests.get(url=dic, headers=headers).text
    dics_1 = etree.HTML(resp_1)
    pics = dics_1.xpath('//div[@class="entry themeform"]//p/img/@src')
    for pic in pics:
        title = pic.split('/')[-1]
        print('正在下载', title)
        pic_1 = requests.get(url=pic, headers=headers).content
        with open('D:/pics/' + title, mode="wb") as f:
            f.write(pic_1)
            print('下载完成\n')