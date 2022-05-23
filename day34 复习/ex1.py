# 作者:  Bruce
# 时间： 2022/5/20
# 金山文档
# 解析库
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 判断当前的某个节点是否存在
import selenium.common.exceptions

# 保存文件库
import json
import csv

# 时间库
import time


class Suning(object):
    # 打开文件
    def open_file(self):
        self.fd = open('Suning.txt', 'w', encoding='utf-8')
        # 打开浏览器

    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.wait = WebDriverWait(self.browser, 10)
        # 初始化变量

    def init_variable(self):
        self.data = zip()
        self.isLast = False
        # 解析网页

    def parse_page(self):
        try:
            skus = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="general clearfix"]/li')))
            skus = [item.get_attribute('id').replace('-', '/') for item in skus]
            links = [f'https://product.suning.com/{sku}.html' for sku in skus]

            titles = self.wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//ul[@class="general clearfix"]/li//div[@class="title-selling-point"]/a')))
            titles = [item.text for item in titles]

            self.data = zip(links, titles)
        except selenium.common.exceptions.TimeoutException:
            print('超时')
            self.parse_page()
        except selenium.common.exceptions.StaleElementReferenceException:
            print('刷新失败')
            self.browser.refresh()
            # 翻页

    def next_page(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextPage"]'))).click()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 滑动到页面最底层
            time.sleep(1)
        except selenium.common.exceptions.NoSuchElementException:
            self.isLast = True
        except selenium.common.exceptions.TimeoutException:
            self.next_page()
        except selenium.common.exceptions.StaleElementReferenceException:
            self.browser.refresh()
            # 写入文件

    def write_to_file(self):
        for item in self.data:
            self.fd.write("--------------------------------------\n")
            self.fd.write("链接: " + str(item[0]) + "\n")
            self.fd.write("价格: " + str(item[1]) + "\n")
            # 关闭文件

    def close_file(self):
        self.fd.close()
        # 关闭浏览器

    def close_browser(self):
        self.browser.quit()

    def suning_spider(self):
        self.open_file()
        self.open_browser()
        self.init_variable()
        print('start')
        self.browser.get('https://search.suning.com/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91/')
        time.sleep(1)
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        count = 0
        while not self.isLast:
            count += 1
            print(f'正在爬取第{count}页')
            self.parse_page()
            self.write_to_file()
            self.next_page()
        self.close_file()
        self.close_browser()


if __name__ == '__main__':
    su = Suning()
    su.suning_spider()