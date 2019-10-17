# nonlocal.py


v = 100
def f1():
    v = 200
    print("f1.v=", v)
    def f2():
        nonlocal v  # 声明v不是局部变量,也不是全局变量
        v = 300
        print("f2.v=", v)
    
    f2()
    print("调用结束后 f1.v=", v)
f1()
