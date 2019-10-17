import pymongo

conn = pymongo.MongoClient('localhost', 27017)

dblist = conn.database_names()
dbname = 'test'

if dbname in dblist:
    mydb = conn[dbname]
    mycol = mydb['acct']
    mydict = {
        'acct_no':'622345000006',
        'acct_name':'Linke',
        'balance':8888.888,
    }

    ret = mycol.insert_one(mydict)
    print('NewID:', ret.inserted_id)

conn.close()


















