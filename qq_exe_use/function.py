# -*- coding:gb2312 -*-
from bs4 import BeautifulSoup
import urllib
import requests
import time
import re
import config


#判断特定id的cookies是否有效
#若有效，返回内容；无效：提示原因并更新
def check_cookies(cookies,id):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'content-type': 'text/html; charset=utf-8',
        'Referer': 'https://qun.qq.com/member.html',
        'Cookie': cookies
    }
    url_check = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
    get_bkn_res = get_bkn(cookies)
    bkn = get_bkn_res[1]
    id_need = int(get_bkn_res[0][0])
    id_list = []
    if id_need == id:
        try:
            data = {
                'bkn': bkn
            }
        except:
            return 'data err'
        params = urllib.urlencode(data)
        req = requests.post(url_check, data=params, headers=headers)
        content = req.json()
        if content['ec'] == 0:
            id_list.append([id, cookies])
            return content  # cookies验证没问题，自动返回list
        else:
            # 更新cookies
            cookies = raw_input("输入 {} 的 cookies：".format(id))
            try:
                list = cookies.split('; ')
                dis_qq = {}
                for i in range(0, len(list)):
                    dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
            except:
                print "格式有误，重新输入"
                cookies = raw_input("重新输入{}的 cookies：".format(id))
                try:
                    list = cookies.split('; ')
                    dis_qq = {}
                    for i in range(0, len(list)):
                        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
                except:
                    print "又输入错了，直接关了程序，然后再开一下！"
                    return 1
            print ("处理中……")
            sql_update = """update qq_cookies set cookies=\"{}\",update_time={} where id={}""".format(cookies,
                                                                                                      time.time(),
                                                                                                      id)
            if config.mysql_local_update_insert(sql_update) == 1:
                return "数据写入成功，需再次执行程序！"
            else:
                return "数据写入错误，联系程序员！"
    else:
        print "帐号和cookies不对应！"
        cookies = raw_input("需要重新登陆,输入账号{}的cookies：".format(id))
        try:
            list = cookies.split('; ')
            dis_qq = {}
            for i in range(0, len(list)):
                dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
        except:
            print "wrong,try again!"
            cookies = raw_input("input {}`s cookies again：".format(id))
            try:
                list = cookies.split('; ')
                dis_qq = {}
                for i in range(0, len(list)):
                    dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
            except:
                print "input {}`s cookies again："
                return 1
        print ("处理中……")
        sql_update = """update qq_cookies set cookies=\"{}\",update_time={} where id={}""".format(cookies,
                                                                                                  time.time(),
                                                                                                  id)
        if config.mysql_local_update_insert(sql_update) == 1:
            print "数据写入成功，需再次执行程序！"
            return 1
        else:
            print "数据写入错误，联系程序员！"
            return 1

#返回bkn和id的数组0:id 1 :bkn
def get_bkn(cookies):
    list = cookies.split('; ')
    hash = 5381
    dis_qq = {}
    for i in range(0, len(list)):
        try:
            for i in range(0, len(list)):
                dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
        except IndexError, e:
            return e
        else:
            skey = dis_qq['skey']
            qq_id = re.findall('[1-9][0-9]{4,}', dis_qq['uin'])
            for i in xrange(len(skey)):
                hash += (hash << 5) + ord(skey[i])
                i += 1
            bkn = hash & 2147483647
            return [qq_id, bkn]


#返回群id数组
def get_qun_id(cookies):
    id=int(get_bkn(cookies)[0][0])
    qun_id_list = []
    re_check=check_cookies(cookies,id)
    if re_check==1:
        return 'err'
    else:
        if re_check['ec'] == 0:
            list_json=re_check['join']
            list_max = len(list_json)
            for i in xrange(0, list_max):
                j=[list_json[i]['gc'],list_json[i]['gn']]
                qun_id_list.append( j)
            return qun_id_list
        else:
            return "请再次运行程序！"

#返回数组集合 qq id，群id  所有者id
def get_qun_user_id(qun_id,cookies):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'content-type': 'text/html; charset=utf-8',
        'Referer': 'https://qun.qq.com/member.html',
        'Cookie': cookies
    }
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'
    get_bkn_res = get_bkn(cookies)
    bkn = get_bkn_res[1]
    id_need = int(get_bkn_res[0][0])
    id_list = []
    try:
        data = {
            'gc': qun_id,
            'st': 0,
            'end': 0,
            'bkn': bkn
        }
    except:
        return 'data err'
    params = urllib.urlencode(data)
    request = requests.post(url=url, data=params, headers=headers)
    res_json = request.json()
    if res_json['ec']!=0:
        return
    else:
        s = res_json['count']
        data = {
            'gc': qun_id,
            'st': 0,
            'end': s,
            'bkn': bkn
        }
        params = urllib.urlencode(data)
        request = requests.post(url=url, data=params, headers=headers)
        res_json = request.json()
        member_list = res_json['mems']
        for i in xrange(0, len(member_list)):
            uin = member_list[i]['uin']
            id_list.append([uin, qun_id, id_need])
        if len(id_list)==0:
            pass
        else:
            return id_list



#返回0 无需写入，1写入成功，其他 具体错误
#QQ号，所属群id，来源查询QQ号
def insert_qq_id(list):
    sql_i = 'insert into qq_id set id={},qun_id={},qq_ower={}'.format(list[0], list[1], list[2])
    re = config.mysql_local_update_insert(sql_i)
    return re

#从数据库去cookies
#返回1：没这个cookies；0:数组状态0及具体cookies
def get_cookies(qq_id):
    sql = 'select * from qq_cookies where id={}'.format(qq_id)
    sql_res = config.mysql_local_select(sql)
    if len(sql_res) == 0:
        print '没有这个QQ号的信息'
        return 1
    else:
        cookies=sql_res[0]['cookies']
        return [0,cookies]


#检查群id是否已经记录
#已存在，返回0，否则返回1
def check_qunid(qun_id):
    sql = 'select * from qq_qun where id={}'.format(qun_id)
    re = config.mysql_local_select(sql)
    if len(re) == 0:
        return 1
    else:
        return 0

#新的qun_id写入数据库，同时拿出所有qun_id待处理的
#数组集合：qun_id，from_id
def get_qun_id_need(cookies,id):
    check_cookie = check_cookies(cookies, id)
    if check_cookie == 1:
        return check_cookie
    else:
        qun_id_list = get_qun_id(cookies)
        for i in xrange(0, len(qun_id_list)):
            qun_id = qun_id_list[i][0]
            qun_name = qun_id_list[i][1]
            qun_name = qun_name.encode('utf-8')
            if check_qunid(qun_id) == 1:
                sql = 'insert into qq_qun set id={},name=\"{}\",from_id={}'.format(qun_id, qun_name, id)
                re = config.mysql_local_update_insert(sql)
                print re
            else:
                pass
        sql = 'select id as qun_id,from_id from qq_qun where is_err is NULL '
        return  config.mysql_local_select(sql)


def update_qq_qun_list(qun_id):
    sql='update qq_qun set is_err=0 where id={}'.format(qun_id)
    return config.mysql_local_update_insert(sql)

