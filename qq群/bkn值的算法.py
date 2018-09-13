import re
def GetBkn(skey):
    hash = 5381
    i=0
    for i in xrange(len(skey)):
        hash+=(hash<<5)+ord(skey[i])
        i+=1
    return hash & 2147483647
s='@rU53oppgt'
print(GetBkn('Znc4bNu5Fc'))

qq_cookies=   'RK=s7oUV+W0bK; pt2gguin=o1125354542; ptcz=f4fe9aaa075ae69a3a9a3535603abb24c1c445ad6f63bbabd3eb8a608cbcf1a6; pgv_pvid=1388597080; p_skey=pdB0YWuuGenke14vXtmEvqmKXWqB*mbVZgSsIPQqCqw_; p_uin=o1125354542; uin=o1125354542; skey=Znc4bNu5Fc'

dis_qq={}

list=qq_cookies.split('; ')
def get_skey_qq_id(cookies):
    for i in range(0, len(list)):
        dis_qq[list[i].split('=')[0]] = list[i].split('=')[1]
    seky=dis_qq['skey']
    qq_id=re.findall('[1-9][0-9]{4,}',dis_qq['uin'])
    return [seky,qq_id]
print(get_skey_qq_id(qq_cookies))