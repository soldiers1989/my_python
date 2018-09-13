# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import pymysql
import re

keywords="电子元器件"
def get_max_result_num(key):
    url = 'http://shouji.baidu.com/s?wd={}&data_type=&f=header_%40input%40btn_search'.format(key)
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'content-type': 'text/html; charset=utf-8',
        'host': 'shouji.baidu.com'
        }
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    soup=soup.select('#doc > div.result-summary > span.num')[0].getText()
    return int(soup)

def get_list(key):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    num=get_max_result_num(keywords)
    num=int(num/10)+1
    #name_list=[]
    for i in range(3,num):
        url='http://shouji.baidu.com/s?data_type=app&multi=0&ajax=1&wd={}&page={}'.format(key,i)
        headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'Accept-Language': 'zh-CN,zh;q=0.9',
                 'content-type':'text/html; charset=utf-8',
                 'host':'shouji.baidu.com'
                 }
        request = urllib2.Request(url=url, headers=headers)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response, "html.parser")
        for j in range(0,10):
            name = soup.select('.app-name')[j].getText()
            name=re.sub(r' ', '', name)
            name = re.sub(r'\n', '', name)

            dis = soup.select('.brief')[j].getText()
            dis = re.sub(r' ', '', dis)
            dis = re.sub(r'\"', '', dis)
            dis = re.sub(r'\n', '', dis)

            href=soup.select('.app-name')[j].get('href')
            sql_c='select name from baidu_app where url like \"{}\"'.format(href)
            cur.execute(sql_c)
            res=cur.fetchone()
            if res is None:
                sql = 'insert into baidu_app set name=\"{}\",dis=\"{}\",url=\"{}\"'.format(name.encode('utf8'),
                                                                                            dis.encode('utf8'), href)
                cur.execute(sql)
                conn.commit()
            else:
                pass
            print(name)
    return i
print(get_list(keywords))
