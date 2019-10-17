# class_variable2.py

# 此示例示意类变量的定义和使用方法
# 用total_count 实现对象个数的自动计数
class Human:
    total_count = 0  # 类变量,用来记录此类的实例的个数
    def __init__(self):
        self.__class__.total_count += 1
    
    def __del__(self):
        self.__class__.total_count -= 1

    def sleep(self):
        '''注:方法名也属于类变量'''
        pass 

h1 = Human()
h2 = Human()
L = [Human() for x in range(100)]
print("当前Human类型的实例个数是:", Human.total_count)
del h1  # 释放一个对象
del L[50:]  # 释放后50个
del L  # 释放绑定列表
print(Human.total_count)  # 1

