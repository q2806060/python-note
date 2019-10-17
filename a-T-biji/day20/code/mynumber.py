# mynumber.py


class MyNumber:
    '''此类用于定义一个自定义的数字类,用于示意运算符重载'''
    def __init__(self, value):
        self.data = value
    
    def __repr__(self):
        return "MyNumber(%d)" % self.data

    def __add__(self, other):
        '此方法创建一个MyNumber类型的实例,返回回去'
        print("MyNumber.__add__方法被调用!")
        v = self.data + other.data
        return MyNumber(v)

    def __sub__(self, rhs):
        return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 = n1 + n2  # 等同于 n1.__add__(n2)
print(n1, '+', n2, '=', n3)
n4 = n1 - n2
print(n1, '-', n2, '=', n4)  # MyNumber(-100)

i1 = int(100)
i2 = int(200)
# i3 = i1 + i2 # 等同于 i3 = i1.__add__(i2)
i3 = i1.__add__(i2)
print(i1, "+", i2, '=', i3)


