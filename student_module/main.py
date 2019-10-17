from menu import show_menu
import student_info


def main():
    students_list = student_info.read_info()   
    while True:  
        show_menu()
        s = input('请选择：')       
        if s == '1':
            while True:
                s = student_info.add_students()
                if s == 'q':
                    break
                students_list.append(s)
        elif s == '2':
            student_info.view_students(students_list)
        elif s == '3':
            student_info.del_students(students_list)
        elif s == '4':
            student_info.modify_student_score(students_list)
        elif s == '5':
            student_info.scores_high(students_list)
        elif s == '6':
            student_info.scores_low(students_list)
        elif s == '7':
            student_info.age_high(students_list)
        elif s == '8':
            student_info.age_low(students_list) 
        elif s == '9':           
            students_list = student_info.read_info()
        elif s == '10':
            student_info.save_info(students_list)
        elif s == 'q':
            break
        else:
            print('您选择错误，请重新输入！')
main()









