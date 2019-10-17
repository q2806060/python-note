# 简单客户端
import socket

address = ('127.0.0.1', 9999)

client = socket.socket()   # 创建socket

client.settimeout(5)
client.connect(address)    # 连接服务器端口：connect()函数

while True:
    msg = input('请输入发送信息：')
    if msg == 'q' or msg == 'Q':
        break

    client.send(msg.encode())  # 发送消息：send()函数
    
    print('消息已发送！')
    data = client.recv(1024)
    print(data.decode())

client.close()   # 关闭连接





























































