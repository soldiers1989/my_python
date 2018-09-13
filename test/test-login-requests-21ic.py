# -*- coding:utf8 -*-
from bs4 import BeautifulSoup
import requests
import time
import re



def get_cookies(username,password):
    try:
        f = open('test.txt', 'r+')
    except FileNotFoundError:
        pass
    else:
        result = f.read().split('\n')
        for i in result:
            up_time = i[1:11]
            x=i.split(',')
            print(x[2])

    s=requests.session()
    postData={'mod':'logging',
              'action':'login',
              'loginsubmit':'yes',
              'infloat':'yes',
              'lssubmit':'yes',
              'inajax':1,
              'username':username,
              'password':password,
              'quickforward':'yes',
              'handlekey':'ls'}
    rs=s.post(url='http://bbs.21ic.com/member.php',data=postData)
    cookie = s.cookies.get_dict()
    res = requests.post('http://my.21ic.com/member.php?mod=logging&action=login', cookies=cookie)
    try:
        c=cookie['www_username']
    except:
        return rs.content.decode()
    else:
        try:
            f = open('test.txt', 'r+')
        except FileNotFoundError:
            ff = open('test.txt', 'w')
            ff.close()
        else:
            t = {int(time.time()), username, cookie}
            f.read()
            f.write('\n')
            f.write(str(t))
            f.close()
        return 1

username='韦天王'
password='doushi123888'
#print(get_cookies(username,password))

try:
    f = open('test.txt', 'r+')
except FileNotFoundError:
    pass
else:
    result = f.read().split('\n')
    for i in result:
        up_time = i[1:11]
        user_name = i.split(',')
        if username==user_name:
            n=time.time()-int(up_time)
            if n>86400:

