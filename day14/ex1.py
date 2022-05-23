# 导入库
# 1. 解析库
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions

# 2. 保存库
import json
import csv

# 3. 时间
import time


# 京东爬虫
class JdSpider(object):

    # 初始化
    # def __init__(self):
    #     self.wait = None
    #     self.file_data = None
    #     self.filename = None
    #     self.isLast = None
    #     self.data = None
    #     self.browser = None

    # 打开文件
    def open_file(self):
        self.fm = input('请输入要保存的文件格式txt/json/csv:')
        while self.fm != 'txt' and self.fm != 'json' and self.fm != 'csv':
            print('输入错误，请重新输入！')
        if self.fm == 'txt':
            self.fd = open('Jd.txt', 'w', encoding='utf-8')
        elif self.fm == 'json':
            self.fd = open('Jd.json', 'w', encoding='utf-8')
        elif self.fm == 'csv':
            pass

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
        # try:
        #     self.wait = WebDriverWait(self.browser, 10)
        #     skus = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]')))
        #     skus = [item.get_attribute('data-sku') for item in skus]
        #     link = [f'https://item.jd.com/{sku}.html' for sku in skus]
        #
        #     titles = self.wait.until(
        #         ec.presence_of_all_elements_located((By.XPATH, '//div[@class="p-name p-name-type-2"]/a/em')))
        #     title = [item.text for item in titles]
        #
        #     prices = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, '//div[@class="p-price"]/strong')))
        #     price = [item.text for item in prices]
        #
        #     comments_numbers = self.wait.until(
        #         ec.presence_of_all_elements_located((By.XPATH, '//div[class="p-commit"]/strong')))
        #     comments_number = [item.text for item in comments_numbers]
        #
        #     self.data = zip(link, title, price, comments_number)
        # except selenium.common.exceptions.TimeoutException:
        #     print('超时')
        #     self.parse_web()
        # except selenium.common.exceptions.StaleElementReferenceException:
        #     self.browser.refresh()
        try:
            skus = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//li[@class="gl-item"]')))
            skus = [item.get_attribute('data-sku') for item in skus]  # 数据编号

            lianjie = ["https://item.jd.com/{sku}.html".format(sku=item) for item in skus]  # 和编号进行链接的拼接

            jiage = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="gl-i-wrap"]/div[2]/strong/i')))
            jiage = [item.text for item in jiage]  # 价格

            biaoti = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="gl-i-wrap"]/div[3]/a/em')))
            biaoti = [item.text for item in biaoti]  # 标题

            pingjia = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[@class="gl-i-wrap"]/div[4]/strong')))
            pingjia = [item.text for item in pingjia]  # 评价
            self.data = zip(lianjie, jiage, biaoti, pingjia)
        # 异常处理
        except selenium.common.exceptions.TimeoutException:  # 超时异常
            print("parse_page: TimeoutException")
            self.parse_page()

        except selenium.common.exceptions.StaleElementReferenceException:  # 页面刷新不成功，请求异常
            print("parse_page: StaleElementReferenceException")
            self.browser.refresh()  # 刷新重置


    # 翻页
    def next_page(self):
        try:
            self.wait.until(ec.presence_of_all_elements_located((By.XPATH,'//a[class="pn-next"]'))).click()
            time.sleep(1)
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
        except selenium.common.exceptions.NoSuchElementException:
            self.isLast = True
        except selenium.common.exceptions.TimeoutException:
            print('超时')
            self.next_page()
        except selenium.common.exceptions.StaleElementReferenceException:
            print('页面刷新失败')
            self.browser.refresh()

    # 保存到文件中
    def write_to_file(self):
        if self.fm == 'txt':
            for item in self.data:
                self.fd.write('---------------\n')
                self.fd.write(str(item[0]) + '\n')
                self.fd.write(str(item[1]) + '\n')
                self.fd.write(str(item[2]) + '\n')
                self.fd.write(str(item[3]) + '\n')
        elif self.fm == 'json':
            temp = ('links', 'title', 'price', 'comments number')
            for item in self.data:
                json.dump(dict(zip(temp, item)), self.fd, ensure_ascii=False)

    # 关闭文件
    def close_file(self):
        self.fd.close()

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
        count = 0
        while not self.isLast:
            count += 1
            print(f'正在爬取第{count}页...')
            self.parse_page()
            self.write_to_file()
            self.next_page()
        self.close_file()
        self.close_browser()
        print('结束爬取')


if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8"

    jd_spider = JdSpider()
    jd_spider.crawl(url)
