# -*- coding: utf-8 -*-
import pymysql

#连接本地数据库，并执行sql语句输出
#自动判断增删改查类型
#非查询语句，返回down
def sql_connect(host='127.0.0.1',user='root',password='root',db_name='',sql=''):
    conn = pymysql.connect(host=host,
                       port=3306,
                       user=user,
                       password=password,
                       db=db_name,
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    if "select" in sql:
        re = cur.fetchall()
        return re
    elif "SELECT" in sql:
        re = cur.fetchall()
        return re
    else:
        conn.commit()
        cur.close()
        conn.close()
        return 'down!'
