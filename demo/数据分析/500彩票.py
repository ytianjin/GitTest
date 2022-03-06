from urllib import response
import requests
from lxml import etree

def index(response):
    url = 'https://datachart.500.com/dlt/history/history.shtml'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers).text
    return response
def td(response):  
    td = [i.text for i in etree.HTML(index(response)).xpath('//tbody[@id="tdata"]//tr//td[@class="t_tr1"]')]
    x = 8
    for i in range(0,240,8):
        with open("lst.csv", mode="a")as f:
            f.write(str(td[i:x]).replace('[', '').replace(']', '').replace("'", ''))
            f.write('\n')
            x +=8

def td1(response):
    td1 = [i.text for i in etree.HTML(index(response)).xpath('//tbody[@id="tdata"]//tr//td[@class="cfont2"]')]
    x = 5
    for i in range(0,150,5):
        with open("lst1.csv", mode="a")as f:
            f.write(str(td1[i:x]).replace('[', '').replace(']', '').replace("'", ''))
            f.write('\n')
            x +=5
def td2(response):
    td2 = [i.text for i in etree.HTML(index(response)).xpath('//tbody[@id="tdata"]//tr//td[@class="cfont4"]')]
    x = 2
    for i in range(0,60,2):
        with open("lst2.csv", mode="a")as f:
            f.write(str(td2[i:x]).replace('[', '').replace(']', '').replace("'", ''))
            f.write('\n')
            x +=2
td(response)
td1(response)
td2(response)
