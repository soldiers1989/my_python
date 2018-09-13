# -*- coding:utf-8 -*-
import urllib2
import cookielib


#直接获取cookies
def catch_cookies():
    cookie = cookielib.CookieJar()  # 声明CookieJar对象实例来保存cookie
    handler = urllib2.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    opener = urllib2.build_opener(handler)  # 通过handler构建opener
    opener.open(r'http://www.doorock.com')
    for item in cookie:
        print item
catch_cookies()

#将获取到的cookies放到文件中
def creat_cookies():
    filename = 'cookie.txt'  # 保存cookie的文件
    cookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例（cookie）来保存cookie，后面写入文件
    handler = urllib2.HTTPCookieProcessor(cookie)  # 还是创建处理器
    opener = urllib2.build_opener(handler)  # 创建支持处理HTTP请求的opener对象
    headers = ('User-Agent',
               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheaders = [headers]
    opener.open(r'http://www.qichacha.com/')
    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到文件
    # ignore_discard表示即使cookie将被丢弃也将保存下来，ignore_expires表示如果该文件中cookie已经存在，则覆盖原文件写入


#用获取到的cookies访问网站
def use_cookies():
    cookie=cookielib.MozillaCookieJar()#声明CookieJar对象实例来保存cookie
    Useragent=('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    AcceptEncoding=('Accept-Encoding','gzip,deflate,gzip,deflate')
    AcceptLanguage=('Accept - Language', 'zh-cn,zh,en')
    Accept=('Accept', '* / *')
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)  # 从文件中读取内容到cookie变量中
    handler = urllib2.HTTPCookieProcessor(cookie)  # 处理器
    opener = urllib2.build_opener(handler)
    opener.addheaders = [Useragent,AcceptEncoding,AcceptLanguage,Accept]

    text = opener.open('http://www.qichacha.com/search?key=%E7%94%B5%E5%AD%90%E4%BA%A7%E5%93%81#index:12&').read()
    return (text)
creat_cookies()
#catch_cookies()
#use_cookies()