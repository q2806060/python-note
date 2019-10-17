# mydeco3.py

# 假设银行系统有的业务为,存钱和取钱

# 以下是小钱同学写的装饰器函数
def privileged_check(fn):
    def fx(n, x):
        print("正在进行权限验证....")
        fn(n, x)
    return fx

def message_send(fn):
    def fy(n, x):
        fn(n, x)
        print("正在发送短信给:", n)
    return fy

# ------以下是魏老师写的程序-----------
@privileged_check
def savemoney(name, x):
    print(name, '存钱', x, '元')

@message_send
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

# -------- 以下是调用小张写的程序------
savemoney("小王", 200)
savemoney("小赵", 400)

withdraw("小李", 500)


