# -*- coding: utf-8 -*-
import requests
import time
import sqlite3
import json


def get_cookies(username,password):
    db = sqlite3.connect('db.db')
    sql = """CREATE TABLE "cookies" ("update_time"  INTEGER,"cookies"  TEXT,"username"  TEXT)"""
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
        db.close()
    except:
        pass
    # 解决建表问题和判断表是否存在，不存在数据库，建数据库，不存在表，建表。
        sql = """select * from cookies where username = \"{}\"""".format(username)
    cur = db.cursor()
    cur.execute(sql)
    re=cur.fetchall()
    if re==[]:
        s = requests.session()
        postData = {'mod': 'logging',
                    'action': 'login',
                    'loginsubmit': 'yes',
                    'infloat': 'yes',
                    'lssubmit': 'yes',
                    'inajax': 1,
                    'username': username,
                    'password': password,
                    'quickforward': 'yes',
                    'handlekey': 'ls'}
        s.post(url='http://bbs.21ic.com/member.php', data=postData)
        cookie = s.cookies.get_dict()
        sql = """insert into cookies values ({},\"{}\",\"{}\")""".format(time.time(), cookie, username)
        db = sqlite3.connect('db.db')
        cur = db.cursor()
        cur.execute(sql)
        db.commit()
        db.close()
        return cookie
    else:
        if time.time() - re[0][0] > 86400:
            s = requests.session()
            postData = {'mod': 'logging',
                        'action': 'login',
                        'loginsubmit': 'yes',
                        'infloat': 'yes',
                        'lssubmit': 'yes',
                        'inajax': 1,
                        'username': username,
                        'password': password,
                        'quickforward': 'yes',
                        'handlekey': 'ls'}
            s.post(url='http://bbs.21ic.com/member.php', data=postData)
            cookie = s.cookies.get_dict()
            sql = """insert into cookies values ({},\"{}\",{})""".format(time.time(), cookie, username)
            return cookie
        else:
            sql = """select cookies from cookies where username = \"{}\"""".format(username)
            db = sqlite3.connect('db.db')
            cur = db.cursor()
            cur.execute(sql)
            re = cur.fetchone()
            return re[0]

username='黄黄'
password='ds1234567890'

cookies=get_cookies(username,password)
print(str(cookies))

print(json.loads(cookies))
#cookie = cookies.get_dict()
#res=requests.post('https://cloud.flyme.cn/browser/index.jsp', cookies=cookies)

#print(res.content)