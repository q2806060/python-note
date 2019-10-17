from socket import *

address = ('127.0.0.1', 9999)

client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('Please input:')
    if not data:
        continue
    if data == 'q' or data == 'Q':
        break
    client.sendto(data.encode(), address)
    #接收数据
    resp, addr = client.recvfrom(1024)
    if resp:
        print('已成功发送消息：' + resp.decode())

client.close()














































































