# -*- coding:utf-8 -*-
import urllib
import urllib2
import Queue
from bs4 import BeautifulSoup
import threading
import time



#模拟请求函数
def soup_text_3(headers,url,id):
    if id=='':
        return
    else:
        data = {
            'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                       还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
            'touid': id
        }
        params = urllib.urlencode(data)
        request = urllib2.Request(url=url, data=params, headers=headers)
        response = urllib2.urlopen(request)
        soup = BeautifulSoup(response, "html.parser")
        return soup.text


url='http://www.dianyuan.com/index.php?do=community_mail_submit'

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Cookie': 'UM_distinctid=16462e6be734fa-022f12f9d45b53-5e442e19-1fa400-16462e6be7439d; _version_up_temp=1; _9755xjdesxxd_=32; cookie_uid=8hhte4dazn; rid=5b3c27bc7bc44; CNZZDATA1259640412=540026615-1530671096-null%7C1530671096; CNZZDATA1255149870=391002366-1530672112-null%7C1530672112; CNZZDATA1259646395=1453125441-1530676541-null%7C1530676541; CNZZDATA5119584=cnzz_eid%3D386009574-1530674568-null%26ntime%3D1530674568; CNZZDATA5333296=cnzz_eid%3D1727851591-1530676548-null%26ntime%3D1530676548; CNZZDATA5333310=cnzz_eid%3D922422477-1530673813-null%26ntime%3D1530673813; acw_tc=AQAAAB5NZ0li9QIAqw7dciPYPUbXr+4e; PHPSESSID=8a2n8t4jvbf3a783dqmripbkm0; CNZZDATA5856677=cnzz_eid%3D432098355-1530668545-null%26ntime%3D1530838504; CNZZDATA5781160=cnzz_eid%3D1184672083-1530665347-null%26ntime%3D1530839870; CNZZDATA1253348660=774631188-1530681865-null%7C1530841710; Netbroad_Dianyuanauto_save_754424=6dc0BgYFVlICAAgFCAoHAFJTDAQBAFYAVg1QDVQ; Netbroad_Dianyuanpush_key=e76cBABUVlJWBlZTCFRRVFQDXlRWVARcAVxXVAcBAFFVAVE; CNZZDATA5781162=cnzz_eid%3D1003566824-1530665257-null%26ntime%3D1530845698; afpCT=1; CNZZDATA5858887=cnzz_eid%3D486843040-1530665472-null%26ntime%3D1530846436; CNZZDATA2637227=cnzz_eid%3D1366216128-1530664304-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1530848579; CNZZDATA2664271=cnzz_eid%3D1704735767-1530662395-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1530849667; gdxidpyhxdE=Pziin0ubOo8p%2B4BwJuOsYh6udgQV44MSRJVV%2BxvmNVznU6BhZj9QysTmWhea%5C1f4HLKkUczfMnNhZuSt%5C8nplkVoAJwXVS%2FoeecIjrhgYEe3W213LYQEq1n%2F6CeBEAljo%2FrJVT%2B%2B%2FUfCS6VPML38fjPRUBLydzxOO9C%2FeINluNq7xE6a%3A1530850937250; aa967c72b1dffdef64b9a4d61707f234=36b8c940e961d7beddb44aabbee1d12b; __site_info__=721bd270175ca94ced3a6024e1868805; __time_a_=8709513217; _user_account_=4a4e811a40fc08ef5c9ab9bbc3ae7adb; _uid___=177881; username=zhanfeida'}
max=759803#当前最大的id

have_down=179805#已经抓取过的id

min=167571#管理员的id

f10000=10000
class myThread(threading.Thread):  # 线程处理函数
    global headers
    global url
    global have_down
    global f10000

    def __init__(self, name):
        threading.Thread.__init__(self)  # 线程类必须的初始化
        self.thread_name = name # 将传递过来的name构造到类中的name
    def run(self):
        q = Queue.Queue()
        for i in range(have_down + 1, have_down + f10000):
            q.put(i)
        while not q.empty():
            t = q.get()
            if t == '':
                return t
            else:
                data = {
                    'content': """硬件研发进度慢？原厂支持难？来斗石网，200+专业FAE，24小时快速响应！
                               还可以加入我们，来做兼职FAE，用你的技术创造更高价值！点击<a href=http://www.doorock.com> www.doorock.com</a>了解详情!""",
                    'touid': t
                }
                params = urllib.urlencode(data)
                request = urllib2.Request(url=url, data=params, headers=headers)
                response = urllib2.urlopen(request)
                soup = BeautifulSoup(response, "html.parser")
                print(soup.text)
        else:
            return

myThreads=[]
for t in range(1, 11):
    thread = myThread(str(t))
    myThreads.append(thread)
ti1 = time.time()
for th in myThreads:
    th.start()
for th in myThreads:
    th.join()
print(time.time() - ti1)


