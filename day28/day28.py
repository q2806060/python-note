from socket import *

address = ('0.0.0.0', 9999)

server = socket(AF_INET, SOCK_DGRAM)

server.bind(address)
print('服务器已启动：', address)

while True:
    data, addr = server.recvfrom(1024)
    if not data:
        break
    print('收到数据：', data.decode())
    print('接受自：', addr)
    # 回数据
    resp = '已收到消息:' + data.decode()
    server.sendto(resp.encode(), addr)

server.close()

















































































