from socket import *
import pymongo

address = ('0.0.0.0', 9999)
db_conn = None

db_host = '127.0.0.1'
db_port = 27017
db_name = 'test'

def conn_database():   #connect database
    global db_conn, db_host, db_port
    db_conn = pymongo.MongoClient(db_host, db_port)
    if not db_conn:
        print('failed connect database!')
        return -1
    else:
        return 1

def close_database():
    if not db_conn:
        return
    else:
        db_conn.close()

def query(msgs):
    qry = None
    if msgs[1] == 'all':
        qry = {}
    else:
        qry = {'acct_no':msgs[1]}
    print(qry)
    resp = ''
    try:
        #db_list = db_conn.database_names()
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        docs = mycol.find(qry)
        for doc in docs:
            acct_info = '账户：%s，用户：%s，余额：%f\n' %(doc['acct_no'], doc['acct_name'], doc['balance'])
            resp += acct_info
    except Exception as e:
        print(e)

    return resp

def new_acct(msgs):
    result = ''
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]
    new_dict = {'acct_no':acct_no, 'acct_name':acct_name, 'acct_type':acct_type, 'balance':float(balance)}
    try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        ret = mycol.insert_one(new_dict)
        result += 'Insert ok, ID:%s' %ret.inserted_id
    except:
        result += 'Insert fail! Please re-select!'
    return result

def update_no(msgs):
    try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        docs = mycol.find()
        for doc in docs:
            if doc['acct_no'] == msgs[1]:
                return '1'
        return '0'
    except Exception as e:
        print(e)

def update(msgs):
    result = ''
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]
    try:
        mydb = db_conn[db_name]
        mycol = mydb['acct']
        mycol.update_one({'acct_no':acct_no}, {'$set':{'acct_name':acct_name, 'acct_type':acct_type, 'balance': float(balance)}})
        result += 'Update ok, Update 1 data.'
    except:
        result += 'Update fail! Please re-input!'
    return result


def main():
    if conn_database() == -1:
        return
    server = socket()
    server.bind(address)
    server.listen(5)
    print('Server ready!')
    sockfd, addr = server.accept()
    while True:
        data = sockfd.recv(2048)
        if not data:
            print('Client close!')
            break
        print(data.decode())
        msgs = data.decode().split('::')
        if msgs[0] == 'query':
            result = query(msgs)
        elif msgs[0] == 'new':
            result = new_acct(msgs)
        elif msgs[0] == 'update_no':
            result = update_no(msgs)
        elif msgs[0] == 'update':
            result = update(msgs)
        elif  msgs[0] == 'delete':
            pass
        else:
            print('Request illegal!')
        sockfd.send(result.encode())    #send query data to client
    close_database()
    server.close()

main()



















































































































