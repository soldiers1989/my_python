# coding=utf-8
import pymysql
from sshtunnel import SSHTunnelForwarder
import pymongo

def rds_mysql_sql_select(sql):
    with SSHTunnelForwarder(
            ('139.196.176.177', 13019),
            ssh_username="lfj",
            ssh_password="AA642Wt97D",
            remote_bind_address=('rr-uf647rm39z4909g8qgo.mysql.rds.aliyuncs.com', 3306)) as server:
        server.start()
        p = server.local_bind_port
        conn = pymysql.connect(host='127.0.0.1',
                               port=p,
                               user='hntx_operation',
                               password='hntx_operation@2018$%#',
                               db='hntx_gongqiu',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        try:
            cur.execute(sql)
            re = cur.fetchall()
            cur.close()
            conn.close()
        except conn.Error, e:
            server.stop()
            return e
        else:
            server.stop()
            return re

def mysql_local_select(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='local_gongqiu',
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
                               db='local_gongqiu',
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
            return "OK!"

def mongodb_local(insert):
    "连接mongodb数据库"
    if type(insert)!=str:
        return "需传入str格式参数！"
    else:
        try:
            client = pymongo.MongoClient('127.0.0.1', 27017)
            db = client.mydb
        except Exception as e:
            return e
        else:
            return db
