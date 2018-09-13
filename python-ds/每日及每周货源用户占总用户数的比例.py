# coding=utf-8
import pymysql
import time
#hn_member更新到member_last_update
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql_all="""SELECT DISTINCT dau_time_strptime FROM hntx_mc_dau """
cur.execute(sql_all)
re=cur.fetchall()
#取所有日期


sql_drop="""DROP TABLE IF EXISTS `dau_number`;"""
cur.execute(sql_drop)
conn.commit()
#删除老表


sql_creat="""CREATE TABLE `dau_number` (
  `day` VARCHAR (20) NOT NULL,
  `dau_number` int(11) DEFAULT NULL,
  `member_number` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
cur.execute(sql_creat)
conn.commit()
#创建新表

for i in range(0,len(re)):
    sql_day="""SELECT count(user_id) FROM hntx_mc_dau WHERE dau_time_strptime={}""".format(re[i]['dau_time_strptime'])
    cur.execute(sql_day)
    re_day=cur.fetchone()
    count=re_day['count(user_id)']
    #每日的活跃用户量

    sql_member_number="""select count(member_id) from hn_member WHERE member_register_time <{}""".format(re[i]['dau_time_strptime']+86400)
    cur.execute(sql_member_number)
    re_sql_member_number=cur.fetchone()
    member_number=re_sql_member_number['count(member_id)']
    #截至当日的注册会员总数



    sql_insert="""insert into dau_number SET day={},dau_number={},member_number={}""".format(re[i]['dau_time_strptime'],count,member_number)
    cur.execute(sql_insert)
    conn.commit()
    # 数据写入新表
    print (re[i]['dau_time_strptime'])

