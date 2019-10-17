

class Student:
    def __init__(self, name, age, score=0):
        self.__name = name
        self.__age = age
        self.__score  = score

    def get_info(self):
        return self.__name, self.__age, self.__score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score






































