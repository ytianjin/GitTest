import time
import requests
from lxml import etree

url = 'https://www.3gbizhi.com/meinv/xgmn_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
            'Cookie': 'Hm_lvt_c8263f264e5db13b29b03baeb1840f60=1637669738; Hm_lpvt_c8263f264e5db13b29b03baeb1840f60=1637670372; _ga=GA1.2.1920652733.1637670374; _gid=GA1.2.577966964.1637670374'
}
response = requests.get(url=url, headers=headers)
resps = response.text
resps_1 = etree.HTML(resps)
datas = resps_1.xpath('//div[@class="contlistw mtw"]//li/a/@href')
for data in datas:
    try:
        pics_1 = requests.get(url=data, headers=headers).text
    except:
        continue
    pics_2 = etree.HTML(pics_1)
    pics = pics_2.xpath('//div[@class="picimglist pos"]//li/a/@href')
    for pic in pics:
        try:
            dics = requests.get(url=pic, headers=headers).text
        except:
            continue
        dicx = etree.HTML(dics)
        dics_1 = dicx.xpath('//div/a[@href="javascript:;"]/img/@src')
        for dic in dics_1:
            title = dic.split('/')[-1]
            print('正在下载', title)
            try:
                pic_url = requests.get(url=dic, headers=headers).content
            except:
                continue
            with open('D:/pics/' + title, mode="wb") as f:
                f.write(pic_url)
                print('下载完成\n')
                time.sleep(5)
