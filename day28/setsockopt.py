from socket import *

address = ('0.0.0.0', 9999)

s = socket()

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)         # so_reuseaddr 设置端口可以重复使用，允许同一个端口启动同一服务器的多个示例

s.bind(address)
print('family：', s.family)                     # 取地址类型
print('type:', s.type)                          # 取套接字类型
print('getsockname:', s.getsockname())            #地址
print('***** fileno:', s.fileno())                #
print('getsockopt:', s.getsockopt(SOL_SOCKET, SO_REUSEADDR))













































