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
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

sql_member='select member_id as id ,member_tel as tel from hn_member'
cur.execute(sql_member)
re=cur.fetchall()
for i in range(0, len(re)):
    id=re[i]['id']
    tel=re[i]['tel']
    sql_get_loc="""select location_pro,location_city from tel_location_copy WHERE tel={}""".format(tel)
    cur.execute(sql_get_loc)
    re_sql_get_loc = cur.fetchone()
    if re_sql_get_loc == None:
        update_sql = """insert into tel_location VALUES ({},{},\'{}\',\'{}\')""".format(id, tel, '0', '0')
    else:
        pro = re_sql_get_loc['location_pro'].encode('UTF-8')
        city = re_sql_get_loc['location_city'].encode('UTF-8')
        update_sql = """insert into tel_location VALUES ({},{},\"{}\",\"{}\")""".format(id, tel, pro, city)
    cur.execute(update_sql)
    conn.commit()
    print id
conn.close()
print('All down！')
