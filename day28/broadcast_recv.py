from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(('0.0.0.0', 9999))

while True:
    try:
        msg, addr = s.recvfrom(1024)
        print('收到信息：', msg.decode())
    except:
        print('接收异常！')
        break

s.close()













































































