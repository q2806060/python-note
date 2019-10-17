# 练习:
#   实现两个自定义的列表相加等操作
#     class MyList:
#         .... 此处自己实现
#     L1 = MyList([1, 2, 3])
#     L2 = MyList(range(4, 6))
#     L3 = L1 + L2
#     print("L3=", L3)  # L3=MyList([1, 2, 3, 4, 5])
#     L4 = L2 + L1
#     print("L4=", L4)  # L4=MyList([4, 5, 1, 2, 3])
#     L5 = L1 * 2
#     print("L5=", L5)  # L5=MyList([1, 2, 3, 1, 2, 3])



class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)
        
L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 6))
L3 = L1 + L2  # L3=L1.__add__(L2)
print("L3=", L3)  # L3=MyList([1, 2, 3, 4, 5])
L4 = L2 + L1
print("L4=", L4)  # L4=MyList([4, 5, 1, 2, 3])
L5 = L1 * 2
print("L5=", L5)  # L5=MyList([1, 2, 3, 1, 2, 3])

# 思考
L6 = 2 * L1  # 2.__mul__(L1)
print(L6)

