# coding=utf-8
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import time
import hashlib

#获取login
def get_open_api_auth_token(time):
    log_in_url = 'https://huinongtx.udesk.cn/open_api_v1/log_in'
    email='it@huinongtx.com'
    post_email_pass = {
        "email": email,
        "password": "czman890119"
    }

    data = urllib.urlencode(post_email_pass)
    request = urllib2.Request(log_in_url, data)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    res = soup.text
    res_json = json.loads(res)
    sign_need=email+'&'+res_json['open_api_auth_token']+'&'+str(time)
    sign=hashlib.sha1(sign_need).hexdigest()
    return sign
#数据组装
email='it@huinongtx.com'
url='http://huinongtx.udesk.cn/open_api_v1/customers?page=1&page_size=10&email={}&timestamp={}&sign={}'.format(email,int(time.time()),get_open_api_auth_token(int(time.time())))
post_data={
}
data=urllib.urlencode(post_data)
request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response, "html.parser")
res = soup.text

print res