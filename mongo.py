from pymongo import MongoClient
import pandas as pd
client = MongoClient('mongodb://127.0.0.1:27017/')#连接mongo
db = client['Sina']
fangyuan = db['GetShowItems']
aa = fangyuan.find()
data = pd.DataFrame(list(aa))
print(data)
# data = pd.DataFrame(data,dtype='str')
# db = conn.mydb  #连接mydb数据库，没有则自动创建
# my_set = db.test_set　　#使用test_set集合，没有则自动创建