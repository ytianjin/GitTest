from email import header
import requests
import time
from urllib.parse import urlencode
from lxml import etree

parse = {
        'sem': '1',
        'sem_kid': '1000060',
        'sem_type': '1',
        'bd_vid': '10575026760741467082'
}
url = 'https://699pic.com/tupian/photo-qingnian.html?' + urlencode(parse)
headers = {
        'cookie': 'channel_info_reg=d3d3LmJhaWR1LmNvbQ%3D%3D;channel_info=d3d3LmJhaWR1LmNvbQ%3D%3D; mediav=%7B%22eid%22%3A%22841650%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22%3FGFeM%5D%3CZJ!8%5Dj%60U9t1_I%22%2C%22ctn%22%3A%22%22%2C%22vvid%22%3A%22%3FGFeM%5D%3CZJ!8%5Dj%60U9t1_I%22%2C%22_mvnf%22%3A1%2C%22_mvctn%22%3A0%2C%22_mvck%22%3A0%2C%22_refnf%22%3A0%7D; PHPSESSID=9f530b2fa0a340a9fd0e46362c74ba23; uniqid=61ef9808c028c; from_data=YTo4OntzOjQ6Imhvc3QiO3M6MTM6Ind3dy5iYWlkdS5jb20iO3M6Mzoic2VtIjtiOjE7czoxMDoic291cmNlZnJvbSI7aTowO3M6NDoid29yZCI7czowOiIiO3M6Mzoia2lkIjtpOjEwMDA0MDA4O3M6ODoic2VtX3R5cGUiO2k6MTtzOjQ6ImZyb20iO2k6MDtzOjY6ImNyZWF0ZSI7czoxOToiMjAyMi0wMS0yNSAxNDoyNjoxNiI7fQ%3D%3D; sem_from=1; bd_vid=MTA5NTIxNjg4OTk5NzEwMTM5MzcsaHR0cHMlM0ElMkYlMkY2OTlwaWMuY29tJTJGYmVzdF9hbGJ1bSUyRjY0JTJGNDAzJTJGMS5odG1sJTNGc2VtJTNEMSUyNnNlbV9raWQlM0QxMDAwNDAwOCUyNnNlbV90eXBlJTNEMSUyNmJkX3ZpZCUzRDEwOTUyMTY4ODk5OTcxMDEzOTM3; act_layer_1=A; act_layer_2=A; act_layer_3=A; act_layer_4=B; act_layer_5=B; act_layer_6=A; act_layer_7=A; act_layer_9=A; FIRSTVISITED=1643091980.694; user_uniqid=22CCCD4E89C73317; s_token=4b0258d32b6a2f0478a7f18e869ec851; visited_times=2; redirect=https%3A%2F%2F699pic.com%2Ftupian%2Fphoto-qingnian.html%3Fsem%3D1%26sem_kid%3D1000060%26sem_type%3D1%26bd_vid%3D10575026760741467082; referer_page=search:index_1; Qs_lvt_375926=1643091980%2C1643092021; Qs_pv_375926=262539702730918660%2C260288512803637760; prevPageSid=64916; Hm_lvt_ddcd8445645e86f06e172516cac60b6a=1643091984,1643092030; Hm_lpvt_ddcd8445645e86f06e172516cac60b6a=1643092030; Hm_lvt_1154154465e0978ab181e2fd9a9b9057=1643091984,1643092030; Hm_lpvt_1154154465e0978ab181e2fd9a9b9057=1643092030',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = requests.get(url=url, headers=headers).text
data = etree.HTML(response)
line = data.xpath('//div[@class = "list"]/a/@href')
for pag in line:
        pag_url = 'https:' + pag
        resps = requests.get(url=pag_url, headers=headers).text                          #//div[@class = "huabu"]/a/@href
        resps1 = etree.HTML(resps)
        resp = resps1.xpath('//div[@class = "huabu"]/a/@href')[0]
        title = resps1.xpath('//div[@class = "huabu"]/a/img/@title')[0]
        title1 = title + '.jpg'
        print('正在下载', title1)
        png = 'https:' + resp
        png1 = requests.get(url=png, headers=headers).content
        with open('D:/pag/' + title1, mode="wb")as f:
                f.write(png1) 
                time.sleep(5)
                print('下载完成\n')