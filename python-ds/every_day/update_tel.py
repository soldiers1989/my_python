# -*- coding: utf-8 -*-


#查询归属地并更新到本地

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

sql_tel_location='select max(member_id) as id from tel_location'
cur.execute(sql_tel_location)
max_id=cur.fetchone()['id']
if max_id==None:
    max_id=0
else:
    max_id
sql_member='select member_id as id ,member_tel as tel from hn_member WHERE  member_id >{}'.format(max_id)
cur.execute(sql_member)
re=cur.fetchall()
for i in range(0, len(re)):
    id=re[i]['id']
    tel=re[i]['tel']
    url = 'http://apis.juhe.cn/mobile/get?phone={}&key=612971102857c0e7a016c466510f3c65'.format(tel)
    res = soup_text_1(url)
    res_json = json.loads(res)
    code = int(res_json['resultcode'].encode('UTF-8'))
    if code == 200:
        pro = res_json['result']['province'].encode('UTF-8')
        city = res_json['result']['city'].encode('UTF-8')
        update_sql ="""insert into tel_location VALUES ({},{},\"{}\",\"{}\")""".format(id,tel,pro,city)
        print tel
    elif code == 112:
        url = 'http://apis.juhe.cn/mobile/get?phone={}&key=54db270eb62b90ba50b0669baf95c567'.format(tel)
        res = soup_text_1(url)
        res_json = json.loads(res)
        code = int(res_json['resultcode'].encode('UTF-8'))
        if code==200:
            pro = res_json['result']['province'].encode('UTF-8')
            city = res_json['result']['city'].encode('UTF-8')
            update_sql = """insert into tel_location VALUES ({},{},\"{}\",\"{}\")""".format(id, tel, pro, city)
            print  tel
        elif code==112:
            print("超出今日可用查询额度！")
            break
    else:
        print 'x'
        update_sql ="""insert into tel_location VALUES ({},{},\'{}\',\'{}\')""".format(id,tel,'0','0')
    cur.execute(update_sql)
conn.commit()
conn.close()
print('手机号归属地查询完成！')
