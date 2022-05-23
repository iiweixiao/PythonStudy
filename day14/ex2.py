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
    def open_file(self):
        self.fm = input('请输入文件保存格式txt/json/csv: ')
        while self.fm != "txt" and self.fm != 'json' and self.fm != "csv":
            self.fm = input('输入错误，请重新输入文件保存格式(txt/json/csv):')
        if self.fm == 'txt':
            self.fd = open("Jd.txt", 'w', encoding="utf-8")
        elif self.fm == "json":
            self.fd = open("Jd.json", 'w', encoding='utf-8')
        elif self.fm == "csv":
            self.fd = open("Jd.csv", 'w', encoding='utf-8', newline="")

    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)  # 隐式等待 超过30秒没有定位到一个元素，程序就会报错抛出异常，期间会一直轮询查找定位元素
        self.wait = WebDriverWait(self.browser, 10)

    def init_variable(self):
        self.data = zip()  # 将可迭代的对象作为参数， 将对象中对应的元素打包成一个个元组，然后返回由元组组成的列表
        self.isLast = False  # 用来判断是否达到最后一条

    def parse_page(self):
        #
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

    def write_to_file(self):
        if self.fm == "txt":
            for item in self.data:
                self.fd.write("--------------------------------------\n")
                self.fd.write("链接: " + str(item[0]) + "\n")
                self.fd.write("价格: " + str(item[1]) + "\n")
                self.fd.write("标题: " + str(item[2]) + "\n")
                self.fd.write("评价: " + str(item[3]) + "\n")

        if self.fm == "json":
            temp = ("链接", "价格", "标题", "评价")
            for item in self.data:
                json.dump(dict(zip(temp, item)), self.fd, ensure_ascii=False)

        if self.fm == "csv":
            write = csv.writer(self.fd)
            for item in self.data:
                write.writerow(item)

    def close_file(self):
        self.fd.close()

    def close_browser(self):
        self.browser.quit()

    def crawl(self, url):
        self.open_file()
        self.open_browser()
        self.init_variable()
        print("开始爬取")
        self.browser.get(url)
        time.sleep(1)

        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.parse_page()
        self.write_to_file()
        # self.fan_ye()
        self.close_file()
        self.close_browser()
        print("结束爬取")


if __name__ == '__main__':
    url = "https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8"
    spider = JdSpider()
    spider.crawl(url)
