# coding=utf-8

#跳板机访问远程地址

import pymysql


from sshtunnel import SSHTunnelForwarder
with SSHTunnelForwarder(
        ('106.14.34.24', 15555),
        ssh_username="lfj",
        ssh_password="hnmsy!!!@)",  # 登陆跳板
        remote_bind_address=('localhost', 3306)) as server:  # 远程地址
    server.start()
    p=server.local_bind_port
    conn_ssh = pymysql.connect(host='127.0.0.1',
                       port=p,
                       user='lfj',
                       password='123123',
                       db='hntx_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
    cur_ssh = conn_ssh.cursor()
    cur_ssh.execute("select max(id) as id from gq_manage_record")
    re_ssh=cur_ssh.fetchone()
    cur_ssh.close()
    conn_ssh.close()
    server.stop()
print re_ssh

