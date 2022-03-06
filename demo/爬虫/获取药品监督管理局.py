import requests

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'Cookie': 'JSESSIONID=C9F37601BB0E69AC96335A7FB04693D0; _ga=GA1.3.603833183.1645237101; _gid=GA1.3.17928469.1645237101; acw_tc=3ccdc16116452377093475956e648333c38ec44d06977dc4f03a19e03a6446; JSESSIONID=F22424012551621B143828B8C59C25A7; _ga=GA1.4.603833183.1645237101; _gid=GA1.4.17928469.1645237101',
    'Host': 'scxk.nmpa.gov.cn:81',
    'Origin': 'http://scxk.nmpa.gov.cn:81',
    'Referer':'http://scxk.nmpa.gov.cn:81/xk/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

for page in range(1,6):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15', 
        'productName': '',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }

    datas = requests.post(url=url, headers=headers, data=data).json()
    for lst in datas['list']:
        lst_id = lst['ID']
        
        url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        data = {
            'id': lst_id
        }
        datas = requests.post(url=url, headers=headers, data=data).json()
        