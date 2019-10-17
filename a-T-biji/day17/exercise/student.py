# 练习:
#   1. 写一个学生类Student类.此类用于描述学生信息,学生信息有:
#      姓名,年龄,成绩(默认为0)
#     1) 为该类添加初始化方法,实现在创建对象时自动设置:
#        姓名(name),年龄(age), 成绩(score)属性
#     2) 添加set_score方法能力对象修改成绩信息
#     3) 添加show_info方法打印学生对象的信息
#   如:
#     class Student:
#         def __init__(...):
#             ...
#         def set_score(self, score):
#             ...
#         def show_info(self):
#             ...
#     L = []
#     L.append(Student("小张", 20, 100))
#     L.append(Student("小李", 18, 98))
#     L.append(Student("小菜", 19))
#     L[-1].set_score(70)
#     for s in L:
#         s.show_info()  # 列出所有学生的信息




class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self, score):
        self.score = score  # 修改学生成绩

    def show_info(self):
        print(self.name, '今年', self.age,
              '岁,成绩是:', self.score)
L = []
L.append(Student("小张", 20, 100))
L.append(Student("小李", 18, 98))
L.append(Student("小菜", 19))
L[-1].set_score(70)
for s in L:
    s.show_info()  # 列出所有学生的信息

# print(len(L))  # 3