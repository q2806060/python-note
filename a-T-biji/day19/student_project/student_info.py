
from student import Student

def input_student():
    L = []  # 先创建一个空列表．准备放学生信息的字典
    while True:
        n = input("请输入学生姓名: ")
        if not n:  # 如果姓名为空，结束输入
            break
        try:
            a = int(input("请输入学生年龄: "))
            s = int(input("请输入学生成绩: "))
        except ValueError:
            print("您的输入有误,请按回车键重新输入:")
            input()
            continue

        d = Student(n, a, s)  # 创建新对象
        L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        n, a, s = d.get_infos()
        a = str(a)
        s = str(s)  # 将整数转为字符串
        print("|%s|%s|%s|" % (n.center(15),
                            a.center(10),
                            s.center(10)))
    print("+---------------+----------+----------+")

def delete_student_info(L):
    '''L绑定的是列表对象'''
    n = input("请输入要删除的学生姓名: ")

    for i in range(len(L)):  # i代表索引
        d = L[i]
        if d.get_name() == n:
            del L[i]  # 根据索引来删除 或 L.pop(i)
            print("删除", n, "成功")
            return
    print("删除失败!")

def modify_student_score(L):
    n = input("请输入要修改的学生的姓名: ")
    for i in range(len(L)):
        d = L[i]
        if d.get_name() == n:
            # 修改学生成绩
            s = int(input("请输入要修改的新成绩: "))
            # d.score = s
            d.set_score(s)
            print("成功修改", n, '的成绩为:', s)
            # 返回
            return
    print(n, "这个学生不存在")


def output_student_by_score_desc(L):
    # 先对L进行降度排序, 生成一个新列表L2
    def get_score(d):  # d用来绑定列表里的字典
        return d.get_score()
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    L2 = sorted(L, key=lambda d: d.get_score())
    output_student(L2)

def output_student_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d.get_age(), reverse=True)
    output_student(L2)

def output_student_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d.get_age())
    output_student(L2)


def read_from_file():
    L = []
    # 从si.txt 中读取数据
    try:
        fr = open('si.txt')
        try:
            for line in fr:
                line = line.rstrip()  # 去掉左侧的'\n'
                n, a, s = line.split(',')  # ['xiaozhang', '20', '100']
                a = int(a)
                s = int(s)  # 转为整数
                L.append(Student(n, a, s))
        finally:
            fr.close()
        print("读取数据成功!")
    except OSError:
        print("读取数据失败")
    return L

def save_to_file(L):
    # 文件数据到文件 si.txt 中
    try:
        fw = open('si.txt', 'w')
        try:
            for d in L:
                # 方法1
                # fw.write(d.get_name())
                # fw.write(',')
                # fw.write(str(d.get_age()))
                # fw.write(',')
                # fw.write(str(d.get_score()))
                # fw.write('\n')
                # 方法2
                d.write_to_file(fw)
        finally: 
            fw.close()
        print("保存成功!")
    except OSError:
        print("保存失败!")


