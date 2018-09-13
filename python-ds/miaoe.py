# -*- coding: utf-8 -*-

#抓取苗易网数据
#对方是微信端的


from bs4 import BeautifulSoup
import urllib
import urllib2
import pymysql.cursors
# 获取tel的函数
def get_tel(postData):
    url = 'http://wx.miaoe.com/wxinquiry/miaomuqiugou.html'
    data = urllib.urlencode(postData)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255',
        'Accept - Language':' zh - CN, zh;q = 0.9',
        'Referer':'http: // wx.miaoe.com / wxinquiry / miaomuqiugou.html'
        }

    request = urllib2.Request(url, data, headers=headers)
    response = urllib2.urlopen(request)
    # 获取指定数据
    soup = BeautifulSoup(response, "html.parser")
    hdLinkMobile = []
    hdLinkman=[]
    companyName=[]
    hdArea=[]
    for i in range(0, 10):
        tel=soup.select("input.hdLinkMobile")[i].attrs['value']
        name=soup.select("input.hdLinkman")[i].attrs['value']
        companyname=soup.select("input.companyName")[i].attrs['value']
        address=soup.select("input.hdArea")[i].attrs['value']
        hdLinkMobile.append(tel)
        hdLinkman.append(name)
        companyName.append(companyname)
        hdArea.append(address)
    res = [hdLinkMobile,hdLinkman,companyName,hdArea]
    return res
# 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
for x in range(5415,6200):
    postData = {'fullName': '全国',
                'type': 'list',
                'currentPage': x,
                'pageAction': 'next'
                }
    print '正在请求第{}页……'.format(x)
    s=get_tel(postData)
    for i in range(0,10):
        tel=s[0][i].encode('utf-8')
        name=s[1][i].encode('utf-8')
        companyname=s[2][i].encode('utf-8')
        address=s[3][i].encode('utf-8')
        page=(x-1)*10+i+1
        sql = """insert into miaoe values (\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")""".format(page,tel,name,companyname,address)
        cur.execute(sql)
        conn.commit()
    print '第{}条'.format(page)
print '全部完成'


