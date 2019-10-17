# inherit.py


# 此示例示意单继承的语法
class Human:
    '''此类描述人类的共有行为'''
    def say(self, what):  # 说话
        print("说:", what)
    
    def walk(self, distance):  # 走路
        print("走了", distance, '公里')

class Student(Human):
    # def say(self, what):  # 说话
    #     print("say:", what)
    
    # def walk(self, distance):  # 走路
    #     print("走了", distance, '公里')
    def study(self, subject):  # 学习
        print("学习:", subject)

class Teacher(Human):
    def teach(self, subject):
        print("教:", subject)

t1 = Teacher()
t1.teach('面向对象')
t1.walk(6)
t1.say("今天晚上吃点什么?")

s1 = Student()
s1.walk(4)
s1.say("感觉有点")
s1.study("Python")

h1 = Human()
h1.say("天气真好!")
h1.walk(5)




