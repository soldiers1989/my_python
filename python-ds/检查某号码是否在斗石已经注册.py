# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib
import urllib2

# 获取tel的函数
def get_tel(postData):
    url = 'http://www.doorock.com/getVerificationCode?t=0.33641635514907375'
    data = urllib.urlencode(postData)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255',
        'Accept - Language':' zh - CN, zh;q = 0.9',
        'X - Requested - With':'XMLHttpRequest',
        'Referer':'http://www.doorock.com/getVerificationCode?t=0.33641635514907375',
        'Connection': 'keep - alive'
        }
    request = urllib2.Request(url, data, headers=headers)
    response = urllib2.urlopen(request)
    # 获取指定数据
    soup = BeautifulSoup(response, "html.parser")
    return soup

postData = {'useraccount': '17314968109'}
print get_tel(postData)