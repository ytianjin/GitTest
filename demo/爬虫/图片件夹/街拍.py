import urllib.parse
import requests
import json
from urllib.parse import urlencode
import os
from hashlib import md5

def get_page_index(page_num):
        data = {'keyword': '街拍',
                'pd': 'atlas',
                'dvpf': 'pc',
                'aid': '4916',
                'page_num': 'page_num',
                'search_json': '{"from_search_id":"20220111195606010212022226567006A3","origin_keyword":"街拍","image_keyword":"街拍"}',
                'rawJSON': '1',
                'search_id': '2022011320204401015013613022BD51D4'

        }
        url = ' https://so.toutiao.com/search/?' + urlencode(data)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                'Cookie': '_S_DPR=1.5; _S_IPAD=0; MONITOR_WEB_ID=7051915685719098888; tt_webid=7051915969217021444; ttwid=1%7Cvhb1fdGcXV0WVCxdSdeiszWDkYY7-dU6xcJaLonxKgc%7C1641990020%7Ca995740a0b1dd76d64313dc77ce365aed3df24b645b35d7543dae8b63ba17e9a; _S_WIN_WH=291_569',
                'Host': 'so.toutiao.com',
                'Referer': 'https://so.toutiao.com/search?keyword=%E8%A1%97%E6%8B%8D&pd=atlas&dvpf=pc&aid=4916&page_num=0&search_json={%22from_search_id%22:%2220220111195606010212022226567006A3%22,%22origin_keyword%22:%22%E8%A1%97%E6%8B%8D%22,%22image_keyword%22:%22%E8%A1%97%E6%8B%8D%22}'
        }
        response = requests.get(url=url, headers=headers)
        return response.json()

def parse_page_index(json):
        images = json.get('rawData').get('data')
        for item in images:
                link = item.get('extra').get('download_url')
                title = item.get('text')
                yield {
                        'link' : link,
                        'title' : title,
                }


def saving_img(image):
        if not os.path.exists(image.get('title')):
                os.mkdir(image.get('title'))
                data = requests.get(image.get('link')).content
                file_path = '{0} / {1}.{2}' .format(image.get('title')),md5(data).hexdigest(),'jpg'
                with open(file_path, 'wb') as f:
                        f.write(data) 

def main(page_num):
        json = get_page_index(page_num)
        for imge in parse_page_index(json):
                saving_img(imge)


if __name__ == '__main__':
        for i in range(0,1):
                main(i)
        # print(response.text)
        # resp = json.loads(response)
        # resp1 = resp['rawData']['data']
        # for line in resp.get('data'):
        #         yield line.get('download_url')
        #         title = line['text']
        #         img_url = line['extra']['download_url']
        #         print(title)
        #         print(img_url)
