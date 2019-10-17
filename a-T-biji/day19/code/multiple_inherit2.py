# multiple_inherit2.py

# 此示例示意多继承中存在名字冲突的问题
# 小张写了一个类A
class A:
    def m(self):
        print("A.m被调用")

# 小李写了一个类B
class B:
    def m(self):
        print('B.m被调用')

# 小王感觉小张和小李写的两个类自己可以用
# class AB(B, A):
class AB(A, B):  # 继承列表的先后顺序会影响最终的结果
    pass

ab = AB()
ab.m()  # 请问调用谁?

