# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
import requests
from bs4 import BeautifulSoup
import pymysql
import random
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='company_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()

#模拟请求函数
def soup_text_3(headers,url,post):
    params = urllib.urlencode(post)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text

def get_message_id(url):
    request = requests.get(url)
    response = request.text
    soup = BeautifulSoup(response, "html.parser")
    re = soup.select('.gtr')
    x = []
    for xx in re:
        x.append(xx['id'])
    if len(x)==0:
        return 1
    else:
        return (x[0][1:10])

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
    'Referer': 'http://www.dianyuan.com',
    'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA1259646395=1453125441-1530676541-null%7C1530676541; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1530674568; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; acw_tc=AQAAAB5NZ0li9QIAqw7dciPYPUbXr+4e; PHPSESSID=8a2n8t4jvbf3a783dqmripbkm0; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1530838504; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; aa967c72b1dffdef64b9a4d61707f234=36b8c940e961d7beddb44aabbee1d12b; afpCT=1; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531098418; gdxidpyhxdE=c25rjwhnJXMI%5C1T9j5jxLDu2CchkkL1e%2F%5CUYI6R%5C7egSBwuLaoQsN31RHgrQNC4Ijdlm4j0xoPcoJgeluZIwMPq1%2Bap9nJTNvdVTkW9D%2BlKZiH4q5lhe1jWvS4iTAx7QOrRGyDL0aBEmUtsdOndOm8%5CVR0ErYREPVuYpjNULlwokTyJU%3A1531099323649; __site_info__=62e376bcb68dc19e1b73f6f443f62567; __time_a_=8709518605; _user_account_=aba2a43510090adeedbb04a80bacc04d; _uid___=577288; username=ahaufox; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531098436; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1531096800; Netbroad_Dianyuanpush_key=0892CQkBAFRVBlMFVAEDVQVUAAJQAABfVFEFA1VRDAxWVgc; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1531096632; CNZZDATA1253348660=774631188-1530681865-null%7C1531097410'}
sql_get_last_max='select tid from dianyuanwang_luntan'
cur.execute(sql_get_last_max)
re=cur.fetchall()
a_tid=[]
for i in range(len(re)):
    a_tid.append(re[i]['tid'])

max_tid=2436014
m_tid=max_tid-11

conntent="""有IC应用问题？可以到斗石FAE，找专业FAE解决问题。还可以申请成为认证工程师，利用闲暇时间，轻松赚钱。各位有兴趣可以去看下。网址：http://doorock.com 传送门在这→→→→<a href="http://www.doorock.com">斗石FAE</a>"""

for x in range(m_tid,max_tid):
    if x in a_tid:
        print("重复"+str(x))
    else:
        url = 'http://www.dianyuan.com/index.php?do=community_post_submit'
        pid = get_message_id('http://www.dianyuan.com/bbs/' + str(x) + '.html')
        if pid == 1:
            print('帖子不存在')
        else:
            datas = {
                'content': conntent,
                'pid': pid,
                'id': '0',
                'tid': x,
                'from': '0'
            }
            sql = 'insert into dianyuanwang_luntan set tid={},have_send=1'.format(x)
            cur.execute(sql)
            conn.commit()
            soup_text_3(headers, url, datas)
            print(x)
            time.sleep(random.randint(1, 11))
cur.close()

