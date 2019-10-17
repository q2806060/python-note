# len_overwrite.py


# 此示例示意自定义的类创建的对象能够使用len(x) 函数  
# 和 abs(x) 函数

class MyList:
    '''自定义的容器类,内部使用内建的列表保存数据'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        '''此方法为len(x)调用,此方法的返回值必须为整数'''
        return len(self.data)
        # return len(self)  # 递归调用... 出错
        # return 9999

myl = MyList([1, -2, 3, -4])
print(myl)
print(len(myl))  # 调用myl.__len__()

myl2 = MyList()  # 无参
print('myl2 =', myl2)
print(len(myl2))  # 0

