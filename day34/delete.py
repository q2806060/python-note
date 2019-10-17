import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()
dbname = 'test'

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']
    query = {'acct_no':'622345000007'}
    ret = mycol.delete_one(query)
    print('删除笔数：%d' %ret.deleted_count)


conn.close()










































