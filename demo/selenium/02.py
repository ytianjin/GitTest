import time
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

web = webdriver.Chrome()
web.get("https://accounts.douban.com/passport/login")
# height: 300px; width: 300px;  <iframe style="height: 300px; width: 300px;" frameborder="0" src="//accounts.douban.com/passport/login_popup?login_source=anony"></iframe>
time.sleep(1)
web.find_element_by_class_name('account-tab-account').click()
time.sleep(0.5)
web.find_element_by_id('username').send_keys("13537924453")
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="password"]').send_keys("tiang198416")
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
time.sleep(3)
web.switch_to.frame('tcaptcha_iframe')
silde = web.find_element_by_id('tcaptcha_drag_thumb')
actions = webdriver.ActionChains(web)
aicde=205
actions.click_and_hold(silde)
actions.pause(0.3)
actions.move_by_offset(aicde,0)
actions.pause(0.3)
actions.move_by_offset(aicde+20,0)
actions.pause(0.3)
actions.move_by_offset(-10,0)
actions.pause(0.3)
actions.release()
actions.perform()
time.sleep(2)
# while True:
#     distance=325
#     actions = webdriver.ActionChains(web)
#     silde = web.find_element_by_id('tcaptcha_drag_thumb')
#     actions.click_and_hold(silde)
#     actions.pause(0.5)
#     actions.move_by_offset(distance+5,0)
#     actions.pause(0.5)
#     actions.move_by_offset(-10,0)
#     actions.pause(0.5)
#     actions.release()
#     actions.perform()
#     time.sleep(1)
#     try:
#         web.find_element_by_xpath('//*[@id="reload"]/div').click()
#     except:
#         web.quit()
#         break