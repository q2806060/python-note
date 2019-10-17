import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",8888))

msg = input("what do you want to say:")
client.send(msg.encode())

data = client.recv(1024)
print(data.decode())

client.close()
























