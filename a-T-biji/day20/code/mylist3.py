
# 此示例示意复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        print("__mul__被调用")
        return MyList(self.data * rhs)

    def __imul__(self, rhs):
        print("__imul__被调用!")
        self.data *= rhs  # 修改原来内部的列表
        return self
    
    def __del__(self):
        print(self, "被销毁")

L1 = MyList([1, 2, 3])
print("id(L1)=", id(L1))  # ???
L1 *= 2  # 1. L1 = L1.__mul__(2)  或  L1.__imul__(2)
print("id(L1)=", id(L1))  # ???
print("L1=", L1)  # L1 = MyList([1, 2, 3, 1, 2, 3])

print("程序结束")


