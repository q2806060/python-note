# mynumber2.py


class MyNumber:
    '''此类用于定义一个自定义的数值类,此类的对象的data属性
    用于绑定内部的数据'''
    def __init__(self, value):
        self.data = value
    
    # def __str__(self):
    #     print("__str__方法被调用!")
    #     return "自定义数字: %d" % self.data

    # def __repr__(self):
    #     print("__repr__方法被调用!")
    #     return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
# print('str(n1)====>', str(n1))

print(n1)  # 等同于 print(str(n1))

