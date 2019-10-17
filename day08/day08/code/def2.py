# def2.py

# 写一个函数,此函数可以接收调用时传入两个实参
# 此函数会将最大的一个数打印出来

def mymax(a, b):
    print("a =", a)
    print("b =", b)
    if a > b:
        print(a, "最大")
    else:
        print(b, "最大")


mymax(100, 200)
mymax("ABC", "123")

