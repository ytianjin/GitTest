import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver import ActionChains


web = webdriver.Chrome()
# web.maximize_window()
web.get('https://ai.taobao.com/')
time.sleep(1)
web.find_element_by_xpath('//*[@id="J_LoginInfoHd"]/a[1]').click()
time.sleep(1)
web.maximize_window()
web.find_element_by_id('fm-login-id').send_keys("13537924453")
time.sleep(1)
web.find_element_by_id('fm-login-password').send_keys("tiang198416")
time.sleep(1)
web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(1)
web.switch_to.frame('baxia-dialog-content')
time.sleep(0.3)
silde = web.find_element_by_id('nc_1_n1z')
actions = webdriver.ActionChains(web)
dicde=150
actions.click_and_hold(silde)
actions.pause(0.3)
actions.move_by_offset(dicde+200,0)
actions.pause(0.4)
actions.move_by_offset(-50,0)
actions.pause(0.5)
actions.release()
actions.perform()
time.sleep(2)