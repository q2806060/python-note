from socket import *
from select import *

address = ('0.0.0.0', 9999)
server = socket()
server.bind(address)
server.listen(5)
print('服务器已启动:', address)

fdmap = {
    server.fileno():server
}

p = epoll()
p.register(server, EPOLLIN)

# 循环监控

while True:
    events = p.poll() # 阻塞，等待Ｉ／Ｏ事件
    for fd, e in events:
        sock = fdmap[fd]
        if fd == server.fileno():
            client, addr = server.accept()
            print('收到连接：', addr)
            p.register(client, EPOLLIN|EPOLLET)
            fdmap[client.fileno()] = client
        elif e & EPOLLIN:
            data = sock.recv(1024)
            if not data:
                p.unregister(fd)
                sock.close()
                del sock
            else:
                print('收到数据：', data.decode())
                sock.send(b"test mag")