# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib
import urllib2
from constant import every_sql
import sys
import cookielib
reload(sys)
sys.setdefaultencoding('utf8')

def use_cookies(url):
    cookie=cookielib.MozillaCookieJar()#声明CookieJar对象实例来保存cookie
    Useragent=('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    AcceptEncoding=('Accept-Encoding','gzip,deflate,gzip,deflate')
    AcceptLanguage=('Accept - Language', 'zh-cn,zh,en')
    Accept=('Accept', '* / *')
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)  # 从文件中读取内容到cookie变量中
    handler = urllib2.HTTPCookieProcessor(cookie)  # 处理器
    opener = urllib2.build_opener(handler)
    opener.addheaders = [Useragent,AcceptEncoding,AcceptLanguage,Accept]
    text = opener.open(url).read()
    return (text)

def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255',
        'Accept - Language': ' zh - CN, zh;q = 0.9',
        'Referer': 'http://www.qichacha.com/'
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # 获取指定数据
    soup = BeautifulSoup(response, "html.parser")

    info = []
    #获取公司名称
    name = soup.select(".company-name")
    info.append(name[0].get_text())

    phone=soup.select(".phone ")
    info.append(phone[0].get_text())

    email = soup.select(".email ")
    info.append(email[0].get_text())

    base=soup.select(".basic-item-right ")
    for i in xrange(len(base)) :
        x=base[i].get_text()
        info.append(x)
    print(info)

    return info

urllist_sql="""SELECT id,url from content_url where url !='' and have_down=0 limit 30000"""
urllist=every_sql.sql_connect(db_name='web_url_qichacha',sql=urllist_sql)
for i in xrange(0,len(urllist)):
    #取url进行取内容操作
    url=urllist[i]['url']
    info = get_content('http://www.qichacha.com{}'.format(url))
    #info=get_content('http://www.qichacha.com/firm_a91af21f697cdb0052ddfa2831656a72.html')

    for x in xrange(0, len(info)):
        company_name=info[0].replace('\r\n','')
        time=info[7].replace('\r\n','')
        phone=info[1].replace('\r\n','')
        email=info[2].replace('\r\n','')
        name=info[3].replace('\r\n','')
        index_url=url
        location=info[10].replace('\r\n','')
        jyfw=info[9].replace('\r\n','')
        zczb=info[6].replace('\r\n','')
        yyzz=info[5].replace('\r','').replace('\n','')
        company_type=info[8].replace('\r\n','')
        status=info[12]
    info_list_sql="""insert into company_info_all (company_name,time,phone,name,email,index_url,location,jyfw,zczb,yyzz,company_type,status) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(company_name,time,phone,name,email,index_url,location,jyfw,zczb,yyzz,company_type,status)
    every_sql.sql_connect(db_name='web_url_qichacha', sql=info_list_sql)

    #取内容动作完成，更行当前id在content_url中的状态
    status_sql="""update content_url set have_down=1 where id={}""".format(urllist[i]['id'])
    every_sql.sql_connect(db_name='web_url_qichacha', sql=status_sql)
    print i + 1
    time.sleep(1000)


