# del_method.py

class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", info, '对象被创建')

    def __del__(self):
        '''析构方法,不能有除self以外的其它形参'''
        print("汽车", self.info, '将被销毁!')

c1 = Car("BYD EV450")  # 创建对象
L = []
L.append(c1)
del c1  # 请问此时汽车对象会被销毁吗?
input("请输入回车键结束程序执行!")

print("程序结束")
