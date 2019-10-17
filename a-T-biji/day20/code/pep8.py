# 此示例示意 PEP8编码规范

import time
import sys

import tensorflow

import mymod  # 自己写的

class Student:
    def __init__(self, s=0):
        self.__score = s

    @property
    def score(self):
        '作为getter'
        return self.__score

    @score.setter
    def score(self, score):
        '作为setter,限制设置值的行为'
        if score<0 or score>100:
            print("成绩超出范围, 设置失败")
            return
        self.__score = score


s = Student(58)
v = s.score  # 对s的score属性取值
print("v=", v)
s.score = 99  # 对s.属性赋值
print(s.score)  # 被破坏了
x = 1 * 2 + 3 * 4 - 5