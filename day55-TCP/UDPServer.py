import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(('0.0.0.0',8888))

while True:
    data,addr = server.recvfrom(1024)
    if not data:
        break
    print(addr,"say",data.decode())
    server.sendto("server recv".encode(),addr)

server.close()





































