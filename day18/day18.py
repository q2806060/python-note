#1

# class Human:
#     def set_info(self, name, age, addr = '不详'):
#         self.name = name
#         self.age = age
#         self.addr = addr

#     def show_info(self):
#         print(self.name, '今年', self.age, '岁，家庭住址：', self.addr)

# s1 = Human()
# s1.set_info('小张', 20, '北京东城区')
# s2 = Human()
# s2.set_info('小李', 18)
# s1.show_info()
# s2.show_info()


#2

# class Student():
#     def __init__(self, name, age, score = 0):
#         self.name = name
#         self.age = age
#         self.score = score
#     def set_score(self, score):
#         self.score = score
#     def show_info(self):
#         print(self.name, '的年龄是：', self.age, '，成绩是：', self.score)

# l = []
# l.append(Student('小张', 20, 100))
# l.append(Student('小李', 18, 98))
# l.append(Student('小菜', 19))
# l[-1].set_score(70)
# for s in l:
#     s.show_info()



#3

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.skill = []
#     def teach(self, other, skill):
#         other.skill.append(skill)
#     def work(self, money ):
#         self.money += money
#     def borroe(self, other, money):
#         other.money -= money
#         self.money += money
#     def show_info(self):
#         print(self.age, '岁的', self.name, '有钱', self.money, '元，他学会的技能是：', self.skill)

# zhang3 = Human('张三', 35)
# li4 = Human('李四', 10)
# zhang3.teach(li4, 'python')
# li4.teach(zhang3, '王者荣耀')
# zhang3.work(1000)
# li4.borroe(zhang3, 200)
# zhang3.show_info()
# li4.show_info()


# 练习


# def isprime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# def deco(num, l = []):
#     if isprime(num):
#         l.append(str(num))
#         return l       
#     for i in range(2, num):
#         if num % i == 0:
#             l.append(str(i))
#             s = int(num / i)
#             deco(s, l)
#             return l
#     return l            
# def deco_factor(num):
#     if isprime(num):
#         print(num, '=', num, 'x', 1)
#     else:
#         l = deco(num)
#         l = 'x'.join(l)
#         print(num, '=', l)
# num = int(input('请输入一个正整数：'))
# deco_factor(num)


    



class Student:
    def set_score(self, score):
        self.score = score
    def show_info(self):
        print(self.name, '的年龄是：', self.age, '，成绩是：', self.score)
    def add_student(self):
        d = {}
        self.name = input('请输入学生姓名：')
        if not self.name:
            return
        self.age = int(input('请输入年龄：'))
        self.score = float(input('请输入成绩：'))
        d['name'] = self.name
        d['age'] = str(self.age)
        d['score'] = str(self.score)
        return d

    def del_student(self, lst):
        name = input('请输入要删除学生的姓名：')
        for i in lst:
            if i['name'] == name:
                lst.remove(i)
                print('删除成功！')
            else:
                print('您查找的对象不存在！')
    
    def student_count(self, lst):
        count = 0
        for i in lst:
            count += 1
        print('您共有学生',count,'个.') 
    def student_average_score(self, lst):
        x = len(lst)
        score_sum = sum(map(lambda d : float(d['score']), lst))
        average_score = score_sum / x
        print('您的学生平均成绩是：', average_score)
    def student_average_age(self, lst):
        x = len(lst)
        age_sum = sum(map(lambda d : float(d['age']), lst))
        average_age = age_sum / x
        print('您的学生平均年龄是：', average_age)

student_list = []
while True:     
    print('+-------------------------------------------------------+')
    print('| 1) 添加学生信息                                       |')
    print('| 2) 显示学生信息                                       |')
    print('| 3) 删除学生信息                                       |')
    print('| 4) 打印学生个数                                       |')
    print('| 5) 打印学生平均成绩                                   |')
    print('| 6) 打印学生平均年龄                                   |')
    print('| q) 退出                                               |')
    print('+-------------------------------------------------------+')
    try:
        x = input('请选择：')
        if x == '1':
            while True:
                d_student = Student()
                d = d_student.add_student()
                if not d:
                    break
                student_list.append(d)
        elif x == '2':
            pass
        elif x == '3':
            d_student = Student()
            d_student.del_student(student_list)
        elif x == '4':
            d_student = Student()
            d_student.student_count(student_list)
        elif x == '5':
            d_student = Student()
            d_student.student_average_score(student_list)
        elif x == '6':
            d_student = Student()
            d_student.student_average_age(student_list)
        elif x == 'q':
            break
    except ValueError:
        print('您输入有误，请重新输入！')
    



































