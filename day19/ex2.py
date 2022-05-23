# 爬取沈腾微博内容 https://weibo.com/shenteng
# 通过Fetch/XHR找到接口
import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie': 'XSRF-TOKEN=h3e162ZHGJNA5XDZ9mfWjHhL; login_sid_t=e05bf87e21bdb29e82b9041b90ac4dd7; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=8781102137923.727.1651755336039; SINAGLOBAL=8781102137923.727.1651755336039; ULV=1651755336044:1:1:1:8781102137923.727.1651755336039:; wb_view_log=1920*10801; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFyGMIRMXjwSxrsYdY9DC2Z5JpX5o275NHD95QE1hz4So57S0nfWs4DqcjswJLoqPSL; SSOLoginState=1651755358; SUB=_2A25Pd7kODeRhGeRG6VsX8C7LwzmIHXVsBK3GrDV8PUNbmtB-LWqkkW9NTcDmlYNxLSIP8ThlAKioYEP2gWNOrN_Q; ALF=1683291358; WBPSESS=OKF-ZiLobWqoaRaS8aE0CjsjtdMoLrEBEjJIx2E1gMUlZC_f0oxcd8CWIduo2dPOqNAgLegLg4YMR40WMVWt24TSbmtg-rHRabZRIk4uAZNE2bqKHNIrXrMYmoZ0-ZUA3UrWMuR9CRXOvgsrNE0ykQ=='
}

uid = '1782432341'  # 沈腾id号
page = 0
while page < 3:
    url = f'https://weibo.com/ajax/statuses/mymblog?uid={uid}&page={page}&feature=0'
    page += 1
    html = requests.get(url, headers=headers).text  # 字典格式
    data = json.loads(html)  # 转成json数据格式
    lst = data['data']['list']  # 列表，字典的列表
    para = ''
    para = 'w' if page == 0 else 'a'
    with open('1.txt', para) as f:
        for i in lst:
            keys = ['created_at', 'text_raw', 'reposts_count', 'comments_count', 'attitudes_count']
            di = {'text_raw': '正文', 'created_at': '发布时间', 'reposts_count': '转发', 'comments_count': '评论', 'attitudes_count': '点赞'}

            for key in keys:
                if key == 'text_raw':
                    s = '【' + str(di[key]) + '】：\n' + str(i[key]) + '\n'  # '正文'+'：回车'+ 正文内容
                else:
                    s = '【' + str(di[key]) + '】：' + str(i[key]) + '\n'
                f.write(s)
                # print(s)
            f.write('-----------------\n\n')

