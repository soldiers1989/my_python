# -*- coding:utf-8 -*-
import urllib
import urllib2
import time
from bs4 import BeautifulSoup



#模拟请求函数
def soup_text_3(headers,url,post):
    params = urllib.urlencode(post)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text

url='http://www.dianyuan.com/index.php?do=community_mail_submit'


headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
    'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
    'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA1259646395=1453125441-1530676541-null%7C1530676541; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1530674568; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; acw_tc=AQAAAB5NZ0li9QIAqw7dciPYPUbXr+4e; PHPSESSID=8a2n8t4jvbf3a783dqmripbkm0; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1530838504; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; aa967c72b1dffdef64b9a4d61707f234=36b8c940e961d7beddb44aabbee1d12b; afpCT=1; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531098418; gdxidpyhxdE=c25rjwhnJXMI%5C1T9j5jxLDu2CchkkL1e%2F%5CUYI6R%5C7egSBwuLaoQsN31RHgrQNC4Ijdlm4j0xoPcoJgeluZIwMPq1%2Bap9nJTNvdVTkW9D%2BlKZiH4q5lhe1jWvS4iTAx7QOrRGyDL0aBEmUtsdOndOm8%5CVR0ErYREPVuYpjNULlwokTyJU%3A1531099323649; __site_info__=62e376bcb68dc19e1b73f6f443f62567; __time_a_=8709518605; _user_account_=aba2a43510090adeedbb04a80bacc04d; _uid___=577288; username=ahaufox; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531098436; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1531096800; Netbroad_Dianyuanpush_key=0892CQkBAFRVBlMFVAEDVQVUAAJQAABfVFEFA1VRDAxWVgc; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1531096632; CNZZDATA1253348660=774631188-1530681865-null%7C1531097410'}


'''
datas = {
    'content': """ 硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
      还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com>doorock.com</a>了解详情!""",
    'touid': '754424'
}
print(soup_text_3(headers,url,datas))
'''
max=759832#当前最大的id
759809-754424
755848

have_down=759796#已经抓取过的id

min=167571#管理员的id

f10000=1000

for i in range(have_down+1,max):
    t1=time.time()
    datas = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
      还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': i
    }
    t=0
    print(soup_text_3(headers,url,datas),i)
    t = time.time() - t1
    print(t)

