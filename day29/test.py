from socket import *
from select import *

server = socket()
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print('服务器已启动！')

rlist = [server]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    print('监控到有I/O事件发生！')

    # 遍历返回I/O列表，依次进行处理
    for r in rs:
        
        if r is server:
            client, addr = server.accept()
            print('收到新的连接：', addr)
            rlist.append(client)

        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                continue
            else:
                print('收到数据：', data.decode())
                wlist.append(r) 

    for w in ws:
        w.send('Test masg!'.encode())
        wlist.remove(w)
    for x in xs:
        pass


server.close()
































































