# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import pymysql
import time
import requests


def get_user_uin(qun_id,user_id):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'content-type': 'text/html; charset=utf-8',
        'Referer': 'https://qun.qq.com/member.html',
        'Cookie': all_cookies[(user_id)]
    }
    url = 'https://qun.qq.com/cgi-bin/qun_mgr/search_group_members'

    #计算bkn
    hash = 5381
    list = all_cookies[(user_id)].split('; ')
    dis_qq = {}
    for i in range(0, len(list)):
        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
    skey = dis_qq['skey']
    for i in xrange(len(skey)):
        hash += (hash << 5) + ord(skey[i])
        i += 1
    bkn = hash & 2147483647
    # 计算bkn结束

    # 计算最大值
    data = {
        'gc': qun_id,
        'st': 0,
        'end': 0,
        'bkn': bkn
    }
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    res = BeautifulSoup(response, "html.parser").text
    res_json = json.loads(res)
    s = res_json['count']
    # 计算最大值结束

    # 请求结果页
    data = {
        'gc': qun_id,
        'st': 0,
        'end': s,
        'bkn': bkn
    }
    params = urllib.urlencode(data)
    req = requests.post(url=url, data=params, headers=headers)
    id_all = req.json()
    id_list = []
    for i in range(0, len(id_all['mems'])):
        id_list.append(id_all['mems'][i]['uin'])
    return (id_list)
    #请求结果页结束

#选择尚未拉去的QQ群号码
def get_qun_list():
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql = "select id,from_id from qq_qun where  is_err is null limit 11"
    cur.execute(sql)
    resp = cur.fetchall()
    list_qq = []
    for i in resp:
        qun_id = int(i['id'])
        user_id = str(i['from_id'])

        sss = get_user_uin(qun_id,user_id)
        print(sss)
        for j in sss:
            list_qq.append([j,qun_id,user_id])
    return list_qq
#选择尚未拉去的QQ群号码结束，返回list

all_cookies={}
#all_cookies['547575116']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3718780928; _qpsvr_localtk=0.957458186183098; ptisp=ctc; ptui_loginuin=547575116; pt2gguin=o0547575116; uin=o0547575116; skey=@KsSZ4ICm9; p_uin=o0547575116; pt4_token=Q9ThnfVYUJL8D2uDq6ZU-lWVA*yI4lDkFOEMGDl4xFI_; p_skey=w2OUYLMyB7hh-S6fQ86GKgS31NGgKXe2rCMVABWsMpo_'
#all_cookies['452193182']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3718780928; _qpsvr_localtk=0.957458186183098; ptisp=ctc; ptui_loginuin=547575116; pt2gguin=o0452193182; uin=o0452193182; skey=@rMYqeb2WF; p_uin=o0452193182; pt4_token=cbt5s7*81QU*cuzUQ9DAGqfj8YF4AsA8nvYtiZfYD1k_; p_skey=cme1HKOiPoH7KDm5*v85uqCTyqZ7ScTUEMuA61sPkDI_'
#all_cookies['1125354542']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3718780928; _qpsvr_localtk=0.957458186183098; ptisp=ctc; ptui_loginuin=547575116; pt2gguin=o1125354542; uin=o1125354542; skey=@oFdWjqgFL; p_uin=o1125354542; pt4_token=jUZ9Crre0-ZekRl8ZtKYCKZwf*EbX1nZLcgRQdN5NnQ_; p_skey=i9ABwWJ3efYavQzpnx2oRCHnn-VAHhBMadjJTtZprPo_'

conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

sql_get_cookies_547575116='select * from cookies where id=547575116'
cur.execute(sql_get_cookies_547575116)
res_cookies=cur.fetchone()
if time.time()-res_cookies[0]["update_tme"]>20000:
    print ('需要更新登陆信息')
    all_cookies['547575116'] = raw_input("设置547575116的登陆信息")
    all_cookies['452193182'] = raw_input("设置452193182的登陆信息")
    all_cookies['1125354542'] = raw_input("设置1125354542的登陆信息")
else:
    all_cookies['547575116'] = res_cookies['547575116']
    all_cookies['452193182'] = res_cookies['452193182']
    all_cookies['1125354542'] = res_cookies['1125354542']

for m in get_qun_list():
        sql_i = 'insert into qq_id set id={},qun_id={},qq_ower={}'.format(m[0], m[1], m[2])
        cur.execute(sql_i)
        conn.commit()
        sql_u = "update qq_qun set is_err=0 where  id={}".format(m[1])
        cur.execute(sql_u)
        conn.commit()
        print(m)

