
class MyList:
    '''自定义的容器类,内部使用内建的列表保存数据'''
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __len__(self):
        '''bool(self) 第一步找__len__,如果返回0为假,
        返回非零值为真
        '''
        print("__len__方法被调用!")
        return len(self.data)
    
    def __bool__(self):
        'bool(self) 第一步找__bool__方法'
        print("__bool__方法被调用!")
        return False

myl = MyList([1, -2, 3, -4])
print(bool(myl))  # False
if myl:
    print("myl值为真")
else:
    print("myl值为假")
