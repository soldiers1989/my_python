# -*- coding:utf-8 -*-
import urllib
import urllib2
import Queue
from bs4 import BeautifulSoup
import threading
import time



#模拟请求函数
def soup_text_3(headers,url,data):
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return  soup.text

url='http://www.dianyuan.com/index.php?do=community_mail_submit'

#max=760597#当前最大的id
max=760592
have_down=165321
#have_down=760592#已经抓取过的id


q = Queue.Queue()

for i in range(have_down+1,max):
    if i%3==0:
        headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
        'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
        'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; acw_tc=AQAAAB5NZ0li9QIAqw7dciPYPUbXr+4e; PHPSESSID=8a2n8t4jvbf3a783dqmripbkm0; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; CNZZDATA1259646395=1453125441-1530676541-null%7C1531109217; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1531104135; CNZZDATA1271612743=52279750-1531116032-null%7C1531116032; CNZZDATA1253348617=894857706-1531124559-%7C1531124559; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531185323; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1531185791; afpCT=1; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1531183780; CNZZDATA1253348660=774631188-1530681865-null%7C1531181248; CNZZDATA5823629=cnzz_eid%3D2060905375-1531127761-%26ntime%3D1531184047; Netbroad_Dianyuanauto_save_754424=5cfcVAIJA1FSB1QFUl1UUgUABFEKBAFVWgRRDgvcmqyFur2Bp7Pc3eM; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531183961; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1531182147; gdxidpyhxdE=W7g6iPp%2FUY%2F112IQ6ehwPridALibs3D88TMl1BaQa%2FVonfPLNWcK21uRkYAnLBkVaQ147hSDSjYU0sZnSuAtt%2B6YWSqoOqWbPy%2BR%2FyOBUjbjNNVps3KIbqVaBIzjnBi0c3i2XgAMgnuLw%2FtXJYOSKJG5qZrbnSpABivnLh6sGwUMNesK%3A1531187634592; 222.94.73.236_1531184400=1; aa967c72b1dffdef64b9a4d61707f234=e89195aee72e3df605f66a129f0fef37; Netbroad_Dianyuanpush_key=0dbaBVMAVAIEBgkIB1MFVgAEDARWVlYPB1UCBwMGAgwCUAU; __site_info__=865ea11d8c08408bed89b1a3bb822561; __time_a_=8709512942; _user_account_=66ef4d49092fd24bd4bbab9f6e9d4e33; _uid___=597315; username=FAE%E7%94%B5%E6%BA%90'}
    else:
        if i%3==1:
            headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
            'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; CNZZDATA1259646395=1453125441-1530676541-null%7C1531109217; CNZZDATA1271612743=52279750-1531116032-null%7C1531116032; aa967c72b1dffdef64b9a4d61707f234=e89195aee72e3df605f66a129f0fef37; CNZZDATA1253348617=894857706-1531124559-%7C1531209707; CNZZDATA5823629=cnzz_eid%3D2060905375-1531127761-%26ntime%3D1531211399; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1531209425; CNZZDATA1253348635=1438443782-1531212781-null%7C1531212781; CNZZDATA1253348660=774631188-1530681865-null%7C1531213487; CNZZDATA5823622=cnzz_eid%3D1580682441-1531214402-null%26ntime%3D1531214402; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1531447092; acw_tc=AQAAAABvmSu6WgMA8Q3dcuBUSSvbhq6D; PHPSESSID=kogbcj8kmtnt8cng5jg1uot5i7; afpCT=1; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531787838; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531786038; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1531787946; Netbroad_Dianyuanpush_key=f131BFQFVFRTUwkHA1ICBwZTXVRaBQsJWlAHB1QHVw0ABQE; CNZZDATA1253348604=1728622284-1531786415-null%7C1531786415; gdxidpyhxdE=cRl352jliO4DlmJhRcHE7M2GW9Ett5GWyRyrz2%2FLxpQQs62spnD1H8jYdZZQj%2BCd9wehlPfe9LNyzWlyIrp%2BsDCkUXsN54nGI4ZQ6OR%2Fk9MOpCQpT15zczExpNpKQZZYCYg9Ivvg%2BXozhVhxhm2dHAZjjH8eeMoSphSvaeMgRb3PAJi6%3A1531791864462; __site_info__=5445afa4227ed014d370b1c21cc3a8f2; __time_a_=8709512947; _user_account_=489f4d11d1ea0994bbf98b35a34b7965; _uid___=352124; username=%E7%94%B5%E6%BA%90FAE; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1531788452'}
        else:
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
                'Referer': 'http://www.dianyuan.com/index.php?do=community_mail_create&touid=759833',
                'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; CNZZDATA1259646395=1453125441-1530676541-null%7C1531109217; CNZZDATA1271612743=52279750-1531116032-null%7C1531116032; aa967c72b1dffdef64b9a4d61707f234=e89195aee72e3df605f66a129f0fef37; CNZZDATA1253348617=894857706-1531124559-%7C1531209707; CNZZDATA5823629=cnzz_eid%3D2060905375-1531127761-%26ntime%3D1531211399; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1531209425; CNZZDATA1253348635=1438443782-1531212781-null%7C1531212781; CNZZDATA1253348660=774631188-1530681865-null%7C1531213487; CNZZDATA5823622=cnzz_eid%3D1580682441-1531214402-null%26ntime%3D1531214402; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1531447092; acw_tc=AQAAAABvmSu6WgMA8Q3dcuBUSSvbhq6D; PHPSESSID=kogbcj8kmtnt8cng5jg1uot5i7; afpCT=1; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531787838; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1531787946; Netbroad_Dianyuanpush_key=f131BFQFVFRTUwkHA1ICBwZTXVRaBQsJWlAHB1QHVw0ABQE; CNZZDATA1253348604=1728622284-1531786415-null%7C1531786415; gdxidpyhxdE=cRl352jliO4DlmJhRcHE7M2GW9Ett5GWyRyrz2%2FLxpQQs62spnD1H8jYdZZQj%2BCd9wehlPfe9LNyzWlyIrp%2BsDCkUXsN54nGI4ZQ6OR%2Fk9MOpCQpT15zczExpNpKQZZYCYg9Ivvg%2BXozhVhxhm2dHAZjjH8eeMoSphSvaeMgRb3PAJi6%3A1531791864462; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1531788452; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1531791527; __site_info__=865ea11d8c08408bed89b1a3bb822561; __time_a_=8709512942; _user_account_=5f5e88f4d3fa5f2b2452dcf17101ae6f; _uid___=662310; username=FAE%E7%94%B5%E6%BA%90'}

    q.put(i)

