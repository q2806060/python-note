from socket import *
import struct
address = ('127.0.0.1', 9999)

client = socket(AF_INET, SOCK_DGRAM)
while True:
    id = int(input('id:'))
    name = input('name:')
    n = len(name)
    height = float(input('height:'))

    fmt = 'i%dsf' %n
    data = struct.pack(fmt, id, name.encode(), height)
    client.sendto(fmt.encode(), address)
    client.sendto(data, address)

client.close()




































