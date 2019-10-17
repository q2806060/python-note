from socket import *

address = ('0.0.0.0', 9999)

s = socket()
s.bind(address)
s.listen(5)
sockfd, addr = s.accept()

try:
    with open('C:/Users/Administrator/Desktop/test_pic0000.jpg', 'wb') as f:
        while True:  
            data = sockfd.recv(1024)
            if not data:
                break
            f.write(data)
        print('已接收到图片！')
except:
    print('接收图片失败！')

sockfd.close()
s.close()



















































