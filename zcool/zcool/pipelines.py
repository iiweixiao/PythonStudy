# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class ZcoolPipeline:
    def __init__(self):
        self.f = open('Zcool.csv', 'w', encoding='utf-8', newline='')
        self.file_name = ['imgLink', 'title', 'types', 'vistor', 'comment', 'likes']
        self.writer = csv.DictWriter(self.f, fieldnames=self.file_name)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(dict(item))
        print(item)

        return item

    def close_spider(self, spider):
        self.f.close()