# -*- coding:utf-8 -*-
# @time: 2021/5/20 5:20
# @Author: 韩国麦当劳
# @Environment: Python 3.7
# @file: 有情人终成眷属.py
import requests
import csv
import time
import json


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Referer": "https://weibo.com"
    }
    cookies = {
        "cookie": "SINAGLOBAL=3928074665190.3086.1636019958647; un=1869; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhAZYekBmZA3LZdKEIS5KaS5JpX5KMhUgL.FoMXeKzfSo2c1hB2dJLoIEYLxK-L1hnLBK.LxK-LBoMLBoiLi--Xi-zRiKnNi--NiKLFi-zRi--Xi-zRiKLWP7tt; ALF=1670307274; SSOLoginState=1638771274; SCF=AsRRFfUgn2Seh7_7V8X9VLnF8Qc8i73B5-XPXXyPSGE1xnHmfHkNG7ZttFem32cVYceBnFs4JGWs85Xc2CT4qLM.; SUB=_2A25MqdobDeRhGeFK6lAU9i_KwziIHXVv30zTrDV8PUNbmtANLRGlkW9NQ4CUmzvUczGmBIdXm9xFTD9XNxGZHoD7; _s_tentry=-; Apache=6884191078948.98.1638771278132; ULV=1638771278163:4:1:1:6884191078948.98.1638771278132:1638279357956; UOR=cn.bing.com,weibo.com,link.csdn.net; webim_unReadCount=%7B%22time%22%3A1638779056050%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A39%2C%22msgbox%22%3A0%7D"
    }
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)   # 加上3s 的延时防止被反爬
    return response.text


def save_data(data):
    title = ['text_raw', 'created_at', 'attitudes_count', 'comments_count', 'reposts_count']
    with open("data.txt", "a", encoding='utf-8', newline="")as fi:
        fi = csv.writer(fi)
        fi.writerow([data[i] for i in title])


if __name__ == '__main__':

    # uid = 1669879400
    # uid = 1878206395 https://weibo.com/ajax/statuses/mymblog?uid=1878206395&page=1&feature=0
    url = 'https://weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0'
    page = 1
    while 1:
        print(page)
        url = url.format(uid, page)
        html = get_html(url)
        responses = json.loads(html)
        blogs = responses['data']['list']
        if len(blogs) == 0:
            break
        data = {}   # 新建个字典用来存数据
        for blog in blogs:
            data['attitudes_count'] = blog['attitudes_count']   # 点赞数量
            data['comments_count'] = blog['comments_count']     # 评论数量(超过100万的只会显示100万)
            data['created_at'] = blog['created_at']     # 发布时间
            data['reposts_count'] = blog['reposts_count']     # 转发数量(超过100万的只会显示100万)
            data['text_raw'] = blog['text_raw']     # 博文正文文字数据
            save_data(data)
        page += 1
