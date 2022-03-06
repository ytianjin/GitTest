import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver import Chrome
from selenium import webdriver

web = webdriver.Chrome()
web.get("https://login.51job.com/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url=")
web.find_element_by_xpath('//*[@id="loginname"]').send_keys("13537924453")
web.find_element_by_xpath('//*[@id="password"]').send_keys("tiang198416")
web.find_element_by_xpath('//*[@id="isread_em"]').click()
web.find_element_by_xpath('//*[@id="login_btn_withPwd"]').click()
web.maximize_window() # 全屏最大化浏览器
web.find_element_by_xpath('//*[@id="topIndex"]/div/p/a[2]').click()
web.find_element_by_xpath('//*[@id="keywordInput"]').send_keys("python")
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a/span').click()
ttags = web.find_element_by_class_name("ttag")
for tag in ttags:
    tag.click()
    web.find_element_by_xpath('//*[@id="popop"]/div/div[3]/span').click()