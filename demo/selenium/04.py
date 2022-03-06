from turtle import distance
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


web = webdriver.Chrome()
web.get("https://mail.qq.com/")
time.sleep(0.5)
web.switch_to.frame('login_frame')
web.find_element_by_id('u').send_keys('953374602')
time.sleep(0.5)
web.find_element_by_id('p').send_keys('tiang')
time.sleep(0.5)
# WebDriverWait(web,10).until(ec.element_to_be_clickable(By.ID('login_button')))
web.find_element_by_id('login_button').click()
time.sleep(1)
web.switch_to.frame('tcaptcha_iframe')
time.sleep(0.5)
while True:
    distance=175
    actions = webdriver.ActionChains(web)
    slider = web.find_element_by_id('tcaptcha_drag_thumb')
    actions.click_and_hold(slider)
    actions.pause(0.3)
    actions.move_by_offset(distance+5,0)
    actions.pause(0.3)
    actions.move_by_offset(-10,0)
    actions.pause(0.5)
    actions.release()
    actions.perform()
    time.sleep(2)
    try:
        # shuaxin=webdriver(web,1).until(ec.presence_of_all_element_located((By.CLASS_NAME,'tcaptcha-embed-contrl')))
        web.find_element_by_class_name('tcaptcha-embed-contrl').click()
    except:
        web.quit()
        break

# web.find_element_by_xpath('//*[@id="p"]').send_keys('tiang.1984.@.#')
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="login_button"]').click()