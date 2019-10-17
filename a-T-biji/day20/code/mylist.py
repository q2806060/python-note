class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)
    
    def __rmul__(self, lhs):
        return MyList(self.data * lhs)

L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 6))
L5 = L1 * 2  # L1.__mul__(2)
print("L5=", L5)  # L5=MyList([1, 2, 3, 1, 2, 3])

L6 = 2 * L1  # L1.__rmul__(2)  反向算术运算符的重载
print(L6)

