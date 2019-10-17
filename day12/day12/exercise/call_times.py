# call_times.py

def make_functions(args):
    count = 0  # 用来记录某个函数的调用次数
    def f1(name):
        print(args, name)
        nonlocal count
        count += 1
    def f2():
        print("调用f1(", args, ")的次数为", count)
        return count

    return (f1, f2)

say_hello, getcount = make_functions("你好:")
print("getcount() 返回:", getcount())  # 0
say_hello("小张")
say_hello("小李")
print("getcount() 返回:", getcount())  # 2

say_goodbye, goodbye_count = make_functions("再见")
print(goodbye_count())  # 0
say_goodbye("Tom")
print(goodbye_count())  # 1
