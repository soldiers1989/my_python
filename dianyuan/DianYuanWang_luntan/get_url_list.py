# -*- coding:utf-8 -*-
import urllib
import urllib2
import Queue
import requests
from bs4 import BeautifulSoup
import threading
import time

def get_message_id(url):
    request = requests.get(url)
    response = request.text
    soup = BeautifulSoup(response, "html.parser")
    re = soup.select('.gtr')
    x = []
    for i in re:
        x.append(i['id'])
    return (x[0][1:10])

url = 'http://www.dianyuan.com/bbs/2436001.html'
print get_message_id(url)