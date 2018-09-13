# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql
import json
import re
import time


def get_skey_qq_id(cookies):
    list = cookies.split('; ')
    dis_qq={}
    for i in range(0, len(list)):
        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
    seky=dis_qq['skey']
    qq_id=re.findall('[1-9][0-9]{4,}',dis_qq['uin'])
    return [seky,qq_id]

def GetBkn(skey):
    hash = 5381
    i=0
    for i in xrange(len(skey)):
        hash+=(hash<<5)+ord(skey[i])
        i+=1
    return hash & 2147483647

def GetGroupList(qq_cookies,skey):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'content-type':'text/html; charset=utf-8',
        'Referer': 'https://qun.qq.com/member.html',
        'Cookie':qq_cookies
    }
    url='https://qun.qq.com/cgi-bin/qun_mgr/get_group_list'
    data={
        'bkn':GetBkn(skey)
    }
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser",from_encoding='utf-8')
    return (soup.text)



all_cookies={}
all_cookies['547575116']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3723420672; pgv_info=ssid=s9198333854; _qpsvr_localtk=0.5459685421603142; ptisp=ctc; ptui_loginuin=547575116; pt2gguin=o0547575116; uin=o0547575116; skey=@WAqLaTsna; p_uin=o0547575116; pt4_token=XQ88SZyMlRoaqqwHubp6KDqVbSOevHvJ5sdMUSs4w08_; p_skey=ZHBUeqtV2qEea9VWdeh*IFqQzdndeC-Mhxp7Jl7JpyI_'
all_cookies['452193182']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3723420672; pgv_info=ssid=s9198333854; _qpsvr_localtk=0.5459685421603142; ptisp=ctc; ptui_loginuin=3287148066; pt2gguin=o0452193182; uin=o0452193182; skey=@rvjbnNUAB; p_uin=o0452193182; pt4_token=X9KM6C2EFMUF--*rUHlAOSfzuA*wYZMNn7dBHnYntmo_; p_skey=DeWNqYOAIx-W-3eWfxPzKtHJbyPpUN-LiBoZWZLd-bM_'
all_cookies['1125354542']='gr_user_id=648d5ce2-52eb-4d32-b1fc-4d9a71f37acb; pgv_pvi=9296552960; pgv_pvid=2622093390; RK=NAjxoQ5BaA; ptcz=6e8e5da7bb8b37cda07027f63b790af1541da3da19c0373d9b0a244159f2b38a; LW_sid=h155J2o8F4C8V6O0D7K909H4c6; LW_uid=V1d5Y24814H8I6t0r7l9Y924d7; eas_sid=Y185R22834t856U0s8o0M0X6R2; o_cookie=3287148066; _ga=GA1.2.1380941232.1530818815; pac_uid=1_3287148066; pgv_si=s3723420672; pgv_info=ssid=s9198333854; _qpsvr_localtk=0.5459685421603142; ptisp=ctc; ptui_loginuin=3287148066; pt2gguin=o1125354542; uin=o1125354542; skey=@F7dZjnm7g; p_uin=o1125354542; pt4_token=AeAh1O1lXxskJTlZQofezCOsSQYDFpgRqwAOwI*6O*Y_; p_skey=Cy6mAXTgZVtApzmuMN1PEbxZnrYeel26gvk3LhNAQBU_'

for i in all_cookies.keys():
    cookies=i
cookies=all_cookies['547575116']

skey_id=get_skey_qq_id(cookies)
respons=GetGroupList(cookies,skey_id[0])
respons = json.loads(respons)
gc=respons['join']
num_qq=len(respons['join'])
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='company_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
#获取群号码和群名称


for i in range(0,num_qq):
    print time.time()
    qun_name=gc[i]['gn'].encode('utf8')
    qun_id=gc[i]['gc']
    sql_check="select id from qq_qun"
    cur.execute(sql_check)
    re=cur.fetchall()
    id=[]
    for i in re:
        id.append(i['id'])
    if qun_id in id:
        pass
    else:
        sql="insert into qq_qun set id={},name=\'{}\',from_id={}".format(qun_id,qun_name,skey_id[1][0])
        cur.execute(sql)
        conn.commit()
        print(qun_name)
