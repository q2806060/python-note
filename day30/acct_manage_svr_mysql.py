from socket import *
import pymysql

db_host = '127.0.0.1'
db_user = 'root'
db_password = '123456'
db_name = 'test'
address = ('0.0.0.0', 9999)

db_conn = None

def conn_database():   #connect database
    global db_conn
    db_conn = pymysql.connect(db_host, db_user, db_password, db_name)
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
    global db_conn
    cur = db_conn.cursor()
    if msgs[1] == 'all':
        sql = 'select * from acct'
    else:
        sql = 'select * from acct where acct_no="%s"' % msgs[1]
    print(sql)
    resp = ''
    try:
        cur.execute(sql)
        result = cur.fetchall()
        for row in result:
            acct_no = row[0]
            acct_name = row[1]
            balance = row[4]
            acct_info = 'Account:%s, User:%s, Balance:%.2f\n' %(acct_no, acct_name, balance)
            resp += acct_info
    except:
        print('Failed query!')
    return resp

def new_acct(msgs):
    result = 0
    global db_conn
    cur = db_conn.cursor()
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = msgs[4]
    
    sql = "insert into acct values('%s','%s',now(),%s,%s)" %(acct_no, acct_name, acct_type, balance)
    print(sql)
    try:
        result = cur.execute(sql)
        db_conn.commit()
    except:
        db_conn.rollback()
    ret ='操作结果影响%d行' % result
    return ret

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
        elif msgs[0] == 'update':
            pass
        elif  msgs[0] == 'delete':
            pass
        else:
            print('Request illegal!')
        sockfd.send(result.encode())    #send query data to client
    close_database()
    server.close()

main()
























































