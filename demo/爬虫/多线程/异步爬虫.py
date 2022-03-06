import os
import time
import requests
import asyncio  # 并发任务
import aiohttp  # 完成网络请求并发任务

headers = {
    'Host': 'www.zcool.com.cn',
    'Referer': 'https://www.zcool.com.cn/work/ZMjU4MjMzNDg=html.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
session = requests.Session()
if not os.path.exists('D:/雪中悍刀行/'):
    os.mkdir('D:/雪中悍刀行/')
# 凡是被async修饰的函数都支持异步编程
async def get_url(url):
    async with aiohttp.ClientSession() as session:  # 这一点与requests.get()同理的方法
        response = await session.get(url) #1   # 1 和2这2个方法与 response = requests.get('www.xxxx.com)
        content = await response.read  # 2                                 response.text 一样的
        return content

# 下载函数
async def downloader(img):
    # print('正在下载', title)
    content = await get_url(img[1])
    with open('D:/雪中悍刀行/' + str(img[0]) + '.jpg', 'wb')as f:
        f.write(content)
        print('下载完成' + str(img[0]))
 
def run():
    url = ('https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837')
    response = requests.get(url)
    datas = response.json()['data']['allImageList']
    # 创建协程对象

    tasks = [asyncio.create_task(downloader((i, img['url']))) for i, img in enumerate(datas)]
    print(tasks)

    # loop = asyncio.get_event_loop()
    # 指定协程运行的任务
    # tasks = [asyncio.ensure_future(downloader((i, img['url']))) for i, img in enumerate(datas)]
    # loop.run_until_complete(asyncio.wait(tasks))
asyncio.run(run())
