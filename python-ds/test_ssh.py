# coding=utf-8
import pymysql
from sshtunnel import SSHTunnelForwarder
with SSHTunnelForwarder(
        ('139.196.173.61', 15555),
        ssh_username="lfj",
        ssh_password="nyycbdHJ69",
        remote_bind_address=('localhost', 3306)) as server:
    server.start()
    p=server.local_bind_port
    print(p)
    conn = pymysql.connect(host='127.0.0.1',
                       port=p,
                       user='lfj',
                       password='123321',
                       db='hntx_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute("select max(id) as id from gq_manage_record")
    re=cur.fetchone()
    print(re)
    server.stop()