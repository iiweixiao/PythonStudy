import requests  # 请求库
import json  # 解析库
import pymysql  # 数据保存库
import threading  # 提升爬取速度

# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="ws3614wx", db="zhihu")

# 创建游标
cusor = db.cursor()


# 创建数据库操作函数  传参
def insertDB(id, title, url):
    # 插入数据
    try:
        sql = "insert into questions values (%s, '%s', '%s')" % (id, title, url)
        cusor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)


def index_web_page(url):
    # 发送网络请求， 获取数据
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }

    html = requests.get(url, headers=headers)
    html.encoding = "Unicode"
    return html.text


def parseJson(html):
    json_data = json.loads(html)
    lst = json_data['data']
    nextUrl = json_data['paging']['next']
    if not lst:
        return

    for item in lst:
        type = item['target']['type']

        if type == "answer":
            # 回答
            question = item['target']['question']
            id = question['id']
            title = question['title']
            url = "http://api.zhihu.com/questions/" + str(id)
            print("回答:", id, title)
            # 保存到数据库
            insertDB(id, title, url)

    return nextUrl


def crawl_1(id):
    url = 'https://www.zhihu.com/api/v4/topics/' + id + '/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=0'
    while url:
        html = index_web_page(url)
        url = parseJson(html)
        print("讨论")




if __name__ == '__main__':
    id = "19656332"
    t1 = threading.Thread(target=crawl_1, args=(id,))
    t1.start()
