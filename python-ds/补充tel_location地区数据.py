# -*- coding: utf-8 -*-

#补充tel归属地数据
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
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql_member='select DISTINCT tel  from tel_location WHERE location_pro=\'0\''
cur.execute(sql_member)
re=cur.fetchall()
if len(re)==0:
    print("无待处理数据")
else:
    for i in range(0, len(re)):
        tel = re[i]['tel']
        url = 'http://apis.juhe.cn/mobile/get?phone={}&key=612971102857c0e7a016c466510f3c65'.format(tel)
        res = soup_text_1(url)
        res_json = json.loads(res)
        code = int(res_json['resultcode'].encode('UTF-8'))
        if code == 200:
            pro = res_json['result']['province'].encode('UTF-8')
            city = res_json['result']['city'].encode('UTF-8')
            update_sql = 'update tel_location set location_pro=\'{}\', location_city=\'{}\' where tel={}'.format(pro, city, tel)
            print (tel,pro,city)
            cur.execute(update_sql)
            conn.commit()
        else:
            update_sql = 'update tel_location set location_pro={}, location_city=NULL where tel={}'.format(0,tel)
            cur.execute(update_sql)
            conn.commit()
    print "完成！"

