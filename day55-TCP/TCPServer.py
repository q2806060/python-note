import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(("0.0.0.0",8888))

server.listen(5)

client,addr = server.accept()

data = client.recv(1024)
print(data.decode())

client.send("server recv.".encode())

client.close()
server.close()




































