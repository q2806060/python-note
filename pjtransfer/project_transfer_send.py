from socket import *

addr = input('请输入IP地址(本机地址127.0.0.1）：')
address = (addr, 9999)

s = socket()

s.connect(address)
try:
    pic = input('请输入图片地址：')  
    with open(pic, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.send(data)
        print('图片已发送！')
except:
    print('图片发送失败！')

s.close()