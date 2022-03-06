import requests
import re
import os
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10700255482569742856&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%B0%8F%E5%A7%90%E5%A7%90&queryWord=%E5%B0%8F%E5%A7%90%E5%A7%90&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1643277799787='

# Word = input('请输入关键字:')
# if not os.path.exists(Word):
#     os.mkdir(Word)
# page = int(input('请输入页数:'))


def get_img(url):
    response = requests.get(url=url, headers=headers)
    # response.encoding = response.apparent_encoding
    # content = response.content.decode('utf-8')
    json = response.json()
    datas= json['data']
    for data in datas:
        data_url = data['thumbURL']
        
    # for contents in content:
    #     img_urls = re.findall('"thumbURL" : "(.*?)"', contents, re.S)
        # print(img_urls)
    # for img_url in img_urls:
    #     response = requests.get(img_url, headers)
    #     content = response.content
    #     with open('{}.jpg'.format(i), 'wb')as f:
    #         f.write(content)

get_img(url)