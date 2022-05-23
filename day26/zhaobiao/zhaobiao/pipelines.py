# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import openpyxl
from zhaobiao.items import ZhaobiaoItem


class ZhaobiaoPipeline:


    def __init__(self):
        self.wb = openpyxl.Workbook()  # 打开excel表格
        self.sheet = self.wb.active  # 激活表单
        self.sheet.title = '招标'  # 表单名称为Top250
        self.sheet.append(('标题', '地点', '行业'))  # 前三列名称

    def process_item(self, item: ZhaobiaoItem, spider):
        self.sheet.append((item['title'], item['place'], item['industry']))
        return item

    def close_spider(self, spider):
        self.wb.save('招标网.xlsx')