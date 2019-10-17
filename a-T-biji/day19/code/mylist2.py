
# 此示例示意可迭代对象很 迭代器的定义方法及调用

class MyList:
    '''将此类改为可迭代对象'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __iter__(self):
        '''有此方法的对象可以称之为可迭代对象
        此方法必须返回迭代器
        '''
        return MyListIterator(self.data)  # 创建迭代器

class MyListIterator:
    '''此类的对象是用于访问MyList对象的迭代器
    此类要作为迭代器则必须有__next__(self) 方法来实现
    迭代器协议
    '''
    def __init__(self, data):
        self.data = data  # 绑定可迭代对象的数据
        self.index = 0  # 代表self.data 列表的索引
    
    def __next__(self):
        '''有此方法的类的对象被称为迭代器'''
        print("__next__被调用!")
        if self.index >= len(self.data):
            raise StopIteration  # 不再提供数据
        r = self.data[self.index]
        self.index += 1
        return r


# for x in MyList("ABC"):
#     print(x)   # A B C

# 以上语句等同于
myl = MyList("123")
print(myl)
it = iter(myl)  # it = myl.__iter__()
while True:
    try:
        x = next(it)  # x = it.__next__()
        print(x)
    except StopIteration:
        break
