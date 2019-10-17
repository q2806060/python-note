# classmethod.py

class A:
    v = 0

    @classmethod
    def get_v(cls):
        '''此方法为类方法,此方法可以获取A类的实例变量v的值'''
        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value

# 4. 类方法不能访问此类创建的对象的实例属性
a1 = A()
a2 = A()
a1.v = 100
a2.v = 200

print(a1.get_v())  # ??
