import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()
dbname = 'test'

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']
    query = {}

    docs = mycol.find(query)
    sortedDocs = docs.sort([('balance', pymongo.ASCENDING)])
    for doc in sortedDocs:
        acct_info = '账号：%s，账户：%s，余额：%.2f' %(doc['acct_no'], doc['acct_name'], doc['balance'])
        print(acct_info)

conn.close()
















