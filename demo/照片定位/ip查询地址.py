from ast import operator
from tkinter import *
import requests
import re


def get_data():
    # print('规划放入套房')
    ip = input_ip.get()
    headers =   {
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Referer': 'http://www.ipip.net/ip/157.122.65.26.html',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cookie': 'LOVEAPP_SESSID=e458ab4e08c18f978acfabc69002b947cf412875; __jsluid_h=bcbdd1888a64ba29d6637e3762b651e6; _ga=GA1.2.788142739.1644298217; _gid=GA1.2.2046811549.1644298217; tj-club=1; Hm_lvt_6b4a9140aed51e46402f36e099e37baf=1644299179; _gat=1; Hm_lpvt_6b4a9140aed51e46402f36e099e37baf=1644299263; __jsl_clearance=1644299295.765|0|ySG5Qe%2BatRDk3f4BJCsXWxYAlL0%3D'}
    rep = requests.get("http://www.ipip.net/ip/{}.html".format(ip), headers=headers).text
    # 通配符
    address = re.search('地理位置.*?;">(.*?)</span>',rep,re.S)
    operator = re.search('运营商.*?;">(.*?)</span>',rep,re.S)
    time = re.search('线路.*?;">(.*?)</span>',rep,re.S)
    wrap = re.search('地区中心经纬度.*?;">(.*?)</span>',rep,re.S)
    if address:
        ip_list = ['地理位置:' +address.group(1),"当前IP:"+ip]
        if operator:
            ip_list.insert(0,"运营商/所有者:"+operator.group(1))
        if time:
            ip_list.insert(0,"线路:"+time.group(1))
        if wrap:
            ip_list.insert(0,"地区中心经纬度:"+wrap.group(1))
    else:
        display_info.delete(0,5)
        display_info.insert(0,"这是一个无效的ip地址")

# 窗口
tk = Tk()

tk.title("Tony")
# from = widthxheight+x+y
# 窗口组件的位置
tk.geometry('+1000+300')
# 输入框组件
# Entry(tk).pack()
input_ip = Entry(tk,width=50)
input_ip.pack()
# 回显列表
display_info = Listbox(tk,width=60,height=10)
display_info.pack()
# 按钮
result_btn = Button(tk,text="查询", command=get_data)
result_btn.pack()

# 轮询
tk.mainloop()

# http://www.ipip.net/ip/157.122.65.26.html

# <td>地理位置.*?;">(.*?)</span>