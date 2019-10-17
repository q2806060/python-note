
# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        gen = (-x for x in self.data)  # 创建一个生成器
        return MyList(gen)
    
    def __pos__(self):
        gen = (abs(x) for x in self.data)
        return MyList(gen)

L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1
print("L2=", L2)  # L2 = MyList([-1, 2, -3, 4, -5])
L3 = +L1
print("L3=", L3)  # L3 = MyList([1, 2, 3, 4, 5])




