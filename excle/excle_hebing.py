# coding=utf-8
import xlrd
import pymysql
from openpyxl import Workbook
def get_id(name,num):
    workbook = xlrd.open_workbook('F:\excle\dianyuan\{}.xls'.format(name))
    for sheet2 in workbook.sheets():
        rows_need = []
        cols = sheet2.col_values(num)  # 获取第一列内容
        for i in range(0, len(cols)):
            rows_need.append((sheet2.row_values(i)[num]))  # 获取第i 行内容
        return rows_need

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='company_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
re=get_id('e',8)
number=len(re)+1
for i in range(2,number):
    sql='insert into tel_limit set tel={},send_message=0,is_right=0'.format(re[i])
    cur.execute(sql)
    conn.commit()
    print(i)
#print(len(get_id('20180428131693546417276867_7544922',8)))