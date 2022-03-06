import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome

n = 1
web = Chrome()
web.get("https://www.lagou.com")
web.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[2]/button[4]').click()
time.sleep(2)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)
# web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a')
alst = web.find_elements_by_class_name('p-top__1F7CL')
for a in alst:
    a.find_element_by_tag_name("a").click()
    # 窗口转换
    web.switch_to.window(web.window_handles[-1])  # 跳转到倒数第一个窗口
    text = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text  # 拿文本
    with open('D:/abc/%s.txt' % n, mode="w")as f:
        f.write(text)
        # 关闭窗口
        web.close()
        # 调整窗口到最开始的那个页面
        web.switch_to.window(web.window_handles[0])
        time.sleep(2)
        n += 1