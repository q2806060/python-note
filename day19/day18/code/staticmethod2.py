# staticmethod.py

# 引示例示意静态方法的定义和使用
class A:
    @staticmethod
    def myadd(a, b):
        return a + b
    
print(A.myadd(100, 200))  # 300
a = A()
print(a.myadd(30, 40))  # 70