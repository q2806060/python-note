# globals_and_locals.py

a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    # print("fn内部locals() 返回", locals())
    # print("fn内部的globals()", globals())
    print('c=', c)  # 100
    print("全局的c的值是:", globals()['c'])

fn(100, 200)
# 程序走到此处有几个全局变量
# print("globals返回:", globals())
