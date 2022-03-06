import requests
import json
import time

# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
response = requests.get(url=url, headers=headers)
resp = response.json()
for resp1 in resp:
    title = resp1['title']
    title_url = resp1['url']
    release_date = resp1['release_date']
    regions = resp1['regions'][0]
    score = resp1['score']
    actors = resp1['actors']
    types = resp1['types']
    result = title, score, regions, types, actors, title_url
    for result1 in result:
        result1 = str(result1).replace('[', ''). replace(']', '')
        with open('D:/33.txt', 'a', encoding= 'utf-8') as f:
            f.write(str(result1).replace("'", ''). replace(',', '') + '\n')
            time.sleep(5)
            print(result1)
    # print(f'电影名:{title}')
    # print(f'主演:{actors}')