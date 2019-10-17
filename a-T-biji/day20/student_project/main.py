
from menu import show_menu
from student_info import *

def main():
    infos = []  # 用来保存信息的最重要的列表
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
        elif s == '9':
            infos = read_from_file()
        elif s == '10':
            save_to_file(infos)
        elif s == 'q':
            break
main()