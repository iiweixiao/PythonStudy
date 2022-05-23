import requests
import json

def parse_web(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36'
    }

    d1 = requests.get(url, headers=headers).text
    # print(d1)
    d2 = json.loads(d1)
    # print(d2)
    lis = d2['data']
    # print(lis)
    for item in lis:
        if item['target']['type'] == 'answer':
            title = item['target']['question']['title']
            _url = item['target']['question']['url']
            print(title, _url)
    aa = d2['paging']['next']
    aa = aa.replace('_v4?', '?')
    next_url = aa.replace('com', 'com/api/v4')
    return next_url

if __name__ == '__main__':
    url = 'https://www.zhihu.com/api/v4/topics/19556677/feeds/essence?offset=0&limit=10&'
    while True:
        url = parse_web(url)



#     # print(item['target'])
#     if item['target']['type'] == 'answer':
#         title = item['target']['question']['title']
#         url1 = item['target']['question']['url']
#         print(index, item, url1)