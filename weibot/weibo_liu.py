# -*- coding:utf8 -*-
import requests
import re
import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='yunfae',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
def get_weibo_text(num):
    for j in range(0,num):
        url = 'https://m.weibo.cn/api/container/getIndex?from=page_100505&containerid=1076031130237465&page={}'.format(j)
        res = requests.request(method='get', url=url).json()['data']['cards']
        for i in range(0, len(res)):
            res_data = (res[i]['mblog']['text'])
            res_data = re.sub(r'<(\S*?)[^>]*>.*?</\1>|<.*? />', '',
                              res_data)
            res_data=re.sub(r'[a-zA-z]+://[^\s]*','',res_data)
            sql = 'insert into liu set text=\"{}\"'.format(res_data)
            try:
                cur.execute(sql)
                conn.commit()
            except:
                pass
            print(res_data)

get_weibo_text(366)