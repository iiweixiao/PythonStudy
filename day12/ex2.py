import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://www.taobao.com")

input1 = browser.find_element(By.ID, 'q')
input1.send_keys("笔记本")

time.sleep(3)
input1.clear()
input1.send_keys('iPad')

button = browser.find_element(By.CLASS_NAME, 'btn-search')  # 找到搜索按钮
button.click()