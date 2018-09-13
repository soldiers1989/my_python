# -*- coding:gb2312 -*-
import pymysql

def mysql_local_select(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='company_tel',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
    except pymysql.Error,e:
        return e
    else:
        try:
            cur.execute(sql)
            re=cur.fetchall()
            cur.close()
            conn.close()
        except conn.Error, e:
            return e
        else:
            return re

def mysql_local_update_insert(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='company_tel',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
    except pymysql.Error,e:
        return e
    else:
        try:
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except conn.Error, e:
            return e
        else:
            return 1
