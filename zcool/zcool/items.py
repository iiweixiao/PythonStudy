# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZcoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgLink = scrapy.Field()
    title = scrapy.Field()
    types = scrapy.Field()
    vistor = scrapy.Field()
    comment = scrapy.Field()
    likes = scrapy.Field()
