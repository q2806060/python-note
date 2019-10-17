import student

def add_students(): 
    try:
        name = input('请输入学生姓名：')
        if name == 'q':
            return name
        age = int(input('请输入学生年龄：'))
        score = float(input('请输入学生成绩：'))
        student_ = student.Student(name, age, score)
        print('添加成功！')
        return student_
    except ValueError:
        print('您输入有误，请重新输入！')

def view_students(students_list):
    print('+----------------+------------+------------+')
    print('|     name       |     age    |   score    |')
    print('+----------------+------------+------------+')
    for i in students_list:
        print('|' + i.get_name().center(16) + '|' + str(i.get_age()).center(12) + '|' + str(i.get_score()).center(12) + '|')
    print('+----------------+------------+------------+')


def del_students(students_list):
    del_name = input('请输入姓名：')
    for name_ in students_list:
        if del_name == name_.get_name():
            students_list.remove(name_)
            print('删除成功！')
            return
        else:
            print('你输入的姓名不存在！请选择重新删除！')

def modify_student_score(students_list):
    modify_student = input('请输入姓名：')
    for modify_student_ in students_list:
        if modify_student == modify_student_.get_name():
            modified_score = input('请输入修改后的成绩：')
            modify_student_.set_score(modified_score)
            print('修改成功！')
            return
        else:
            print('你输入的姓名不存在！请选择重新修改！')

def scores_high(students_list):
    students_list_new = sorted(students_list, key=lambda d:float(d.get_score()), reverse=True)
    view_students(students_list_new)
        
def scores_low(students_list):
    students_list_new = sorted(students_list, key=lambda d:float(d.get_score()))
    view_students(students_list_new)


def age_high(students_list):
    students_list_new = sorted(students_list, key=lambda d:int(d.get_age()), reverse=True)
    view_students(students_list_new)
        
def age_low(students_list):
    students_list_new = sorted(students_list, key=lambda d:int(d.get_age()))
    view_students(students_list_new)


def read_info():
    try:    
        s_file = open('si.txt')
        try:
            l = []
            for i in s_file.readlines():
                l1 = i.split()
                student_ = student.Student(l1[1], l1[3], l1[5])
                l.append(student_)
        finally:
            s_file.close()
        print('读取数据成功！')
    except OSError:
        print('读取数据失败！')
    return l

def save_info(students_list):
    try:
        s_file = open('si.txt', 'w')
        try:
            for d in students_list:
                s = 'name: ' + d.get_name() + '  age: ' + str(d.get_age()) + '  score: ' + str(d.get_score()) + '\n'
                s_file.write(s)
        finally:
            s_file.close()
        print('保存成功！')
    except OSError:
        print('保存失败！')





