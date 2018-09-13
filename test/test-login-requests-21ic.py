# -*- coding: utf-8 -*-
import requests
import time
import sqlite3


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
        sql = """select cookies from cookies where username = \"{}\"""".format(username)
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
        for i in re :
            if time.time()-i[0]>86400:
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
                sql="""insert into cookies values ({},\"{}\",{})""".format(time.time(),cookie,username)
                return cookie
            else:
                sql = """select cookies from cookies where username = \"{}\"""".format(username)
                db = sqlite3.connect('db.db')
                cur = db.cursor()
                cur.execute(sql)
                re=cur.fetchone()
                return re[0]

username='黄黄'
password='ds1234567890'

print(get_cookies(username,password))