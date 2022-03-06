from urllib.request import urlopen

url = 'https://www.kanxiaojiejie.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = urlopen(url).read().decode('utf-8')
print(response)