#   3. 改写之前的学生信息管理程序
#     要求添加四个功能:
#       | 5) 按学生成绩高~低显示学生信息 |
#       | 6) 按学生成绩低~高显示学生信息 |
#       | 7) 按学生年龄高~低显示学生信息 |
#       | 8) 按学生年龄低~高显示学生信息 |


def input_student():
    L = []  # 先创建一个空列表．准备放学生信息的字典
    while True:
        n = input("请输入学生姓名: ")
        if not n:  # 如果姓名为空，结束输入
            break
        a = int(input("请输入学生年龄: "))
        s = int(input("请输入学生成绩: "))
        # 形成字符对象
        d = {}  # 每次创建一个新的字典.来存放当前学生的数据
        d['name'] = n
        d['age'] = a
        d['score'] = s
        # 放到列表中
        L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|     姓名      |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        n = d['name']
        a = d['age']  # a 绑定的是整数
        s = d['score']
        a = str(a)
        s = str(s)  # 将整数转为字符串
        print("|%s|%s|%s|" % (n.center(15),
                            a.center(10),
                            s.center(10)))
    print("+---------------+----------+----------+")

def delete_student_info(L):
    '''L绑定的是列表对象'''
    n = input("请输入要删除的学生姓名: ")
    # 方法1
    # for d in L:
    #     if d['name'] == n:
    #         L.remove(d)
    for i in range(len(L)):  # i代表索引
        d = L[i]
        if d['name'] == n:
            del L[i]  # 根据索引来删除 或 L.pop(i)
            print("删除", n, "成功")
            return
    print("删除失败!")

def modify_student_score(L):
    n = input("请输入要修改的学生的姓名: ")
    for i in range(len(L)):
        d = L[i]
        if d['name'] == n:
            # 修改学生成绩
            s = int(input("请输入要修改的新成绩: "))
            d['score'] = s
            print("成功修改", n, '的成绩为:', s)
            # 返回
            return
    print(n, "这个学生不存在")


def output_student_by_score_desc(L):
    # 先对L进行降度排序, 生成一个新列表L2
    def get_score(d):  # d用来绑定列表里的字典
        return d['score']
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    L2 = sorted(L, key=lambda d: d['score'])
    output_student(L2)

def output_student_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(L2)

def output_student_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d['age'])
    output_student(L2)




def show_menu():
    print("+--------------------------------+")
    print("| 1) 添加学生信息                |")
    print("| 2) 显示学生信息                |")
    print("| 3) 删除学生信息                |")
    print("| 4) 修改学生成绩                |")
    print("| 5) 按学生成绩高~低显示学生信息 |")
    print("| 6) 按学生成绩低~高显示学生信息 |")
    print("| 7) 按学生年龄高~低显示学生信息 |")
    print("| 8) 按学生年龄低~高显示学生信息 |")
    print("| q) 退出                        |")
    print("+--------------------------------+")

def main():
    infos = []
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            # 删除学生信息
            delete_student_info(infos)
        elif s == '4':
            # 修改学生成绩
            modify_student_score(infos)
        elif s == '5':
            output_student_by_score_desc(infos)
        elif s == '6':
            output_student_by_score_asc(infos)
        elif s == '7':
            output_student_by_age_desc(infos)
        elif s == '8':
            output_student_by_age_asc(infos)
        elif s == 'q':
            break
main()