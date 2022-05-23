import requests
import re
import json

from  multiprocessing import  Pool

def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        "Cookie": "__mta=248339128.1634798216595.1634888608153.1634888660552.49; uuid_n_v=v1; _lxsdk_cuid=17ca19124d9c8-067e95700ae966-b7a1438-144000-17ca19124d9c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=248339128.1634798216595.1634808137226.1634882862740.40; uuid=D67952C032FE11EC8F810FD937DF6B98E246DF6026234E5291A6457CD47C0BA5; _csrf=4dd7eb0c9e42a14810ae1dbe00405743ae14d894bacf15c92a00883a00142edc; lt=m048cMgyEwgvRNLPU0lleZwqWf8AAAAAAw8AABlEsAR-eBEGzNytNguZVU-A9ToZwV6Kwujs51RPDu8QdC8IRqUKPaYsmVlImDnL0Q; lt.sig=lQG4uRgQCKBhNwWsNjK7H8Rx-RE; uid=1005291597; uid.sig=COTnRYOVUeGS1vQrK4dhMFoAiBA; _lxsdk=D67952C032FE11EC8F810FD937DF6B98E246DF6026234E5291A6457CD47C0BA5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1634883521,1634886779,1634888608,1634888660; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1634888660; _lxsdk_s=17ca6f44e62-dbe-90-729%7C1005291597%7C8",
        "Referer": "https://passport.meituan.com/"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("请求失败")


"""
                <dd>
                        <i class="board-index board-index-1">1</i>
<img data-src="https://p0.meituan.net/movie/005955214d5b3e50c910d7a511b0cb571445301.jpg@160w_220h_1e_1c" alt="哪吒之魔童降世" class="board-img" />
    </a>

    <p class="name"><a href="/films/1211270" title="哪吒之魔童降世" data-act="boarditem-click" data-val="{movieId:1211270}">哪吒之魔童降世</a></p>
    <p class="star">
                主演：吕艳婷,囧森瑟夫,瀚墨
        </p>
        <p class="releasetime">上映时间：2019-07-26</p> 

        <p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>   
"""


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>'
                         '.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'
                         '.*?star">(.*?)</p>'
                         '.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>'
                         '.*?fraction.*?(\d)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)

    for item in items:
        yield {
            "排行": item[0],
            "图片": item[1],
            "标题": item[2].strip(),
            "主演": item[3].strip()[3:],
            "上映时间": item[4].strip()[5:],
            "评分": item[5].strip() + item[6].strip()
        }

def write_to_file(content):
    with open("maoyan.md", 'a', encoding="utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')




def main(offset):
    url = "https://maoyan.com/board/4?offset="+ str(offset)
    html = get_one_page(url)
    # print(html)
    item = parse_one_page(html)
    # print(item)
    for items in item:
        write_to_file(items)

if __name__ == '__main__':
    p = Pool()
    p.map(main,[i*10 for i in range(10)] )