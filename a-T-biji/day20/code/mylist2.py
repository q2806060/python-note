
# 此示例示意复合赋值算术运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __mul__(self, rhs):
        print("__mul__被调用")
        L =  MyList(self.data * rhs)
        print("__mul__中的L的ID为: ", id(L))
        return L
    
    def __del__(self):
        print(self, "被销毁")

L1 = MyList([1, 2, 3])
print("id(L1)=", id(L1))  # ???
L1 *= 2  # L1 = L1 * 2
print("id(L1)=", id(L1))  # ???
print("L1=", L1)  # L1 = MyList([1, 2, 3, 1, 2, 3])

print("程序结束")


