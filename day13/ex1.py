import os.path
import time
from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

DOWNLOAD_PATH = 'images/'


def download_picture(url: str):
    filename = pic_url[pic_url.rfind('/') + 1:]
    res = requests.get(url)
    with open(os.path.join(DOWNLOAD_PATH, filename), 'wb') as file:
        file.write(res.content)


if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)
browser = webdriver.Chrome()
browser.get('https://image.so.com/c?ch=car')
browser.implicitly_wait(10)  # 隐式等待10秒
kw_input = browser.find_element(By.CSS_SELECTOR, '#app > div > div.search > div > form > div > input')
kw_input.send_keys('名车')
kw_input.send_keys(Keys.ENTER)
for _ in range(3):
    # browser.execute_script(
    #     'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    # )
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
imgs = browser.find_elements(By.CSS_SELECTOR, 'div.waterfall img')

with ThreadPoolExecutor(max_workers=32) as pool:
    for img in imgs:
        pic_url = img.get_attribute('src')
        pool.submit(download_picture, pic_url)
