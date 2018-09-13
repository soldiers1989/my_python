# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql
import re
import time
import requests

def GetBkn(skey):
    hash = 5381
    i=0
    for i in xrange(len(skey)):
        hash+=(hash<<5)+ord(skey[i])
        i+=1
    return hash & 2147483647
def insert_qun_id(cookies,keywords,page):
    url = 'http://qun.qq.com/cgi-bin/group_search/pc_group_search'
    headers={'Host': 'qun.qq.com',
             'Connection': 'keep-alive',

             'Accept': 'application/json, text/javascript, */*; q=0.01',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Origin': 'http://find.qq.com',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) QQ/9.0.4.23786 Chrome/43.0.2357.134 Safari/537.36 QBCore/3.43.915.400 QQBrowser/9.0.2524.400',
             'Referer': 'http://find.qq.com/index.html?version=1&im_version=5581&width=910&height=610&search_target=0',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'en-US,en;q=0.8',
             'Cookie': cookies}
    data1 = 'k=%E4%BA%A4%E5%8F%8B&n=8&st=1&iso=1&src=1&v=5581&bkn=1684538292&isRecommend=false&city_id=0&from=1&newSearch=true&keyword=%E7%94%B5%E6%BA%90%E7%94%B5%E5%AD%90&sort=0&wantnum=24&page=0&ldw=428160423'
    data = {}
    list = headers['Cookie'].split('; ')
    dis_qq = {}
    for i in range(0, len(list)):
        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
    skey = dis_qq['skey']
    for i in (data1.split('&')):
        j = i.split('=')
        data[j[0]] = j[1].encode('utf8')
    data['keyword'] = keywords
    data['bkn'] = GetBkn(skey)
    data['sort'] = 1
    data['page'] = page
    data['k'] = '交友'
    data = urllib.urlencode(data)
    req = requests.post(url=url, data=data, headers=headers)
    id_all = req.json()
    if id_all['endflag']==1:
        return 'err'
    else:
        if id_all.has_key('errcode'):
            return
        else:
            conn = pymysql.connect(host='127.0.0.1',
                                   port=3306,
                                   user='root',
                                   password='root',
                                   db='company_tel',
                                   charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)
            cur = conn.cursor()
            for i in range(0, len(id_all['group_list'])):
                qun_id = id_all['group_list'][i]['code']
                qun_name = id_all['group_list'][i]['name'].encode('utf-8')
                member_num=id_all['group_list'][i]['member_num']
                if member_num>20:
                    sql = 'select id from qun_id_check where id={}'.format(qun_id)
                    cur.execute(sql)
                    res = cur.fetchone()
                    if res is None:
                        try:
                            sql = 'insert into qun_id_check set id={},name=\"{}\",keywords=\"{}\",member_num={}'.format(
                                qun_id, qun_name,
                                keywords, member_num)
                            cur.execute(sql)
                            conn.commit()
                        except:
                            qun_name = '未知'
                            sql = 'insert into qun_id_check set id={},name=\"{}\",keywords=\"{}\",member_num={}'.format(qun_id,
                                                                                                                        qun_name,
                                                                                                                        keywords,member_num)
                            cur.execute(sql)
                            conn.commit()
                    else:
                        pass
                else:
                    pass
    return (page,qun_id,qun_name,member_num)


#keywords='电源电子'
#keywords='电源芯片'
#keywords='电源ic'
#keywords='电源管理IC'
#keywords='电源管理IC'
user_in=(raw_input("输入查询关键词："))
cookies=raw_input('输入任一cookies：')
keywords = "{}".format(user_in)

print (keywords)
print ('wait')
"""
page=1
print(insert_qun_id(keywords,page))
"""
for page in range(0,100):
    s=(insert_qun_id(cookies,keywords,page))
    if s=='err':
        break
    else:
        print s
        time.sleep(5)




