import time
import re
from urllib import response
import requests
from lxml import etree

url = 'https://www.27270.net/game/cosplaymeitu/'
datas = []
def get_page_index(url):
  headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
  }
  response = requests.get(url=url, headers=headers).text 
  return response

def get_resps(resps):
    # response = get_page_index(url)
    # resps = re.findall((r'<a href="(.*?)" title=.*? target="_blank">'), response)
    for resp in resps:
            pags = requests.get(url=resp).text
            html = etree.HTML(pags)
            datas = html.xpath('//div[@class="page-tag oh"]//a/@href')
            del datas[0],datas[0],datas[-1]
            data = datas.pop(0).split('_')[0] + '.html'
            datas.append(data)
            # print(datas)
            # a =list(map(str,datas))
            # print(a)
        #     for pags1 in datas:
        #         pag = f'https://www.27270.net/game/cosplaymeitu/2021/{pags1}'
        #         pag1 = requests.get(url=pag).text 
        #         html_url = etree.HTML(pag1)
        #         png = html_url.xpath('//div[@class="articleV4Body"]/p/a/img/@src')
        #         if png ==[]:
        #             continue
        #         else:
        # # if len(png):
        #             for png1 in png:
        #                 title = png1.split('/')[-1]
        #                 print('正在下载', title)
        #                 line = requests.get(url=png1).content
        #                 with open('D:/pag/' + title, mode="wb")as f:
        #                     f.write(line)
        #                     time.sleep(5)
        #                     print('下载完成\n')
            
response = get_page_index(url)
resps = re.findall((r'<a href="(.*?)" title=.*? target="_blank">'), response)
datas = get_resps(resps)


# def get_datas(datas):
#     for pags1 in datas:
#         pag = f'https://www.27270.net/game/cosplaymeitu/2021/{pags1}'
#         pag1 = requests.get(url=pag).text 
#         html_url = etree.HTML(pag1)
#         png = html_url.xpath('//div[@class="articleV4Body"]/p/a/img/@src')
#         if png ==[]:
#             print(None)
#         else:
#             for png1 in png:
#                 title = png1.split('/')[-1] 
#                 print('正在下载', title)
        
            
        
    

# def get_datas(datas):
#   pass


# def main():
    
#     response = get_page_index(url).text
#     get_resps(response) 

# if __name__ == '__main__':
#     get_datas( )