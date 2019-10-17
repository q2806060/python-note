# mydeco1.py

# 此示例示意装饰器函数的基本原理和作用

def mydeco(fn):
    def fx():
        print("|+++++++++++|")
        fn()
        print('|-----------|')
    return fx


def myfun():
    '''此函数是被装饰函数'''
    print("myfun被调用")

# 以下语句的实质是调用mydeco,绑定mydeco返回的fx函数
myfun = mydeco(myfun)  # 此条语句可以改写为@mydeco,详见mydeco2.py

myfun()
myfun()
myfun()


