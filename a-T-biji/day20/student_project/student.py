# student.py

# 此类用于描述学生对象:
#  属性: 姓名,年龄,成绩
#  方法:

class Student:
    def __init__(self, n, a, s=0):
        self.__name = n  # 姓名
        self.__age = a
        self.__score = s

    def get_infos(self):
        return (self.__name, self.__age, self.__score)

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        # assert 0<= self.__score <= 100, '成绩超出范围'
        if 0 <= score <= 100:
            self.__score = score

    def write_to_file(self, fw):
        print(self.__name, ',', self.__age, ',',
              self.__score, sep='', file=fw)











