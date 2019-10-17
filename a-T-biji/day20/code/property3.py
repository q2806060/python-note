# property3.py

# 此示例示意用特性属性对实例的属性取值和赋值加以控制
# 3. 用循性属性加以控制
class Student:
    def __init__(self, s=0):
        self.__score = s

    def get_score(self):
        '作为getter'
        return self.__score

    def set_score(self, score):
        '作为setter,限制设置值的行为'
        if score < 0 or score > 100:
            print("成绩超出范围, 设置失败")
            return
        self.__score = score

    score = property(get_score, set_score)

s = Student(58)
# v = s.get_score()  # v = s.score
# print('v=', v)
# s.set_score(99)  # s.score = 99
# print(s.get_score())  # print(s.score)

v = s.score  # 对s的score属性取值
print("v=", v)
s.score = 99  # 对s.属性赋值
print(s.score)  # 被破坏了
