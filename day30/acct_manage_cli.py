'''格式
查询：
    请求：
        query::all              #查询所有账户
        query::1111111111111    #查询自定账户
    响应：
        账号：1111111111111， 用户名：Jerry， 余额：10000

新增：
    请求：
        new:2222222222222::Tom::1::10.00
    响应：
        执行一笔操作
'''

from socket import *
import pymysql

client = None
host = '127.0.0.1'
port = 9999

def print_menu():
    menu = '''
    ---------------账户管理系统-----------------
        1.查询账户
        2.新建账户
        3.修改账户
        4.删除账户
        5.退出
    '''
    print(menu)

def open_conn():   #server connect
    try:
        global client
        client = socket()
        client.connect((host, port))
        print('Successful connect!')
        return 0
    except:
        print('Failed connect!')
        return -1

def send_msg(msg):  #send data
    if not client:
        return -1
    n = client.send(msg.encode())
    return n

def recv_msg():    #recv data
    if not client:
        return None
    data = client.recv(2048)
    return data


def query_acct():   #query account
    acct_no = input('Please input acct_no:')
    if acct_no and acct_no != '':
        msg = 'query::' + acct_no
    else:
        msg = 'query::all'

    if send_msg(msg) < 0:
        print('Fail send!')
        return

    data = recv_msg()
    if not data:
        print('Failed query!')
    else:
        print(data.decode())

def new_acct():
    try:
        acct_no = input('Please input new acct_no:')
        acct_name = input('Please input acct_name:')
        acct_type = input('Please input acct_type:')
        balance = float(input('Please input balance:'))
        assert balance >= 10.00000000000
        assert (acct_type  == '1' or acct_type == '2')
    except ValueError:
        print('Data in wrong format!')
    except AssertionError:
        print('Data outside range!')
    except:
        print('Input wrong!')
    else:
        msg = 'new::%s::%s::%s::%f' %(acct_no, acct_name, acct_type, balance)
        print(msg)
        if send_msg(msg) < 0:
            print('Failed send!')
            return
        data = recv_msg()
        if not data:
            print('Recv data fail!')
        else:
            print(data.decode())
            
def update_acct():
    try:
        acct_no = input('Please input update acct_no or input "q" to quit:')
        if acct_no == 'q':
            return
        s = 'update_no::%s'%acct_no
        send_msg(s)
        data = recv_msg()
        if int(data):
            new_acct_name = input('Please input new acct_name:')
            new_acct_type = input('Please input new acct_type:')
            new_balance = float(input('Please input new balance:'))
            msg = 'update::%s::%s::%s::%f' %(acct_no, new_acct_name, new_acct_type, new_balance)
            if send_msg(msg) < 0:
                print('Failed send!')
                return
            data = recv_msg()
            if not data:
                print('Recv data fail!')
            else:
                print(data.decode())          
        else:
            print('Please re-input acct_no')
            update_acct
    except Exception as e:
        print(e)


def main():
    open_conn()
    while True:
        print_menu()
        oper = input('Please select server:')
        if not oper:
            continue
        elif oper == '1':
            query_acct()
        elif oper == '2':
            new_acct()
        elif oper == '3':
            update_acct()
        elif oper == '4':
            pass
        elif oper == '5':
            break
        else:
            print('Please input right NO!')



main()










































































