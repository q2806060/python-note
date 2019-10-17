#学生信息录入系统

def add_students():
    d = {}
    name = input('请输入学生姓名：')
    age = input('请输入学生年龄：')
    score = input('请输入学生成绩：')
    d['name'] = name
    d['age'] = age
    d['score'] = score
    print('添加成功！')
    return d

def view_students(students_list):
    print('+----------------+------------+------------+')
    print('|     name       |     age    |   score    |')
    print('+----------------+------------+------------+')
    for i in students_list:
        print('|' + i['name'].center(16) + '|' + i['age'].center(12) + '|' + i['score'].center(12) + '|')
    print('+----------------+------------+------------+')


def del_students(students_list):
    del_name = input('请输入姓名：')
    for name_dict in students_list:
        if del_name in name_dict.values():
            students_list.remove(name_dict)
            print('删除成功！')
            return

def modify_student_score(students_list):
    modify_student = input('请输入姓名：')
    modified_score = input('请输入修改后的成绩：')
    for modify_student_dict in students_list:
        if modify_student in modify_student_dict.values():
            modify_student_dict['score'] = modified_score
            print('修改成功！')
            return

def scores_high(students_list):
    scores_list = []
    students_list_new = []
    for student_list in students_list:
        scores_list.append(int(student_list['score']))
        scores_list.sort(reverse = True)
    for score in scores_list:
        for student_list in students_list:
            if score == int(student_list['score']):
                students_list_new.append(student_list)
                students_list.remove(student_list)
    view_students(students_list_new)
    return students_list_new
        
def scores_low(students_list):
    scores_list = []
    students_list_new = []
    for student_list in students_list:
        scores_list.append(int(student_list['score']))
        scores_list.sort()
    for score in scores_list:
        for student_list in students_list:
            if score == int(student_list['score']):
                students_list_new.append(student_list)
                students_list.remove(student_list)
    view_students(students_list_new)
    return students_list_new


def age_high(students_list):
    ages_list = []
    students_list_new = []
    for student_list in students_list:
        ages_list.append(int(student_list['age']))
        ages_list.sort(reverse = True)
    for age in ages_list:
        for student_list in students_list:
            if age == int(student_list['age']):
                students_list_new.append(student_list)
                students_list.remove(student_list)
    view_students(students_list_new)
    return students_list_new
        
def age_low(students_list):
    ages_list = []
    students_list_new = []
    for student_list in students_list:
        ages_list.append(int(student_list['age']))
        ages_list.sort()
    for age in ages_list:
        for student_list in students_list:
            if age == int(student_list['age']):
                students_list_new.append(student_list)
                students_list.remove(student_list)
    view_students(students_list_new)
    return students_list_new



def main():  
    students_list = []
    while True:
        print('+-------------------------------------------------------+')
        print('| 1) 添加学生信息                                       |')
        print('| 2) 显示学生信息                                       |')
        print('| 3) 删除学生信息                                       |')
        print('| 4) 修改学生信息                                       |')
        print('| 5) 按学生成绩高~低显示学生信息                        |')
        print('| 6) 按学生成绩低~高显示学生信息                        |')
        print('| 7) 按学生年龄高~低显示学生信息                        |')
        print('| 8) 按学生年龄低~高显示学生信息                        |')
        print('| q) 退出                                               |')
        print('+-------------------------------------------------------+')
        s = input('请选择：')
        if s == '1':
            students_list.append(add_students())
        if s == '2':
            view_students(students_list)
        if s == '3':
            del_students(students_list)
        if s == '4':
            modify_student_score(students_list)
        if s == '5':
            students_list = scores_high(students_list)
        if s == '6':
            students_list = scores_low(students_list)
        if s == '7':
            students_list = age_high(students_list)
        if s == '8':
            students_list = age_low(students_list) 
        if s == 'q':
            break

main()






















































