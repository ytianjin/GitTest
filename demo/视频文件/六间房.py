import time
import requests
url = 'https://v.6.cn/minivideo/getMiniVideoList.php?act=recommend&page=1&pagesize=20'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.'}
response = requests.get(url=url, headers=headers)
resps = response.json()
resps_1 = resps['content']['list']
for resp in resps_1:
    title = resp['title'][0] +'.mp4'
    print('正在下载', title)
    resp_url = resp['playurl']
    data = requests.get(url=resp_url, headers=headers).content
    with open('D:/mp4/' + title, mode="wb") as f:
          f.write(data)
          print('下载完成', title)
          time.sleep(5)
