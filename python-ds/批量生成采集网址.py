# -*- coding: utf-8 -*-
from constant import every_sql
sql='select * from web_url where page=501'
re=every_sql.sql_connect(db_name='web_url_qichacha',sql=sql)
for i in range(0,len(re)):
    for j in range(0,re[i]['page']):
        url = re[i]['url'] + str(j+1)
        sql2 = """insert into web_url_last (url) values (\"{}\")""".format(url)
        every_sql.sql_connect(db_name='web_url_qichacha', sql=sql2)
    print(i)
