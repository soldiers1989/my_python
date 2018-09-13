# coding=utf-8
import pymysql
import redis
#hn_member更新到member_last_update
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()



from sshtunnel import SSHTunnelForwarder
with SSHTunnelForwarder(
        ('139.196.176.177', 13019),
        ssh_username="lfj",
        ssh_password="AA642Wt97D",  # 登陆跳板

        remote_bind_address=('localhost', 6379)) as server:  # 远程地址
    server.start()
    p=server.local_bind_port
    pool =redis.ConnectionPool(host='139.196.173.61', port=p, password='sh9gUINm6uN1t9IR', decode_responses=True,db=11)
    r = redis.Redis(connection_pool=pool)
    dau = r.smembers('hntx_mc_dao:hntx:dayActiveUser:2017:10:01')
    server.stop()
print p
print dau

