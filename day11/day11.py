#1

# fx = lambda n : (n ** 2 + 1) % 5 == 0
# print(fx(3))
# print(fx(4))


#2

# mymax = lambda x, y : x if x > y else y
# print(mymax(100, 200))

# def fx(f, x, y):
#     print(f(x, y))

# fx((lambda a, b : a + b), 100, 200)
# fx((lambda c, d : c ** d), 3, 4)


#3


# while True:
#     a = input('请输入程序：>>>')
#     if a == 'quit()':
#         break
#     exec(a)


# 练习

# def mysum(n):
#     a = 0
#     for i in range(1, n+1):
#         a += i
#     return a

# print(mysum(100))


# def myfac(n):
#     a = 1
#     for i in range(1, n+1):
#         a *= i
#     return a

# print(myfac(5))


# def mypow(n):
#     a = 0
#     for i in range(1, n+1):
#         a += i ** i
#     return a

# print(mypow(3))




# def add_students():
#     d = {}
#     name = input('请输入学生姓名：')
#     age = input('请输入学生年龄：')
#     score = input('请输入学生成绩：')
#     d['name'] = name
#     d['age'] = age
#     d['score'] = score
#     print('添加成功！')
#     return d

# def view_students(students_list):
#     print('+----------------+------------+------------+')
#     print('|     name       |     age    |   score    |')
#     print('+----------------+------------+------------+')
#     for i in students_list:
#         print('|' + i['name'].center(16) + '|' + i['age'].center(12) + '|' + i['score'].center(12) + '|')
#     print('+----------------+------------+------------+')

# def del_students(students_list):
#     del_name = input('请输入姓名：')
#     for name_dict in students_list:
#         if del_name in name_dict.values():
#             students_list.remove(name_dict)
#             print('删除成功！')
#             return

# def modify_student_score(students_list):
#     modify_student = input('请输入姓名：')
#     modified_score = input('请输入修改后的成绩：')
#     for modify_student_dict in students_list:
#         if modify_student in modify_student_dict.values():
#             modify_student_dict['score'] = modified_score
#             print('修改成功！')
#             return


# def main():  
#     students_list = []
#     while True:
#         print('+-------------------------------------------------------+')
#         print('| 1) 添加学生信息                                       |')
#         print('| 2) 显示学生信息                                       |')
#         print('| 3) 删除学生信息                                       |')
#         print('| 4) 修改学生信息                                       |')
#         print('| q) 退出                                               |')
#         print('+-------------------------------------------------------+')
#         s = input('请选择：')
#         if s == '1':
#             students_list.append(add_students())
#         if s == '2':
#             view_students(students_list)
#         if s == '3':
#             del_students(students_list)
#         if s == '4':
#             modify_student_score(students_list)
#         if s == 'q':
#             break

# main()















































































