# -*- coding:utf8 -*-
import function
import requests
url_base='http://www.emakerzone.com/fast_ask_info/'
for i in range(669,1235):
    url=url_base+str(i)
    req = requests.request(method='get', url=url)
    res = req.status_code
    if res==500:
        pass
    else:
        re_ask = function.get_ask_user(url)
        sql = 'insert into user set user_img=\'{}\',user_name=\'{}\',type=\'{}\',question_id={}'.format(re_ask[0], re_ask[1], 'asker',
                                                                                         i)
        function.i_u_sql(sql)
        re_answer = function.get_answer(url)
        if re_answer == None:
            pass
        else:
            for j in re_answer:
                sql = 'insert into user set user_img=\'{}\',user_name=\'{}\',type=\'{}\',question_id={}'.format(j[0], j[1], 'answer',
                                                                                                 i)
                print(i)
                function.i_u_sql(sql)