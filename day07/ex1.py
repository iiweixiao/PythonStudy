import re
import requests

url = 'https://www.iplaysoft.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

r= requests.get(url, headers=headers).text

# rel="external nofollow" title="上海增本土2736+20634 死亡12例" target="_blank"><span>1</span>上海增本土2736+20634 死亡12例 <span class="fr friendly_number"
# title="14749946">1.47千万</span></a>
title = re.compile('href="https://www.iplaysoft.com/*.html">(.*?)</a>')

titles = title.findall(r)[0:5]
print(titles)
# for index, i in titles:
#     print(index, i)