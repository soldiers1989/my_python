# -*- coding:utf-8 -*-
#根据id给用户发私信
#id由火车头采集，然后移到mysql中

import urllib
import urllib2
import pymysql
from bs4 import BeautifulSoup
import time

def post_message(data,url,headers):
    params = urllib.urlencode(data)
    request = urllib2.Request(url=url, data=params, headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response, "html.parser")
    return soup.text

def get_touid():
    sql='select uid from 21ic_uid where have_send is null '
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='company_tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute(sql)
    re = cur.fetchall()
    ret=[]
    for i in re:
        ret.append(i['uid'])
    return ret

touid_list=get_touid()
for i in range(0,len(touid_list)):
    touid=touid_list[i]
    if i%2==0:
        data = {
            'pmsubmit': 'true',
            'touid': touid,
            'formhash': '88836a3d',
            'handlekey': 'showMsgBox',
            'message': '斗石FAE，专业FAE服务贡献平台，提供IC技术支持服务，200+入驻工程师，为超500家企业提供技术支持服务！地址：doorock.com。',
            'messageappend': ''
        }
        header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://bbs.21ic.com/home.php?mod=space&do=friend',
            'Cookie': '__fansid=1529375844728172623; pgv_pvi=1831485633; __utmz=172331232.1529377685.2.2.utmcsr=my.21ic.com|utmccn=(referral)|utmcmd=referral|utmcct=/index.php; Hm_lvt_fc868de3b4ad5914d339b8563f8ef33d=1531206519; Hm_lvt_338f39f5a74fd34752c096cf08b362da=1531206209,1531364980; Hm_lvt_d3ce7b4fa66ea0292094d907b616e231=1531366143; Hm_lvt_9dc6fef27c210ee92d9856cc57734202=1531366159; Hm_lvt_acebf9e95257015655cdaddad6c53c72=1531366195; aSr_saltkey=1; aSr_lastvisit=1531374031; aSr_connect_login=1; aSr_connect_is_bind=1; aSr_connect_uin=E8F17C26CE34015A4D787DEFEC54199B; aSr_connect_synpost_tip=1; aSr_nofavfid=1; aSr_smile=1D1; aSr_forum_lastvisit=D_161_1531378224D_1_1531444528D_6_1531444564; aSr_visitedfid=6D1; aSr_home_readfeed=1531445111; __utma=172331232.833032595.1529375845.1531364309.1531726132.5; __utmc=172331232; Hm_lvt_22332d78648b7586de15b4542cb6f7ae=1529375845,1531206185,1531364309,1531726132; Hm_lpvt_22332d78648b7586de15b4542cb6f7ae=1531726132; __utmc=47566196; aSr_viewid=tid_2530144; aSr_home_diymode=1; aSr__refer=%252Fhome.php%253Fmod%253Dspacecp%2526ac%253Dpm%2526op%253Dshowmsg%2526handlekey%253Dshowmsg_2690256%2526touid%253D2690256%2526pmid%253D0%2526daterange%253D2%2526infloat%253Dyes%2526handlekey%253DshowMsgBox%2526inajax%253D1%2526ajaxtarget%253Dfwin_content_showMsgBox; pgv_info=ssi=s8696361248; aSr_seccode=5360.340d15c15103228183; aSr_con_request_uri=http%3A%2F%2Fmy.21ic.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhttp%253A%252F%252Fbbs.21ic.com%252Ficview-2530144-1-1.html; aSr_sid=gZVNU3; aSr_client_created=1531728620; aSr_client_token=E8F17C26CE34015A4D787DEFEC54199B; aSr_ulastactivity=307dinsYpTmWWXYihcpUIWlwL2mqVgxwyiJSZD%2FZ%2Fn8eE6apEpNT; aSr_auth=3728Iwzi1QuE0kTH%2B5Rg9qHHEcbEin3HlGUDT3IAlMlbWKeAtvpJERKvf2jC8M7Wb7Gndm4a8b7ZrWcWj%2FhNeR8YwTVMLcXA%2B%2FTvlC0; aSr_sendmail=1; aSr_noticeTitle=1; aSr_st_p=2706602%7C1531728624%7C98da02f93c9c9c27345492b00175eaeb; Hm_lvt_765e0563c632442fdfc136d7af327702=1531378208,1531378217,1531726169,1531728628; __utma=47566196.1550463374.1531206205.1531726169.1531728628.6; __utmz=47566196.1531728628.6.4.utmcsr=my.21ic.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect.php; __utmt=1; aSr_lastact=1531728705%09home.php%09spacecp; aSr_checkpm=1; aSr_lastcheckfeed=2706602%7C1531728705; aSr_checkfollow=1; Hm_lpvt_765e0563c632442fdfc136d7af327702=1531728708; __fanvt=1531728707763; __utmb=47566196.4.10.1531728628'}
        url = """http://bbs.21ic.com/home.php?mod=spacecp&ac=pm&op=send&touid={}&inajax=1""".format(touid)
    else:
        data = {
            'pmsubmit': 'true',
            'touid': touid,
            'formhash': 'dc6e963a',
            'handlekey': 'showMsgBox',
            'message': '斗石FAE，专业FAE服务贡献平台，提供IC技术支持服务，200+入驻工程师，为超500家企业提供技术支持服务！地址：doorock.com。',
            'messageappend': ''
        }
        header = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',
            'Referer': 'http://bbs.21ic.com/home.php?mod=space&do=friend',
            'Cookie': '__fansid=1529375844728172623; pgv_pvi=1831485633; __utmz=172331232.1529377685.2.2.utmcsr=my.21ic.com|utmccn=(referral)|utmcmd=referral|utmcct=/index.php; aSr_saltkey=1; aSr_lastvisit=1529377464; aSr_connect_is_bind=0; aSr_nofavfid=1; aSr_smile=1D1; Hm_lvt_fc868de3b4ad5914d339b8563f8ef33d=1531206519; __utma=172331232.833032595.1529375845.1531206185.1531364309.4; __utmc=172331232; Hm_lvt_22332d78648b7586de15b4542cb6f7ae=1529375845,1531206185,1531364309; Hm_lpvt_22332d78648b7586de15b4542cb6f7ae=1531364309; __utmc=47566196; __utmz=47566196.1531364314.2.2.utmcsr=21ic.com|utmccn=(referral)|utmcmd=referral|utmcct=/; pgv_info=ssi=s8290314468; Hm_lvt_338f39f5a74fd34752c096cf08b362da=1531206209,1531364980; aSr__refer=%252Fhome.php%253Fmod%253Dspacecp%2526ac%253Dplugin%2526id%253Dmajia%253Abind%2526do%253Dregister; aSr_leftnav=1-0-0-0-0-0-1-0-1-1-1-1-1-1-0-1-1; aSr_nofocus_forum=1; aSr_home_diymode=1; aSr_seccode=2284.4f01db0b04bd04c15a; aSr_ulastactivity=23cbJPvA8zO6djYa3Vf5nPqW%2FPRp0O4C4EK1jmSv7hhM294Jhbr9; aSr_auth=e7b3V0bw4FFLM5lUVWYRBu01cy5YEmyIwIXNcE4yCGfddcgpF9Ax%2B%2BDlRaTcoT5Bt4cJaNyN17%2BPu3%2BtNn%2F7umBEMX8fFBwtOC0ktGk; www_username=ahaufox; bbs_username=ahaufox; ic21_bbsuser=ahaufox%092676546; Hm_lvt_765e0563c632442fdfc136d7af327702=1531206205,1531364314,1531365937; aSr_forum_lastvisit=D_348_1531206460D_12_1531206611D_11_1531365347D_2_1531365368D_1_1531365907D_6_1531365967; Hm_lpvt_338f39f5a74fd34752c096cf08b362da=1531366120; Hm_lvt_d3ce7b4fa66ea0292094d907b616e231=1531366143; Hm_lpvt_d3ce7b4fa66ea0292094d907b616e231=1531366143; Hm_lvt_9dc6fef27c210ee92d9856cc57734202=1531366159; Hm_lpvt_9dc6fef27c210ee92d9856cc57734202=1531366175; Hm_lvt_acebf9e95257015655cdaddad6c53c72=1531366195; Hm_lpvt_acebf9e95257015655cdaddad6c53c72=1531366195; aSr_visitedfid=6D114D124D127D49D2D1D246D11D12; aSr_st_t=2676546%7C1531366266%7Cb1c06335a34dfc8a8337e3c314965953; aSr_st_p=2676546%7C1531367078%7Cff63f883f0de20d5f470d18a2f86ca3e; aSr_viewid=tid_2529358; aSr_sid=s7u9Fa; aSr_lip=114.222.231.222%2C1531365457; __utma=47566196.1550463374.1531206205.1531364314.1531375713.3; aSr_home_readfeed=1531375957; aSr_lastcheckfeed=2676546%7C1531376763; aSr_checkfollow=1; aSr_sendmail=1; Hm_lpvt_765e0563c632442fdfc136d7af327702=1531376766; aSr_lastact=1531376763%09home.php%09spacecp; aSr_checkpm=1; __fanvt=1531376765962; __utmt=1; __utmb=47566196.54.10.1531375713'}
    url = """http://bbs.21ic.com/home.php?mod=spacecp&ac=pm&op=send&touid={}&inajax=1""".format(touid)
    s= post_message(data,url,header)
    if s.find('pmid') >= 0:
        sql = 'update 21ic_uid set have_send=1 where uid={}'.format(touid)
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='root',
                               db='company_tel',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print s
        time.sleep(10)
    else:
        time.sleep(10)
        print s



