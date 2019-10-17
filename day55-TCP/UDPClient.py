import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input("what do you want to say:")
    if not msg:
        break
    client.sendto(msg.encode(),("127.0.0.1",8888))
    data,addr = client.recvfrom(1024)
    print(data.decode())

client.close()
























