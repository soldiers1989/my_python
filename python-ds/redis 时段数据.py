# coding=utf-8
import pymysql
import redis
import datetime
import time
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='local_gongqiu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

pool = redis.ConnectionPool(host='139.196.173.61', port=6379, password='sh9gUINm6uN1t9IR', decode_responses=True,db=11)
r = redis.Redis(connection_pool=pool)
#时间处理函数
def get_date(befor,x):
    befor_y=datetime.datetime.fromtimestamp(befor).year
    befor_m=datetime.datetime.fromtimestamp(befor).month
    if datetime.datetime.fromtimestamp(befor).day<10:
        befor_d='0'+str(datetime.datetime.fromtimestamp(befor).day)
    else:
        befor_d = datetime.datetime.fromtimestamp(befor).day
    befor_ymd = "{}:{}:{}".format(befor_y, befor_m, befor_d)

    now_time=datetime.datetime.fromtimestamp(befor)
    new_y=(now_time + datetime.timedelta(days=x)).year
    if (now_time + datetime.timedelta(days=x)).month<10:
        new_m='0'+str((now_time + datetime.timedelta(days=x)).month)
    else:
        new_m=(now_time + datetime.timedelta(days=x)).month

    if (now_time + datetime.timedelta(days=x)).day<10:
        new_d='0'+str((now_time + datetime.timedelta(days=x)).day)
    else:
        new_d = (now_time + datetime.timedelta(days=x)).day
    new_ymd = "{}:{}:{}".format(new_y, new_m, new_d)

    date = []
    date.append(befor_ymd)
    date.append(befor_y)
    date.append(new_y)

    date.append(befor_m)
    date.append(new_m)

    date.append(befor_d)
    date.append(new_d)

    date.append(new_ymd)
    return date
#取到的数据写到mysql
#判断当前数据库中的值，若为空，则从2017年1月1日开始采数据
def insert_into_local(year,month,day,hour):
    sql = 'select max(hau_time_strptime) from  hntx_mc_dau'
    cur.execute(sql)
    ret = cur.fetchone()
    last_update=ret['max(hau_time_strptime)']
    conn.commit()
    if last_update == None:
        last_update=1514736000
    else:
        last_update=ret['max(hau_time_strptime)']

    new_time = int(time.mktime(time.strptime("{}:{}:{}:{}".format(year,month,day,hour), "%Y:%m:%d:%h")))
    if new_time>int(time.time()):
        print('日期大于当前时间！')
        return
    n=(new_time-last_update)
    if n>0:
        if n==86400:
            print ("数据不足一天，不给导出")
            return
        else:
            date_need = int(n / 86400)
            for i in range(1, date_need):
                t = get_date(last_update, i)[7]
                s = "hntx_mc_dao:hntx:dayActiveUser:{}".format(t)
                time_strptime = int(time.mktime(time.strptime(t, "%Y:%m:%d")))
                dau = r.smembers(s)
                if dau==set([]):
                    print ("无数据返回！")
                    return
                else:
                    for x in dau:
                        sql_i = "insert into hntx_mc_dau (dau_time,user_id,dau_time_strptime) VALUES (\'{}\',{},{})".format(
                            t, x, time_strptime)

                        cur.execute(sql_i)
                        conn.commit()
                    print(t)
    else:
        print("所有数据已经是最新的！")

insert_into_local(get_date(int(time.time()),0)[2],get_date(int(time.time()),0)[4],get_date(int(time.time()),0)[6])
#这个文件直接运行就行，直接把redis昨天的数据写到本地的。