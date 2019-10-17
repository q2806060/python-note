# mydeco2.py

# 此示例示意装饰器函数的基本原理和作用

def mydeco(fn):
    def fx():
        print("|+++++++++++|")
        fn()
        print('|-----------|')
    return fx

@mydeco
def myfun():
    '''此函数是被装饰函数'''
    print("myfun被调用")

myfun()
myfun()
myfun()


