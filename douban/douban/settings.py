BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

FEED_EXPORT_ENCODING = 'UTF8'  # json文件二进制转中文

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4  # 并发请求数量


DOWNLOAD_DELAY = 3  # 下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True  # 随机化下载延迟

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
}
# 配置数据管道
ITEM_PIPELINES = {
   'douban.pipelines.DoubanPipeline': 300,
}
