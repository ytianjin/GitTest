from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/?tn=95834041_hao_pg")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("美女")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').click()