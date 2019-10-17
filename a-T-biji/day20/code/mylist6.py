
# 此示例示意 索引和切片运算符 [] 的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):  # 索引取值的方法
        print("__getitem__被调用! i=", i)
        return self.data[i]

    def __setitem__(self, i, val):
        print("__setitem__被调用!, i=", i, 'val=', val)
        self.data[i] = val  # 修改内建列表的第i个元素的值为val

    def __delitem__(self, i):
        print("__delitem__被调用!")
        self.data.pop(i)  # 删除i对应的元素

L1 = MyList([1, -2, 3, -4, 5])
v = L1[1]  # v = L1.__getitem__(1)
print("v=", v)  # -2

L1[1] = 2  # L1.__setitem__(1, 2)
print(L1)  # MyList([1, 2, 3, -4, 5])

del L1[3]  # L1.__delitem(3)
print(L1)  # MyList([1, 2, 3, 5])





