import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()              # 查看所有数据库

if not dblist:
    print('dblist is none!')
else:
    for db in dblist:
        print('dblist:', db)

conn.close()




























