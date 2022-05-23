# 导入库
# 1. 解析库
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions

# 2. 保存库
import json
import csv

# 3. 时间
import time


# 京东爬虫
class JdSpider(object):

    # 初始化
    def __init__(self):
        self.wait = None
        self.file_data = None
        self.filename = None
        self.isLast = None
        self.data = None
        self.browser = None

    # 打开文件
    def open_file(self):
        self.filename = input('请输入要保存的文件格式txt/json/csv:')
        while self.filename != 'txt' and self.filename != 'json' and self.filename != 'csv':
            print('输入错误，请重新输入！')
        if self.filename == 'txt':
            self.file_data = open('Jd.txt', 'w', encoding='utf-8')
        elif self.filename == 'json':
            self.file_data = open('Jd.json', 'w', encoding='utf-8')
        elif self.filename == 'csv':
            pass

    # 打开浏览器
    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    # 初始化变量
    def init_variable(self):
        self.data = zip()
        self.isLast = False

    # 解析网页
    def parse_web(self):
        try:
            self.wait = WebDriverWait(self.browser, 10)
            skus = self.wait.until(ec.presence_of_all_elements_located(By.XPATH, '//li[@class="gl-item"'))
            skus = [item.get_attribute('data-sku') for item in skus]
            link = [f'https://item.jd.com/{sku}.html' for sku in skus]

            titles = self.wait.until(
                ec.presence_of_all_elements_located(By.XPATH, '//div[@class="p-name p-name-type-2"]/a/em'))
            title = [item.text for item in titles]

            prices = self.wait.until(ec.presence_of_all_elements_located(By.XPATH, '//div[@class="p-price"]/strong'))
            price = [item.text for item in prices]

            comments_numbers = self.wait.until(
                ec.presence_of_all_elements_located(By.XPATH, '//div[class="p-commit"]/strong'))
            comments_number = [item.text for item in comments_numbers]

            self.data = zip(link, title, price, comments_number)
        except:
            pass

    # 翻页
    def next_page(self):
        pass

    # 保存到文件中
    def write_to_file(self):
        if self.filename == 'txt':
            for item in self.data:
                self.file_data.write('---------------\n')
                self.file_data.write(str(item[0]) + '\n')
                self.file_data.write(str(item[1]) + '\n')
                self.file_data.write(str(item[2]) + '\n')
                self.file_data.write(str(item[3]) + '\n')
        elif self.filename == 'json':
            temp = ('links', 'title', 'price', 'comments number')
            for item in self.data:
                json.dump(dict(zip(temp, item)), self.file_data, ensure_ascii=False)

    # 关闭文件
    def close_file(self):
        self.file_data.close()

    # 关闭浏览器
    def close_browser(self):
        self.browser.quit()

    # 爬取动作
    def crawl(self, url):
        self.open_file()
        self.open_browser()
        self.init_variable()
        print('开始爬取......')
        self.browser.get(url)
        time.sleep(1)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)

        print('正在爬取...')
        self.parse_web()
        self.write_to_file()
        self.close_file()
        self.close_browser()
        print('结束爬取')


if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8"
    jd_spider = JdSpider()
    jd_spider.crawl(url)
