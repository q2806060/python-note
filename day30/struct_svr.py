from socket import *
import struct
address = ('0.0.0.0', 9999)
server = socket(AF_INET, SOCK_DGRAM)
server.bind(address)
while True:
    data, addr = server.recvfrom(1024)
    fmt = data.decode()
    print(fmt)
    data, addr = server.recvfrom(1024)
    msg = struct.unpack(fmt, data)
    print(msg)

server.close()






































