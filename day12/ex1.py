from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.taobao.com")

input_first = browser.find_element(By.CSS_SELECTOR,
                                   'body > div.screen-outer.clearfix > div.tbh-service.J_Module > div > ul')
input_second = browser.find_element(By.CSS_SELECTOR, '.service-bd li')
print(input_first)
print(input_first)
browser.close()
