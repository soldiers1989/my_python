# -*- coding:utf-8 -*-
import urllib
import urllib2
import pymysql
import re
from bs4 import BeautifulSoup


def max_id(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    res=soup.select('#chart > p > em > a')
    new_url= res[0]['href']

    request2 = urllib2.Request(url=new_url)
    response2 = urllib2.urlopen(request2)
    soup2 = BeautifulSoup(response2, "html.parser")
    re2 = soup2.select('#wp > div > div.user-top.clearfix > div.lf.user-msg > div.bower-detail > a')[0]
    s=re2['href'].encode('utf8')
    return re.findall('[1-9][0-9]{2,}',s)[0]

def post_message(data,url,headers):
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return soup.text

url="http://bbs.elecfans.com/"
max_id=int(max_id(url))
def insert_id(max_id):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    sql_old = 'select id from elecfans where id={}'.format(max_id)
    cur.execute(sql_old)
    res=cur.fetchall()
    conn.commit()
    x=[]
    for i in res:
        x.append(i['id'])
    return  x
print(max_id)

if insert_id(max_id)=='':
    pass
else :
    if max_id in insert_id(max_id):
        pass
    else:
        url = "http://bbs.elecfans.com/home.php?mod=spacecp&ac=pm&op=send&pmid=77878&daterange=0&handlekey=pmsend&pmsubmit=yes&inajax=1"
        data = {
            'touid': max_id,
            'formhash': '0b36d335',
            'message': '斗石FAE，专业FAE服务贡献平台，提供IC技术支持服务，200+入驻工程师，为超500家企业提供技术支持服务！地址：doorock.com。',
        }
        header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://bbs.elecfans.com/home.php?mod=space&do=pm&subop=view&touid={}'.format(max_id),
            'Cookie': 'visitor=d0e34858611258ceaffcfdc9085ba5ee; _ga=GA1.2.929317288.1529466827; bdshare_firstime=1529466865195; rlhx_e495_saltkey=kU3oZ88u; rlhx_e495_lastvisit=1531186776; rlhx_e495_visitedfid=49; auth_webinar_event=DBHRZSzXl4wiCg9WsUBs1kVpIv6h5j2uDfTw4iht5g9C6MYGO5e4AMy9GiV0ne07GppjI8GQ74G%252Br7WUGmKQRM89PqVbxp9W5ncBUHe3fX69NW7%252Buom81IowZJaqG9fWdGw5N31G2pxeYv1IK3UWS5QKJ7Spi0A9J1RyzA%252FOIIn0F4VYWLvXhHcSB2ZoELqRv3DkZrBhkxco7NNyyn5rlaEYzdsmbYiK%252Bdibi8wVTrI; auth_bbs=4s3GA6B9WngZfIhXZ4k4lXWNzc4u2Tb1XLvbQSo3b1jwBZS%252B1INnk%252Fw9pe%252FJ6ixlORFqZBzjd9uYvlcVRfVVnII1%252FQbmdWlyJsGeTougrJchBFUPnsUYMtlcff4aRgXbXVuISRvTm4Uu60GMxBrUd74Od%252ByCvp1pAyi64rAg%252BvXpZ54p33xSot8WfDOYV1hSIIiT5OdWmBKXVZh5wk%252FAcj%252BclUUwtP9jyeuD3t91GDI; PHPSESSID=8uv8tq62iqoalv46smd6lm4kd2; _gid=GA1.2.2137401381.1531730343; Hm_lvt_4dbddc73fd0fe464304ba8ad95cbc96e=1529466827,1531189896,1531364082,1531730343; rlhx_e495_sid=Eo0B43; rlhx_e495_lip=114.222.231.222%2C1531364134; rlhx_e495_nofavfid=1; rlhx_e495_ulastactivity=13dbDMTOV6Md1Tb5hJSR21HMv5KWOHmw0zWIzUUe6aNv1poqfloP; Hm_lvt_5e568854ed60ccf3b533106b98711ff5=1529466864,1530842096,1531189895,1531730391; popAds=1; rlhx_e495_atarget=1; rlhx_e495_groupviewed=934; rlhx_e495_st_t=2987378%7C1531730457%7C760720d66b4aa10288c53e3102cf4122; rlhx_e495_forum_lastvisit=D_934_1531730395D_49_1531730457; rlhx_e495_smile=1D1; rlhx_e495_home_diymode=1; rlhx_e495_st_p=2987378%7C1531730577%7C6ec0428c5c01d3cfd2212c6c307cfe85; Hm_lpvt_4dbddc73fd0fe464304ba8ad95cbc96e=1531730582; rlhx_e495_viewid=uid_3019319; rlhx_e495_lastcheckfeed=2987378%7C1531731403; Hm_lpvt_5e568854ed60ccf3b533106b98711ff5=1531731407; rlhx_e495_lastact=1531733466%09home.php%09spacecp'}
        print post_message(data, url, header)
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='company_tel',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        sql_new = 'insert into elecfans set id={}'.format(max_id)
        cur.execute(sql_new)
        conn.commit()


