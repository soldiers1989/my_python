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
def headers(id):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
        'Referer': 'http://www.dianyuan.com',
        'Cookie': id
    }
    return headers

ids=['__site_info__=865ea11d8c08408bed89b1a3bb822561; __time_a_=8709512942; _user_account_=66ef4d49092fd24bd4bbab9f6e9d4e33; _uid___=597315; username=FAE%E7%94%B5%E6%BA%90;',
     '__site_info__=96de33f111020d6cd644998f0206b4de; __time_a_=8709512944; _user_account_=d69aab7325a0b648b1de9c4f71e41cd8; _uid___=572136; username=%E7%94%B5%E6%BA%90%E7%B1%BB_FAE;',
     '__site_info__=2102553e3142fa6f3da36e5f495f8e64; __time_a_=8709512945; _user_account_=c4d7e818aa773afe94d3308a5741e621; _uid___=988290; username=%E7%94%B5%E6%BA%90_FAE;',
     '__site_info__=5445afa4227ed014d370b1c21cc3a8f2; __time_a_=8709512947; _user_account_=43ec23f95afc0ffa3f6ac01a52f1aabc; _uid___=281567; username=%E7%94%B5%E6%BA%90FAE;']
sql_get_last_max='select tid from dianyuanwang_luntan'
cur.execute(sql_get_last_max)
re=cur.fetchall()
a_tid=[]
for i in range(len(re)):
    a_tid.append(re[i]['tid'])

max_tid=2434075
m_tid=max_tid-100
conntents=["""有IC应用问题？可以到斗石FAE，找专业FAE解决问题。还可以申请成为认证工程师，利用闲暇时间，轻松赚钱。各位有兴趣可以去看下。网址：http://doorock.com 传送门在这→→→→<a href="http://www.doorock.com">斗石FAE</a>""",
          """说个题外话，最近在斗石网兼职做FAE，能赚点私房钱。还有人知道这个吗，有还没注册的可以去看下,目前还是开放的,据说是限时开放注册的,大家抓紧哈!网址：http://doorock.com 传送门在这→→→→<a href="http://www.doorock.com">斗石FAE</a>""",
          """斗石FAE,你值得拥有！这年头都不容易啊""",
           """借宝地，打个广告  斗石FAE，全国首家FAE服务共享平台！网址：<a href="http://doorock.com">http://doorock.com</a>""",
         """用你的技术创造更高的价值——斗石FAE!加入斗石，实现你的财务自由""",
          """原厂技术支持难？不如来斗石网。200+资深工程师，24小时为您提供技术支持！专注电子行业,IC应用的技术支持"""]

for x in range(m_tid,max_tid):
    if x in a_tid:
        continue
    else:
        url = 'http://www.dianyuan.com/index.php?do=community_post_submit'
        pid = get_message_id('http://www.dianyuan.com/bbs/' + str(x) + '.html')
        if pid == 1:
            sql = 'insert into dianyuanwang_luntan set tid={},have_send=1'.format(x)
            cur.execute(sql)
            conn.commit()
        else:
            conntent=conntents[x%6]
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
            id_n=x%4
            id=ids[id_n]
            print(soup_text_3(headers(id), url, datas))
            print(x)
cur.close()

