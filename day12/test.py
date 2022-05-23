import json
import requests


def parse_url(index, url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.127 Safari/537.36'}

    # 网页数据  
    d1 = requests.get(url, headers=headers).text
    # 用json解析得到一个列表  
    d2 = json.loads(d1)
    # print(type(d2))  
    # 把字典中data键的值取出来，成为列表  
    lst = d2['data']


    for item in lst:
        if item['target']['type'] == 'answer':
            # print('haha')  # 测试正常  
            title = item['target']['question']['title']
            # print(title)  # test  
            _id = item['target']['question']['id']
            _token = item['target']['token']
            url = f'https://www.zhihu.com/question/{_id}/answer/{_token}'
            print(index, title, url)
            index += 1

    aa = d2['paging']['next']
    aa = aa.replace('_v4?', '?')
    next_url = aa.replace('com', 'com/api/v4')
    return next_url, index

index = 1
if __name__ == '__main__':
    topic = '19556677'  # 话题号
    url = f'https://www.zhihu.com/api/v4/topics/{topic}/feeds/essence?offset=10&limit=10&'
    while True:
        url, index = parse_url(index, url)
