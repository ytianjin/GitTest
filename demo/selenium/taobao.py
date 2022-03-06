from distutils.file_util import move_file
from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

def main():
    web = webdriver.Chrome()
    web.maximize_window()
    web.get('https://login.taobao.com/member/login.jhtml')
    time.sleep(1)
    web.find_element_by_name('fm-login-id').send_keys("帐号")
    time.sleep(1)
    web.find_element_by_name('fm-login-password').send_keys("密码")
    time.sleep(1)

    GetImage(web)

def GetImage(web):
    web.save_screenshot('taobao.png')
    code_img_ele = web.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
    Action(web, code_img_ele)

def Action(web,code_img_ele):
    action = ActionChains(web)
    action.click_and_hold(code_img_ele)
    action.move_by_offset(300,42).perform()
    # ActionChains(driver).move_by_offset(300, 42).perform()
    time.sleep(1)
    # ActionChains(driver).click_and_hold().move_by_offset(300,42).release().perform()
    action.release()
    web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
    time.sleep(10)
    web.quit()

if __name__ == "__main__":
    main()