import requests
import json

def parse_sspai(index, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

    d1 = requests.get(url, headers=headers).text
    d2 = json.loads(d1)
    li = d2['data']
    for i, item in enumerate(li):
        title = item['title']
        _id = item['id']
        _url = f'https://sspai.com/post/{_id}'
        print(index*10+i-9, title, _url)


if __name__ == '__main__':
    index = 0
    while True:
        if index == 0:
            url = 'https://sspai.com/api/v1/article/tag/special/page/get?limit=10&offset=0&created_at=1651064431&tag=%E6%95%88%E7%8E%87%E6%8A%80%E5%B7%A7&search_type=1'
        else:
            url = f'https://sspai.com/api/v1/article/tag/special/page/get?limit=10&offset={index}0&created_at=1651064988&tag=%E6%95%88%E7%8E%87%E6%8A%80%E5%B7%A7&search_type=1'
        index += 1
        parse_sspai(index, url)