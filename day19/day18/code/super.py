# super.py

# 此示例示意super函数的使用
class A:
    def work(self):
        print("A.work被调用!")
    
class B(A):
    def work(self):
        print("B.work被调用")

    def do_work(self):
        # 1. 调用B类的work方法
        self.work()
        # 2. 调用A类的work方法
        super(B, self).work()
        # 3.  如果在方法内调用,可以写为如下:
        super().work()  # 等同于super(B, self).work

b = B()  # 创建一个实例 
# b.work()  # B.work被调用
# super(B, b).work()  # A.work被调用
b.do_work()
super().work()  # 出错,super无参调用只能在方法中调用



