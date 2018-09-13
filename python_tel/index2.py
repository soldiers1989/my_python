# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql
import json
import time
import hashlib

def soup_text_1(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text
#soup转text(传入email,url)
def soup_text_3(email,url,post):
    data = urllib.urlencode(post)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='company_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
x=222222

get_tel_sql =  'select tel from tel_all where pro is null or pro=\'{}\'  ORDER BY  tel desc  limit 2000,1000'.format(' ')
   #get_tel_sql = 'select tel from tel_all where pro is null limit {}'.format(x)
cur.execute(get_tel_sql)
ret = cur.fetchall()
x= cur.rowcount
list = []
for n in xrange(x):
     list.append(ret[n])

    #请求数据并写入数据库
h=1
m=200
tt = []
sum=0
ti="未知"
for i in xrange(x):
    t1 = time.time()
    url = 'http://apis.juhe.cn/mobile/get?phone={}&key=87d35c5f5d3735b390a85eb6ca369058'.format(list[i]['tel'])
    res = soup_text_1(url)
    res_json = json.loads(res)
    code = int(res_json['resultcode'].encode('UTF-8'))
    if code == 200:
        pro = res_json['result']['province'].encode('UTF-8')
        city = res_json['result']['city'].encode('UTF-8')
        # zip = res_json['result']['zip'].encode('UTF-8')
        company = res_json['result']['company'].encode('UTF-8')
        update_tel_sql = 'UPDATE tel_all SET pro =\'{}\',city=\'{}\',company=\'{}\'  WHERE tel ={} '.format(
            pro, city, company, list[i]['tel'])
        cur.execute(update_tel_sql)
        conn.commit()
    else:
        update_tel_sql = 'UPDATE tel_all SET pro =0,city=0, company=0  WHERE tel ={} '.format(list[i]['tel'])
        cur.execute(update_tel_sql)
        conn.commit()
    t2=time.time()
    t=t2-t1
    h += 1
    lef=len(list)-h
    if 0==i%m:
        tt = []
        sum=0
    else:
        tt.append(t*lef/60/60)
        for ii in tt:
            sum = sum + ii
        ti=sum/len(tt)
    if 0==i%m:
        print "剩余待处理：",lef
        print "预计耗时",ti,"小时"
        print "————————————————————————————————————————————————————————————————————————"
    else:
        continue

