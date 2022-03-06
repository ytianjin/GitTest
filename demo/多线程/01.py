from multiprocessing import pool
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
    return 123


pool = Pool(3)
result_list = pool.map(get_request,urls)
print(result_list)

print(time.time()-start)