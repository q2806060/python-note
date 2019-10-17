# function_as_args.py

def f1():
    print("f1被调用")

def f2():
    print("f2被调用!")

def fx(fn):
    print(fn)  # <function f2 at 0XXXXXXXXX>
    fn()  # f2被调用

fx(f1)
fx(f2)

