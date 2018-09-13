# -*- coding: utf-8 -*-
import pymysql
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
def soup_text_1(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='catch_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql_member='select tel   from tel_baoming WHERE pro is NULL  '
cur.execute(sql_member)
re=cur.fetchall()
if len(re)==0:
    print("无待处理数据")
else:
    for i in range(0, len(re)):
        tel = re[i]['tel']
        url = 'http://apis.juhe.cn/mobile/get?phone={}&key=54db270eb62b90ba50b0669baf95c567'.format(tel)
        res = soup_text_1(url)
        res_json = json.loads(res)
        code = int(res_json['resultcode'].encode('UTF-8'))
        if code == 200:
            pro = res_json['result']['province'].encode('UTF-8')
            city = res_json['result']['city'].encode('UTF-8')
            update_sql = 'update tel_baoming set pro=\'{}\', city=\'{}\' where tel={}'.format(pro, city, tel)
            cur.execute(update_sql)
            conn.commit()
        else:
            update_sql = 'update tel_baoming set pro={}}, city=NULL where tel={}'.format("错误",tel)
            cur.execute(update_sql)
            conn.commit()
    print "完成！"




