from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url = 'https://www.taobao.com/'
browser.get(url)

# print(browser.page_source)

# input_first = browser.find_element_by_id()  # python版本3.8以上，此方法已不再使用
# https://blog.csdn.net/weixin_41635857/article/details/120863053
input_first = browser.find_element(By.ID, 'q')
input_second = browser.find_element(By.CSS_SELECTOR, '#q')
input_third = browser.find_element(By.XPATH, '//*[@id="q"]')

print(input_first)
print(input_second)
print(input_third)

browser.close()
