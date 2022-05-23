# 爬取豆瓣电影top250电影名字

import requests
import re

urls = []
headers = {
    'Cookie': 'll="118159"; bid=_dB4ilQ3CoI; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1000363927.1650803281.1650803281.1650803281.1; __utmb=30149280.0.10.1650803281; __utmc=30149280; __utmz=30149280.1650803281.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.360204462.1650803281.1650803281.1650803281.1; __utmb=223695111.0.10.1650803281; __utmc=223695111; __utmz=223695111.1650803281.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=D6A63E5E4BD2F6D31237483BE03866ED3|14ce3a0cc4895d4a7a08d5675332fd39; __gads=ID=0e9c19baa61f9825-22be63136dd20025:T=1650803322:RT=1650803322:S=ALNI_MZWxRqNjLZlqP-Zx_oLOHOLASxefQ; _pk_id.100001.4cf6=d754daf52cdb287e.1650803281.1.1650803478.1650803281.; dbcl2="203282692:TXE3Voo0zio"',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
index = 1
for i in range(10):
    if i == 0:
        url = 'https://movie.douban.com/top250'
    else:
        url = f'https://movie.douban.com/top250?start={25*i}&filter='
    r = requests.get(url, headers=headers).text
    pattern = re.compile('class="">\n\s*?<span class="title">(.*?)</span>', re.S)
    res = re.findall(pattern, r)
    for item in res:
        print(str(index) + ' ' +item)
        index += 1





