#   3. 修改学生信息管理程序,将其修改为两个函数实现
#     函数1:
#         def input_student():
#            ....  # 此函数返回输入学生信息的列表(格式不变)
        
#     函数2:
#         def output_student(L):
#             ... 此处以表格式形式打印学生信息(表格样式不变)
    
#     测试函数:
#         infos = input_student()
#         print(infos) # 打印字典组成的列表
#         output_student(infos)  # 打印表格
#     保证修改后原功能不变


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

infos = input_student()
print(infos) # 打印字典组成的列表
output_student(infos)  # 打印表格

