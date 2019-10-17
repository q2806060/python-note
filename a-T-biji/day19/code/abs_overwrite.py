# abs_overwrite.py


# 此示例示意自定义的列表能够使用abs(x) 函数 返回所有元素都为
# 正数的列表

class MyList:
    '''自定义的容器类,内部使用内建的列表保存数据'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        return len(self.data)

    def __abs__(self):
        '''此方法用来制定abs(obj) 函数的返回值的规则'''
        print("__abs__方法被调用!")
        L = [abs(x) for x in self.data]
        L2 = MyList(L)
        return L2

myl = MyList([1, -2, 3, -4])
print(myl)
print(len(myl))  # 调用myl.__len__()

myl2 = abs(myl)  # myl2 = MyList([1, 2, 3, 4])
print("myl2=", myl2)
