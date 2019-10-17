# star_tuple_args.py

# 此示例示意星号元组的形参的定义和使用


def func(*args):
    '''args一定会绑定一个元组'''
    print("实参个数是:", len(args))
    print("args=", args)

func()  # 元参调用
func(1, 2, 3, 4)
func(1, 2, 3, 4, "ABCD", None, False)

# args 不接收关键字传参
# func(a=100)  # func(*{'a':100})  # 
