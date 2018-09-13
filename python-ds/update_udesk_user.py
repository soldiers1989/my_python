# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql
import json
import time
import hashlib

def soup_text_1(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text

def get_open_api_auth_token(time):
    log_in_url = 'https://huinongtx.udesk.cn/open_api_v1/log_in'
    email='it@huinongtx.com'
    post_email_pass = {
        "email": email,
        "password": "czman890119"
    }
    data = urllib.urlencode(post_email_pass)
    request = urllib2.Request(log_in_url,data)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    res=soup.text
    res_json = json.loads(res)
    sign_need=email+'&'+res_json['open_api_auth_token']+'&'+str(time)
    sign=hashlib.sha1(sign_need).hexdigest()
    return sign
    #获取数据

def get_tel_from_udesk(email):
    t=int(time.time())
    #url='http://huinongtx.udesk.cn/open_api_v1/customers/custom_fields?email={}&timestamp={}&sign={}'.format(email,t,get_open_api_auth_token(t))
    url='http://huinongtx.udesk.cn/open_api_v1/customers/update_customer?type=cellphone&content=17374707003&email={}&timestamp={}&sign={}'.format(email,t,get_open_api_auth_token(t))
    nick_name = "刘飞箭"
    post={
        'customer':{
            'nick_name':nick_name,
            'custom_fields': {
                'SelectField_11168': [0]
            }
    }}
    jdata = json.dumps(post)
    request = urllib2.Request(url,jdata)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    rs= soup.text
    res_json = json.loads(rs)
    re_tel=[]
    #for i in range(0,10):
    #    re_tel.append(res_json['customers'][i]['cellphones'][0]['content'])
    #return re_tel
    return rs
#print get_tel_from_udesk('it@huinongtx.com')
print  get_tel_from_udesk('it@huinongtx.com')
