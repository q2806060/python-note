from socket import *

dest = ('176.40.91.255', 9999)

s = socket(AF_INET, SOCK_DGRAM)         # UPD套接字

s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

msg = 'Broadcast test message'

s.sendto(msg.encode(), dest)
print('你就是个弟弟！')
s.close()



























































