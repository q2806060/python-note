# nonlocal.py

# 4. nonlocal 语句的变量列表里的变量名,不能出现在此函数的
#     形参列表中

v = 100
def f1():
    v = 200
    def f2():
        v = 300
        def f3(v):
            nonlocal v  # 此处会报错
            v = 400
        f3(111)
        print("f2.v=", v)
    f2()
    print("调用结束后 f1.v=", v)
f1()

