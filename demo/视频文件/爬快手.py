import json
import time
import requests

url = 'https://www.kuaishou.com/graphql'
headers = {
            'content-type': 'application/json',
            'Cookie': 'kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_4c8bf08dbe2e5d4539a495c27b09675e; ktrace-context=1|MS43NjQ1ODM2OTgyODY2OTgyLjg5ODEyNzE3LjE2MzY5Nzc0NDQ5NzEuNjA1Mg==|MS43NjQ1ODM2OTgyODY2OTgyLjUyMTcyNjc4LjE2MzY5Nzc0NDQ5NzEuNjA1Mw==|0|graphql-server|webservice|false|NA',
            'Origin': 'https://www.kuaishou.com',
            'Host': 'www.kuaishou.com',
            'Referer': 'https://www.kuaishou.com/search/video?searchKey=%E6%80%A7%E6%84%9F',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
data = {
        'operationName': "visionSearchPhoto",
        'query': "query visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        photoUrl\n        liked\n        timestamp\n        expTag\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n",
        'variables': {'keyword': "性感", 'pcursor': "", 'page': "search"}
}
data = json.dumps(data)
resps_1 = requests.post(url=url, data=data, headers=headers)
resps = resps_1.json()['data']['visionSearchPhoto']['feeds']
for resp in resps:
    title = resp['photo']['caption'] + '.mp4'
    pics = resp['photo']['photoUrl']
    print('正在下载',title)
    pic = requests.get(pics).content
    with open("D:/mp4/" + title, mode="wb") as f:
        f.write(pic)
        print('下载完成\n',title)
        time.sleep(5)

