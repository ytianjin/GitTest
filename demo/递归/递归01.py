import requests
from lxml import etree


def func(n,m):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    response = requests.get(url=n, headers=headers).text
    for tree in etree.HTML(response).xpath(m): 
        agr = f'https://www.tupianzj.com/{tree}'
        func(agr,'//div[@class="pages"]/ul/li/a/ @href')
        print(tree)



url = 'https://www.tupianzj.com/meinv/mm/meituwang/'
m = '//div[@class="zt_con_img"]//li/a/@href'
func(url,m)

"""
#
229013_2.html
229013_3.html
229013_4.html
229013_5.html
229013_6.html
229013_7.html
229013_8.html
229013_2.html
/meinv/20210621/229013.html
javascript:dPlayPre();
#
228893_2.html
228893_3.html
228893_4.html
228893_5.html
228893_6.html
228893_7.html
228893_8.html
228893_2.html
/meinv/20210615/228893.html
javascript:dPlayPre();
#
228455_2.html
228455_3.html
228455_4.html
228455_5.html
228455_6.html
228455_7.html
228455_8.html
228455_2.html
/meinv/20210531/228455.html
javascript:dPlayPre();
#
228504_2.html
228504_3.html
228504_4.html
228504_5.html
228504_6.html
228504_7.html
228504_8.html
228504_2.html
/meinv/20210531/228504.html
javascript:dPlayPre();
#
228399_2.html
228399_3.html
228399_4.html
228399_5.html
228399_6.html
228399_7.html
228399_8.html
228399_2.html
/meinv/20210529/228399.html
javascript:dPlayPre();
#
228105_2.html
228105_3.html
228105_4.html
228105_5.html
228105_6.html
228105_7.html
228105_8.html
228105_2.html
/meinv/20210518/228105.html
javascript:dPlayPre();
#
228030_2.html
228030_3.html
228030_4.html
228030_5.html
228030_6.html
228030_7.html
228030_8.html
228030_2.html
/meinv/20210513/228030.html
javascript:dPlayPre();
#
227848_2.html
227848_3.html
227848_4.html
227848_5.html
227848_6.html
227848_7.html
227848_8.html
227848_2.html
/meinv/20210510/227848.html
javascript:dPlayPre();
#
227726_2.html
227726_3.html
227726_4.html
227726_5.html
227726_6.html
227726_2.html
/meinv/20210508/227726.html
javascript:dPlayPre();
#
227636_2.html
227636_3.html
227636_4.html
227636_5.html
227636_6.html
227636_7.html
227636_8.html
227636_2.html
/meinv/20210506/227636.html
"""