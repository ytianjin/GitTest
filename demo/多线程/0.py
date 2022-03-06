import time
import requests
from multiprocessing.dummy import Pool

start = time.time()
urls = [
    'www.1.com',
    'www.2.com',
    'www.3.com'
]
def get_request(url):
    print("ytfrhg", url)
    time.sleep(2)
    print('jhg', url)

for url in urls:
    get_request(url)

print(time.time()-start)