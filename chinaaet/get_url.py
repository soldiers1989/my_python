# -*- coding:utf-8 -*-
import urllib
import pymysql
from bs4 import BeautifulSoup
import re

def get_user_name(max_page):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    url='http://blog.chinaaet.com/posts?page={}'.format(max_page)
    request = urllib.Request(url=url)
    response = urllib.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    link_name=[]
    link_title=[]
    for link in soup.select('h3 > a'):
        w=link.get('href').encode('utf8')
        ww=re.sub (r'[a-zA-z]+://[^\s]*/p/','',link.get('href'))
        link_title.append(ww)
    for link in soup.select('a.user-name'):
        link_name.append(link.get('href')[25:99])
    for i in range(len(link_title)):
        sql = 'insert into chinaaet set link_name=\'{}\',link_title=\'{}\''.format(link_name[i].encode('utf8'),link_title[i].encode('utf8'))
        cur.execute(sql)
        conn.commit()
    sql_page='insert into chinaaet_page set page_id={}'.format(max_page)
    cur.execute(sql_page)
    conn.commit()
    return link_title#list数据

for i in range(1,1520):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql_page = 'select page_id from chinaaet_page'
    cur.execute(sql_page)
    res=cur.fetchall()
    re_id=[]
    for j in range(0,len(res)):
        re_id.append(res[j]['page_id'])
    if i in re_id:
        continue
    else:
        get_user_name(i)[1].encode('utf8')
        print(i)
print('down')
