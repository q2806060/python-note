from socket import *

address = ('192.168.191.3', 9999)

s = socket()

s.connect(address)
try:
    with open('C:/Users/Administrator/Desktop/test_pic.jpg', 'rb') as p:
        while True:
            data = p.read(1024)
            if not data:
                break
            s.send(data)
        print('图片已发送！')
except:
    print('图片发送失败！')

s.close()



    























































