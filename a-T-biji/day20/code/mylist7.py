
# 此示例示意 索引和切片运算符 [] 的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    
    def __repr__(self):
        return "MyList(%s)" % self.data

    def __getitem__(self, i):  # 索引取值的方法
        print("__getitem__被调用! i=", i)
        if type(i) is int:
            print("用户正在做索引操作")
        elif type(i) is slice:
            print("用户正在做切片操作")
            print("起始值是:", i.start)
            print("终止值是:", i.stop)
            print("步长值是:", i.step)
        return self.data[i]

    def __setitem__(self, i, val):
        print("__setitem__被调用!, i=", i, 'val=', val)
        self.data[i] = val  # 修改内建列表的第i个元素的值为val

    def __delitem__(self, i):
        print("__delitem__被调用!")
        self.data.pop(i)  # 删除i对应的元素

L1 = MyList([1, -2, 3, -4, 5])
lst = L1[::2]
print('lst =', lst)
lst = L1[1:10:2]





