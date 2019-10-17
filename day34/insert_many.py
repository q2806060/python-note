import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()
dbname = 'test'

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']
    mylist = [{
        'acct_no':'622345000007',
        'acct_name':'halalu',
        'balance':1000000
    },{
        'acct_no':'622345000008',
        'acct_name':'Jerry',
        'balance':6666.66
    },{
        'acct_no':'622345000009',
        'acct_name':'sarde',
        'balance':2333333333.33
    }]

    ret = mycol.insert_many(mylist)
    for i in ret.inserted_ids:
        print(i)

conn.close()



















