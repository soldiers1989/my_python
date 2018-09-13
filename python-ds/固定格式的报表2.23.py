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
    cur.execute("""SELECT member_tel as '手机号',producing_place as '用苗地',product_name as '产品名称',spec_list as '产品规格',want_count as '需求数量' FROM gq_dys_want_to_buy left join hn_member on want_user_id=member_id WHERE want_date>1519488000""")
    re=cur.fetchall()
    print(re[9])
    server.stop()
