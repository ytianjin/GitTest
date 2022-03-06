from encodings import utf_8
import requests
import re
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


# word = input('请输入关键字:')
# if not os.path.exists(word):
#     os.mkdir(word)
# page = int(input('请输入页数:'))

url= 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9457410969052072209&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%B0%8F%E5%A7%90%E5%A7%90&queryWord=%E5%B0%8F%E5%A7%90%E5%A7%90&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=30&rn=30&gsm=1e&1643592671623='

def get_img(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = utf_8
    resps =response.text
    resp = re.findall(r'"thumbURL":"(.*?)",', resps)
    print(resp)
    # datas= json['data']
    # for data in datas:
    #     title = data['fromPageTitleEnc']
    #     data_url = data['thumbURL']
    #     print(title)
    #     print(data_url)
        



get_img(url) 