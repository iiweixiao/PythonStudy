from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
attr = browser.find_element(By.ID, 'special')
print(attr)
print(attr.get_attribute('class'))