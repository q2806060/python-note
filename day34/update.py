import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()
dbname = 'test'

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']
    query = {'acct_no':'622345000007'}
    new_value = {'$set':{'balance':66666666666}}
    ret = mycol.update_one(query, new_value, False, False)
    print(ret)
    print('共修改%d笔' %ret.modified_count)


conn.close()















