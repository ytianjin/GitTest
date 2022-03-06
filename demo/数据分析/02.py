import requests

url = 'https://ys.endata.cn/enlib-api/api/home/getrank_mainland.do'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
data = {
    'r': '0.4165262514988455',
    'top': '50',
    'type': '0'
}
response = requests.post(url=url, headers=headers, data=data).json()
datas = response['data']['table0']
for data in datas:
    title = data['MovieName']
    title1 = data['MovieName']
    title_time = data['ReleaseTime']
    piaofan = data['BoxOffice']
    piaojia = data['AvgBoxOffice']
    yusu = data['AvgBoxOffice']
    
    datas = title1, title_time, piaofan, piaojia, yusu
    datas1 = str(datas).replace('(', '').replace(')', '').replace(':', '')
    with open("中国票房榜.csv", mode="a", encoding= 'utf-8')as f:
        f.write(str(datas1).replace("'", '') + '\n')