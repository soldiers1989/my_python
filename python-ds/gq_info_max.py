# coding=utf-8

#通过ssh登陆，取最新更新的用户信息
import pymysql
from sshtunnel import SSHTunnelForwarder
def ssh_con_myql(sql,database):
    with SSHTunnelForwarder(
            ('139.196.173.61', 15555),
            ssh_username="lfj",
            ssh_password="nyycbdHJ69",
            remote_bind_address=('localhost', 3306)) as server:
        server.start()
        p = server.local_bind_port
        conn_t = pymysql.connect(host='127.0.0.1',
                                 port=p,
                                 user='lfj',
                                 password='123321',
                                 db=database,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        conn_t = conn_t.cursor()
        conn_t.execute(sql)
        re = conn_t.fetchall()
        conn_t.close()
        return re
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur_o = conn.cursor()

def get_last_update(gq_id):
    sql_local_max = 'select max(id) as id from gq_info_max'
    cur_o.execute(sql_local_max)
    re = cur_o.fetchone()
    if re['id'] == None:
        real = 1
    else:
        real = re['id'] + 1
    if real==gq_id:
        return ('没有需要更新的数据')
    else:
        for s in range(real, gq_id):
            print(s)
            sql_insert = """insert into gq_info(id,mid,member_id,product_name,product_spec,price,pro_name,city_name,country_name,is_warrant,is_sale,add_time,unit,view_times,contact_times,type_id,is_audit,operation_type,operation_time )  sELECT gq_supply.id,gq_manage_record.id as mid,gq_supply.member_id,gq_supply.product_name,product_spec,price,pro_name,city_name,country_name,is_warrant,is_sale,add_time,unit,view_times,contact_times,type_id,is_audit,operation_type,operation_time FROM gq_supply left join gq_manage_record ON gq_manage_record.gq_id=gq_supply.id WHERE gq_supply.id={} ORDER BY mid""".format(
                s)
            cur_o.execute(sql_insert)
            conn.commit()
        sql_max_c = 'select id,max(mid) as mid from gq_info group by id'
        cur_o.execute(sql_max_c)
        res = cur_o.fetchall()
        sql_max1 = 'DROP TABLE IF EXISTS `gq_info_max`'
        sql_max2 = 'CREATE table gq_info_max (`id` int(11) DEFAULT NULL,`mid` int(11) DEFAULT NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8'
        cur_o.execute(sql_max1)
        conn.commit()
        cur_o.execute(sql_max2)
        conn.commit()
        for i in range(0, len(res)):
            if res[i]['mid'] == None:
                res[i]['mid'] = 0
            else:
                res[i]['mid']
            if res[i]['id'] == None:
                res[i]['id'] = 0
            else:
                res[i]['id']
            sql_max3 = 'insert into gq_info_max (id,mid) values ({},{})'.format(res[i]['id'], res[i]['mid'])
            cur_o.execute(sql_max3)
            conn.commit()


cur_o.execute('select max(id) as id from gq_supply')
re=cur_o.fetchone()
print(get_last_update(re['id']))