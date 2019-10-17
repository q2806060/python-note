#   2. 用类来描述一个学生信息(可以修改之前写的Student类)
#     class Student:
#         此处自己实现
#     学生信息有:
#        姓名,年龄, 成绩
#     将这些学生的对象存于列表中,可以任意添加和删除学生信息
#      1) 打印出学生的个数
#      2) 打印出所有学生的平均成绩
#      3) 打印出所有学生的平均年龄


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s


L = []
L.append(Student("小张", 20, 100))
L.append(Student('小李', 18, 98))
L.append(Student('小赵', 19, 88))
L.append(Student('小钱', 17, 70))

#  1) 打印出学生的个数
print('学生数是:', len(L))
#  2) 打印出所有学生的平均成绩
total_score = 0
for s in L:
    total_score += s.score
print("平均成绩是:", total_score/len(L))
print("平均成绩是:", sum(map(lambda s: s.score, L))/len(L))

#  3) 打印出所有学生的平均年龄
print("平均年龄:", sum((s.age for s in L))/len(L))
