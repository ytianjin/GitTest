import requests
from lxml import etree

url = 'https://movie.douban.com/chart'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = requests.get(url=url, headers=headers).text
title_url = etree.HTML(response).xpath('//td/a/@href')
title = etree.HTML(response).xpath('//td/a/@title')
title_text = etree.HTML(response).xpath('//p[@class="pl"]//text()')
# agr = [i for i in [i.strip() for i in title_text]if i !='']
for agr, tada, aga in zip(title,title_url,title_text):
    print(agr,tada,aga) 

# /html/body/div[3]/div[1]/div/div[1]/div/div/table[2]/tbody/tr/td[2]/div/p/text()      //div//tbody//p//text()
# //*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/p/text()        //p[@class="pl"]/p/text()