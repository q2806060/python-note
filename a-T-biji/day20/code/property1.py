# property1.py

# 此示例示意用特性属性对实例的属性取值和赋值加以控制
# 1. 不加以控制
class Student:
    def __init__(self, s=0):
        self.score = s
    
s = Student(58)
v = s.score  # 对s的score属性取值
print("v=", v)
s.score = 99999999999  # 对s.属性赋值
print(s.score)  # 被破坏了