while not q.empty():
    ti1=time.time()
    x1 = q.get()
    data1 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
           还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x1
    }
    t1=threading.Thread(target=soup_text_3, args=(headers,url,data1))
    t1.start()


    x2 = q.get()
    data2 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x2
    }

    t2=threading.Thread(target=soup_text_3, args=(headers,url,data2))
    t2.start()

    x3 = q.get()
    data3 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x3
    }
    t3 = threading.Thread(target=soup_text_3, args=(headers, url, data3))
    t3.start()

    x4 = q.get()
    data4 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x4
    }
    t4 = threading.Thread(target=soup_text_3, args=(headers, url, data4))
    t4.start()

    x5 = q.get()
    data5 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x5
    }
    t5 = threading.Thread(target=soup_text_3, args=(headers, url, data5))
    t5.start()

    x6 = q.get()
    data6 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x6
    }
    t6 = threading.Thread(target=soup_text_3, args=(headers, url, data6))
    t6.start()

    x7 = q.get()
    data7 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x7
    }
    t7 = threading.Thread(target=soup_text_3, args=(headers, url, data7))
    t7.start()

    x8 = q.get()
    data8 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x8
    }
    t8 = threading.Thread(target=soup_text_3, args=(headers, url, data8))
    t8.start()

    x9 = q.get()
    data9 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x9
    }
    t9 = threading.Thread(target=soup_text_3, args=(headers, url, data9))
    t9.start()

    x10 = q.get()
    data10 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                     还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x10
    }
    t10 = threading.Thread(target=soup_text_3, args=(headers, url, data10))
    t10.start()

    x11 = q.get()
    data11 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x11
    }
    t11 = threading.Thread(target=soup_text_3, args=(headers, url, data11))
    t11.start()

    x12 = q.get()
    data12 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x12
    }
    t12 = threading.Thread(target=soup_text_3, args=(headers, url, data12))
    t12.start()

    x13 = q.get()
    data13 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x13
    }
    t13 = threading.Thread(target=soup_text_3, args=(headers, url, data13))
    t13.start()

    x14 = q.get()
    data14 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x14
    }
    t14 = threading.Thread(target=soup_text_3, args=(headers, url, data14))
    t14.start()

    x15 = q.get()
    data15 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x15
    }
    t15 = threading.Thread(target=soup_text_3, args=(headers, url, data15))
    t15.start()

    x16 = q.get()
    data16 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x16
    }
    t16 = threading.Thread(target=soup_text_3, args=(headers, url, data16))
    t16.start()

    x17 = q.get()
    data17 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x17
    }
    t17 = threading.Thread(target=soup_text_3, args=(headers, url, data17))
    t17.start()

    x18 = q.get()
    data18 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x18
    }
    t18 = threading.Thread(target=soup_text_3, args=(headers, url, data18))
    t18.start()

    x19 = q.get()
    data19 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x19
    }
    t19 = threading.Thread(target=soup_text_3, args=(headers, url, data19))
    t19.start()

    x20 = q.get()
    data20 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                         还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x20
    }
    t20 = threading.Thread(target=soup_text_3, args=(headers, url, data20))
    t20.start()

    x21 = q.get()
    x22 = q.get()
    x23 = q.get()
    x24 = q.get()
    x25 = q.get()
    x26 = q.get()
    x27 = q.get()
    x28 = q.get()
    x29 = q.get()
    x30 = q.get()

    data21 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x21
    }
    data22 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x22
    }
    data23 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x23
    }
    data24 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x24
    }
    data25 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x25
    }
    data26 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x26
    }
    data27 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x27
    }
    data28 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x28
    }
    data29 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x29
    }
    data30 = {
        'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                                 还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
        'touid': x30
    }

    t21 = threading.Thread(target=soup_text_3, args=(headers, url, data21))
    t22 = threading.Thread(target=soup_text_3, args=(headers, url, data22))
    t23 = threading.Thread(target=soup_text_3, args=(headers, url, data23))
    t24 = threading.Thread(target=soup_text_3, args=(headers, url, data24))
    t25 = threading.Thread(target=soup_text_3, args=(headers, url, data25))
    t26 = threading.Thread(target=soup_text_3, args=(headers, url, data26))
    t27 = threading.Thread(target=soup_text_3, args=(headers, url, data27))
    t28 = threading.Thread(target=soup_text_3, args=(headers, url, data28))
    t29 = threading.Thread(target=soup_text_3, args=(headers, url, data29))
    t30 = threading.Thread(target=soup_text_3, args=(headers, url, data30))
    t21.start()
    t22.start()
    t23.start()
    t24.start()
    t25.start()
    t26.start()
    t27.start()
    t28.start()
    t29.start()
    t30.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    t17.join()
    t18.join()
    t19.join()
    t20.join()
    t21.join()
    t22.join()
    t23.join()
    t24.join()
    t25.join()
    t26.join()
    t27.join()
    t28.join()
    t29.join()
    t30.join()
    ti2=time.time()
    t=ti2-ti1
    print(t,x30)
