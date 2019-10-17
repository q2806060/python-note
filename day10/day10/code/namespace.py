# namespace.py


# 此示例示意python的作用域
v = 100
def f1():
    v = 200
    print("f1.v=", v)
    def f2():
        v=300
        print("f2.v=", v)
    f2()
f1()
print('v=', v)