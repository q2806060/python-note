import pymongo

# 创建连接对象
conn = pymongo.MongoClient("127.0.0.1", 27017)
# 创建库对象
db = conn["db2"]
# 创建集合对象
myset = db["t1"]

# 在t1中插入1条文档
myset.insert_one({"name":"Lucy"})
