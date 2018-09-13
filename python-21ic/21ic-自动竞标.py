# -*- coding:utf-8 -*-
#21IC 参与竞标
#自动登陆并参与竞标
import sys
import io
import urllib.request
import http.cookiejar
import pymysql
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# 改变标准输出的默认编码

#获取cooiks
def log_in(headers, data):
    # 登录时需要POST的数据
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    login_url = 'http://my.21ic.com/logging.php?action=login&index=1&loginsubmit=yes'
    # 构造登录请求
    req = urllib.request.Request(login_url, headers=headers, data=post_data)
    # 构造cookie
    cookie = http.cookiejar.CookieJar()
    # 由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    # 发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)
    # 构造访问请求
    return cookie

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
data = {"username": 'ahaufox',
        "password": '111111liu',
        "x": '88', "y": '14',
        'url': 'http://project.21ic.com'
        }

#获取cookie准备使用
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='21ic',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
def get_id():
    sql="select project_id from 21ic_project where is_down='0'"
    cur.execute(sql)
    conn.commit()
    re=cur.fetchall()
    return re
#获取待竞标ID


cookie = (log_in(headers, data))
pro_id=get_id()

#
#
#参与项目竞标
url = 'http://project.21ic.com/project/bid'
for i in range(0,len(get_id())):
    data_post = {"ask_money": '10000',
                 "period": '10',
                 "pt": '0',
                 "contact_name": '刘先生',
                 'contact_qq': '111111',
                 'plan': '面议',
                 "id": get_id()[i]['project_id']
                 }
    data_post_encode = urllib.parse.urlencode(data_post).encode('utf-8')
    req = urllib.request.Request(url, headers=headers, data=data_post_encode)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    resp = opener.open(req)
    print(resp.read().decode('utf-8'))
    sql = "update 21ic_project set  is_down='1' where project_id={}".format(get_id()[i]['project_id'])
    cur.execute(sql)
    conn.commit()
#
#参与竞标结束





