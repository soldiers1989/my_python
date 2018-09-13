# -*- coding:utf8 -*-
from bs4 import BeautifulSoup
import requests
import pymysql

#请求url，返回提问者头像和昵称
def get_ask_user(url):
    req=requests.request(method='get',url=url)
    res=req.content
    soup = BeautifulSoup(res, "html.parser", from_encoding='utf-8')
    img=soup.select('.cpBOX_left_ifmt > .float-L ')[0]['src']
    name=soup.select('.cpBOX_left_ifmt > .ml1rem  ')[0].contents[0]
    #return img
    return img,name
#print( get_ask_user('http://www.emakerzone.com/fast_ask_info/1'))

#请求url，返回回答问题者头像和昵称
def get_answer(url):
    #检测有多少答案页
    req = requests.request(method='get', url=url)
    res = req.content
    page_get = BeautifulSoup(res, "html.parser", from_encoding='utf-8')
    page_num=page_get.select('.pagination > li ')
    #return page_num
    if page_num==[]:
        page_num=1
    else:
        page_num = int(page_num[len(page_num) - 2].select('a')[0].contents[0])
    user=[]
    #return page_num
    for i in range(1,page_num+1):
        url_need=url+'?page='+str(i)
        req = requests.request(method='get', url=url_need)
        res = req.content
        soup = BeautifulSoup(res, "html.parser", from_encoding='utf-8')
        img_num = len(soup.select(
            'body > div.min-w.yun_askBOX.yun_askIFBox.mt8rem.mb2r > div.float-L.yun_askBOX_left > div.mt2rem.bcd-wit.col-333.yun_askUser > ul > li'))
        for i in range(0, img_num):
            try:
                img = soup.select( '.yun_askUserLiT a img')[i]['src']
            except:
                img='没头像'
            else:
                img = soup.select('.yun_askUserLiT a img')[i]['src']
            if soup.select('.col-333.ml10')[i].contents==[]:
                name='无昵称'
            else:name = soup.select('.col-333.ml10')[i].contents[0]
            user.append([img, name])
            #return img
    return user
#print(get_answer('http://www.emakerzone.com/fast_ask_info/301'))

def i_u_sql(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='yunfae',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
    except:
        return 0
    else:
        try:
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except:
            return
        else:
            return 1

def select_sql(sql):
    try:
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='yunfae',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
    except:
        return
    else:
        try:
            cur.execute(sql)
            re=cur.fetchall()
            cur.close()
            conn.close()
        except:
            return
        else:
            return re



