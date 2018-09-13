# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import requests
import json
import re
import config

def get_check_cookies():
    sql='select * from qq_cookies'
    sql_res=config.mysql_local_select(sql)
    id_list=[]
    for i in sql_res:
        id = i['id']
        cookies = str(i['cookies'])
        update_time = i['update_time']
        id_list.append([id, cookies, update_time])
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'content-type': 'text/html; charset=utf-8',
            'Referer': 'https://qun.qq.com/member.html',
            'Cookie': cookies
        }


        url_chkec = 'https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
        bkn = get_bkn(cookies)
        try:
            data = {
                'bkn': bkn[1]
            }
        except :
            return 'data err'

        params = urllib.urlencode(data)
        req = requests.post(url_chkec, data=params, headers=headers)
        content = req.json()
        #return content
        if content['ec'] == 0:
            return ('开始请求数据')
        else:
            cookies = raw_input("需要重新登陆,输入账号{}的cookies：".format(id))
            list = cookies.split('; ')

            try:
                dis_qq = {}
                for i in range(0, len(list)):
                    dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
            except :
                print "输入有误，重新输入"
                cookies = raw_input("需要重新登陆,输入账号{}的cookies：".format(id))
                list = cookies.split('; ')
                try:
                    dis_qq = {}
                    for i in range(0, len(list)):
                        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
                except:
                    return "输入有误，重新运行程序"

            print ("处理中……")
            sql_update = """update qq_cookies set cookies=\"{}\" where id={}""".format(cookies, id)
            if config.mysql_local_update_insert(sql_update)==1:
                return "可以开始请求数据"
            else:
                return "数据写入失败"

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


print get_check_cookies()