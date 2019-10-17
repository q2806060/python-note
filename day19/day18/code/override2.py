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
# b.work()  # B.work被调用
A.work(b)  # A.work被调用  当覆盖发生时,可以显式调用父类的被覆盖版本的函数
