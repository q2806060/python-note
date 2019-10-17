# override.py

# 此示例示意覆盖的用法
class A:
    def work(self):
        print("A.work被调用!")
    
class B(A):
    '''B类继承自A类'''
    def work(self):
        print("B.work被调用")
    pass

b = B()
b.work()  # B.work被调用

b = A()
b.work() # A.work被调用,根据b绑定的对象的类型来进行查找

