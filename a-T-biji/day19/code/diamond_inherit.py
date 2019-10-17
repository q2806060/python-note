# diamond_inherit.py

# 此示例示意 python棱形继承的问题
#      A
#     / \
#    B   C
#     \ /
#      D

class A:
    def go(self):
        print('A')
        # super().go()  # 出错,object类没有go方法
    
class B(A):
    def go(self):
        print('B')
        super().go()  # C

class C(A):
    def go(self):
        print('C')
        super(C, self).go()

class D(B, C):
    def go(self):
        print('D')
        super().go()
        A.go(self)  # 借助于A类直接调用A类的go方法
        super(C, self).go()  # 调用A类的go方法 

d = D()
d.go()  # ???

print("-------以下打印D类的__mro__----------")
for cls in D.__mro__:
    print(cls)

