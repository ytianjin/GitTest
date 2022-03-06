import time
import re
import requests
from lxml import etree

url = 'https://www.27270.net/game/cosplaymeitu/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    
}
sess = requests.Session()
response = sess.get(url=url, headers=headers).text
tree = etree.HTML(response).xpath('//ul[@class="pic_list"]/li/a/@href')
