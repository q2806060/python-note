# student.py

# 此类用于描述学生对象:
#  属性: 姓名,年龄,成绩
#  方法:

class Student:
    def __init__(self, n, a, s=0):
        self.name = n  # 姓名
        self.age = a
        self.score = s

    def get_infos(self):
        return (self.name, self.age, self.score)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        # assert 0<= self.score <= 100, '成绩超出范围'
        if 0 <= score <= 100:
            self.score = score

    def write_to_file(self, fw):
        print(self.name, ',', self.age, ',',
              self.score, sep='', file=fw)











