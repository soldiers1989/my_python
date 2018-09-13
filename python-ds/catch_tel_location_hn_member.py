# -*- coding: utf-8 -*-

#从Udesk拿用户数据
#数据存如数据库
#查询手机归属地
#归属地到数据库


from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql
import json
import time
import hashlib

#请求Udesk，拿100条手机号数据
    #获取login
def get_open_api_auth_token(time):
    log_in_url = 'https://huinongtx.udesk.cn/open_api_v1/log_in'
    email='it@huinongtx.com'
    post_email_pass = {
        "email": email,
        "password": "czman890119"
    }

    res=soup_text_3(email,log_in_url,post_email_pass)
    res_json = json.loads(res)
    sign_need=email+'&'+res_json['open_api_auth_token']+'&'+str(time)
    sign=hashlib.sha1(sign_need).hexdigest()
    return sign
    #获取数据
#soup转text(仅传入url)
def soup_text_1(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text
#soup转text(传入email,url)
def soup_text_3(email,url,post):
    data = urllib.urlencode(post)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text
def get_tel_from_udesk(email):
    url='http://huinongtx.udesk.cn/open_api_v1/customers?page=1&page_size=10&email={}&timestamp={}&sign={}'.format(email,int(time.time()),get_open_api_auth_token(int(time.time())))
    rs= soup_text_1(url)
    res_json = json.loads(rs)
    re_tel=[]
    for i in range(0,10):
        re_tel.append(res_json['customers'][i]['cellphones'][0]['content'])
    return re_tel
#print get_tel_from_udesk('it@huinongtx.com')

#数据写入sql
    # 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='catch_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

#请求API，拿归属地数据

#phone = get_tel_from_udesk('it@huinongtx.com')[0]
def get_tel_info(x):
    get_tel_sql = 'select tel from catch_user_info where province= \'{}\'limit {}'.format('',x)
    cur.execute(get_tel_sql)
    ret = cur.fetchall()
    list = []
    for n in xrange(x):
        list.append(ret[n])
    for i in xrange(x):
        url = 'http://apis.juhe.cn/mobile/get?phone={}&key=54db270eb62b90ba50b0669baf95c567'.format(list[i]['tel'])
        res = soup_text_1(url)
        res_json = json.loads(res)
        code=int(res_json['resultcode'].encode('UTF-8'))
        if code==200:
            pro = res_json['result']['province'].encode('UTF-8')
            city = res_json['result']['city'].encode('UTF-8')
            zip = res_json['result']['zip'].encode('UTF-8')
            company = res_json['result']['company'].encode('UTF-8')
            update_tel_sql = 'UPDATE catch_user_info SET province =\'{}\',city=\'{}\',zip=\'{}\',company=\'{}\'  WHERE tel ={} '.format(
                pro, city, zip, company, list[i]['tel'])
            cur.execute(update_tel_sql)
            conn.commit()
        else:
           update_tel_sql = 'UPDATE catch_user_info SET province =0,city=0,zip=0,company=0  WHERE tel ={} '.format(list[i]['tel'])
           cur.execute(update_tel_sql)
           conn.commit()

get_tel_info(100)