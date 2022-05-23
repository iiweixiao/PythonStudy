import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from zhaobiao.items import ZhaobiaoItem

class ZbSpider(scrapy.Spider):
    name = 'zb'
    allowed_domains = ['www.chinabidding.cn']
    start_urls = ['https://www.chinabidding.cn/search/searchgj/zbcg?keywords=%E8%AF%95%E9%AA%8C%E6%9C%BA']

    def parse(self, response):
        sel = Selector(response)
        zb_items = sel.xpath('//div[@class="lieb"]/table/tbody/tr/td/table/tbody')

        for i in zb_items:
            item = ZhaobiaoItem()
            item['标题'] = i.xpath('//tr//a/@title').extract_first()
            item['地点'] = i.xpath('//tr/td[5]/text()').extract_first()
            item['行业'] = i.xpath('//tr/td[6]/text()').extract_first()
            yield item
