import requests
import re
from pyquery import PyQuery as pq
def Tools(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'
    }
    response = requests.get(url, headers=headers)
    return response
def Play(title, url):
    # url = 'https://www.520mmtv.com/9614.html'
    response = Tools(url).text
    video_url = re.findall(r'url: "(.*?)",', response)[0]
    video_content = Tools(video_url).content
    with open('D:\mp4\{}.mp4'.format(title), 'ab') as f:
        f.write(video_content)
        print('{}下载完成....'.format(title))
def main():
    url = 'https://www.520mmtv.com/hd/rewu.html'
    response = Tools(url).text
    doc = pq(response) # 创建pyquery对象 注意根据css的 class 类选择 和id选择器进行数据提取
    i_list = doc('.meta-title').items() # .类选择器 中间有空格的 记得替换成.
    meta_title = doc('.meta-title').items() # 标题
    for i, t in zip(i_list, meta_title):
        href = i.attr('href')
        Play(t.text(), href)
if __name__ == '__main__':
    main()

