import requests
from urllib.parse import urljoin
from lxml import etree

url = 'https://you.autohome.com.cn/summary/getsearchresultlist?ps=20&pg=0&type=4&q=%E6%B5%B7%E5%8D%97&dataType=4,9&_=1636183123404'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
'x-requested-with: XMLHttpRequest'}
response = requests.get(url=url, headers=headers)
resps = response.json()
for resp in resps['result'] ['hitlist']:
    resp_url = urljoin(url, resp['url'])
    resp_1 = requests.get(url=resp_url, headers=headers)
    dics_1 = etree.HTML(resp_1.text)
    dics = dics_1.xpath("//div//img/@data-original")
    for dic in dics:
        title = dic.split('/')[-1]
        print('正在下载', title)
        try:
            pic = requests.get(url=dic, headers=headers).content
        except:
            continue
        with open('D:/pics/' + title, mode="wb") as f:
            f.write(pic)
            print('下载完成\n')







    """
    //div[@class="image-wrap"]//img/@src/data-original
    https://you.autohome.com.cn/details/pc/tobigpic?tripId=80930&journeyId=b9199a93ef727b4de520c0aca8bfef59&tabIndex=1&seriesId=4648
    https://img2.autoimg.cn/travelplat/g28/M03/94/03/1185x0_1_autohomecar__ChsEnl3iNiWAAv63ACOlMBZR__g480.jpg
    https://img2.autoimg.cn/travelplat/g28/M03/94/03/ChsEnl3iNiWAAv63ACOlMBZR__g480.jpg
    """