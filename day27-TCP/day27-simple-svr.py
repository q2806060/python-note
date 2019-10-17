# 简单的网络服务器
import socket
import time

address = ('0.0.0.0', 9999)

server = socket.socket()  # 创建socket

server.bind(address)   # 绑定地址

server.listen(10)    # 监听

sockfd, addr = server.accept()    # 接收请求：accept() 函数

while True:
    data = sockfd.recv(1024)   # 数据接收：recv()
    if not data:
        break
    
    print(data.decode())
    time.sleep(10)
    sockfd.send('time test'.encode())

sockfd.close()   # 关闭通信socket

server.close()   # 关闭监听socket



































































