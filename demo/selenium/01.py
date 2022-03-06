import time
import click
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get("https://douban.com")
time.sleep(0.5)
web.switch_to.frame(0)
time.sleep(0.5)
web.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(0.5)
web.find_element_by_id('username').send_keys("13537924453")
time.sleep(0.5)
web.find_element_by_xpath('//*[@id="password"]').send_keys("tiang198416")
time.sleep(0.5)
web.find_element_by_class_name('account-form-field-submit').click()
time.sleep(1)
iframe = web.find_elements(By.TAG_NAME, "iframe")[0]
web.switch_to.frame(iframe)
time.sleep(0.5)
distance=320
actions = webdriver.ActionChains(web)
# silde = web.find_element_by_class_name('tc-drag-thumb')
# actions.click_and_hold(silde)
web.switch_to.default_content()
silde = web.find_element_by_class_name('tc-drag-thumb')
actions.click_and_hold(silde)
actions.pause(0.3)

agr = actions.move_by_offset(distance+5,0)
actions.pause(0.4)
actions.move_by_offset(-10,0)
actions.pause(0.5)
actions.release()
actions.perform()
time.sleep(2)