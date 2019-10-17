from socket import *

address = ('0.0.0.0', 9999)

s = socket()
s.bind(address)
s.listen(5)
sockfd, addr = s.accept()

try:
    addr_save = input('请输入图片存储路径(盘字母大写）：')
    pic_save = input('请输入图片存储名称：')
    with open(addr_save + '/' + pic_save + '.jpg', 'wb') as f:
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



