# with3.py

# 此示例示意将自定义的类A 创始的对象作为环境管理器
# 让A类的对象能够使用with语句进行管理

class A:
    def __enter__(self):
        print("已经进入with语句")
        return self  # 此self对象将用as变量进行绑定

    def __exit__(self, e_type, e_value, e_tb):
        '''此方法在退出with语句时被调用
        当with语句内没有异常时,e_type, e_value, e_tb
        都绑定None, 有异常时,e_type绑定错误类型,e_value
        绑定错误对象, e_tb绑定追踪对象
        '''
        print("已离开with语句")
        print("e_type=", e_type)
        print("e_value=", e_value)
        print("e_tb=", e_tb)

with A() as a: # a = A()
    print("这是with语句内部的一条语句")
    int(input("请输入数字: "))

print("程序结束")

