# coding=utf-8

#mongodb链接测试

import pymongo
client=pymongo.MongoClient('127.0.0.1',27017)
db = client.mydb
my_set = db.test_set
my_set.insert({"name":"zhangsan","age":18})
for i in my_set.find():
    print(i)