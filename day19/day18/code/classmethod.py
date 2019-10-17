# classmethod.py

# 此示例示意类方法的定义和使用
class A:
    v = 0

    @classmethod
    def get_v(cls):
        '''此方法为类方法,此方法可以获取A类的实例变量v的值'''
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

print(A.v)  # 直接访问类变量
print(A.get_v())  # 这是调用类方法来获取类变量v的值
A.set_v(100)
print(A.get_v())  # 100
print(A.v)  # 100
