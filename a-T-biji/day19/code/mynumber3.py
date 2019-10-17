# mynumber3.py

class MyNumber:
    def __init__(self, value):
        self.data = value  # 初始化每个对象都有一个data属性
    def __float__(self):
        '此方法必须返回浮点型数'
        return float(self.data)

    def __int__(self):
        return int(self.data)

n1 = MyNumber("100")
f = float(n1)  #  f = n1.__float__()
print('f=', f)
i = int(n1)  # i = n1.__int__()
print('i=', i)

c = complex(n1)
print(c)   # 100+0j

b = bool(n1)  # n1.__bool__()
print('b=', b)  # True

