# mynumber.py


# 此示例示意在自定义的类内添加__str__方法 和 __repr__方法
# 让自定义的类能够用str(x) 和 repr(x)函数 返回自定义的字符串

class MyNumber:
    '''此类用于定义一个自定义的数值类,此类的对象的data属性
    用于绑定内部的数据'''
    def __init__(self, value):
        self.data = value
    
    def __str__(self):
        print("__str__方法被调用!")
        return "自定义数字: %d" % self.data

    def __repr__(self):
        return "MyNumber(%d)" % self.data

n1 = MyNumber(100)
n2 = MyNumber(200)
print('repr(n1)===>', repr(n1))  # repr(n1) 等同于 n1.__repr__()
print('str(n1)====>', str(n1))  # 自定义数字: 100

