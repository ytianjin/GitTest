import requests
import re


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url= 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9457410969052072209&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%B0%8F%E5%A7%90%E5%A7%90&queryWord=%E5%B0%8F%E5%A7%90%E5%A7%90&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1643592671623='

def get_img(url):
    response = requests.get(url=url, headers=headers)
    json = response.json()
    datas= json['data']
    for data in datas:
        data_url = data['thumbURL']
        title = data_url.split('=')[-4] + '.jpeg'
        print('正在下载',title)
        response1 = requests.get(data_url).content
        with open('D:/pic/' + title, 'wb')as f:
            f.write(response1)
            print('下载完成\n')
get_img(url)

# https://img0.baidu.com/it/u=2227360062,66971942&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500