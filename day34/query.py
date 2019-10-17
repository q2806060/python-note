import pymongo

conn = pymongo.MongoClient('localhost', 27017)
# conn = pymongo.MongoClient('mongodb://localhost:27017')

dblist = conn.database_names()
print(dblist)
dbname = 'test'

if dbname in dblist:
    mydb = conn['test']         # 获取数据库
    mycol = mydb['acct']        # 获取集合对象
    #query = {}                  # 不带筛选条件查询
    #query = {'acct_name':'Tom'}
    query = {'balance':{'$gt':5000}}
    project = {'_id':0}

    docs = mycol.find(query, project)

    for doc in docs:
        acct_info = '账号：%s，户名：%s，余额：%.2f' %(doc['acct_no'], doc['acct_name'], doc['balance'])
        print(acct_info) 
    
conn.close()

























