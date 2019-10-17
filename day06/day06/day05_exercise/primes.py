#   3. 写一个程序,任意输入一个整数,判断这个数是否是素数
#      (primes)
#      素数也叫质数,是只能被1和自身整除的正整数
#      提示:
#        用排除法:
#           当判断x是否为素数时,只要让x分别与
#             2, 3, 4... x-1  相除,只要能整除,则x不是
#           素数.否则x为素数
  
x = int(input("请输入一个正整数:"))
if x < 2:
    print(x, '不是素数')
else:  # x 大于等同于2时
    flag = True  # 旗子立着，代表成立　
    for i in range(2, x):
        if x % i == 0:
            print(x, '不是素数')
            flag = False  # 旗子放倒
            break
    if flag:
        print(x, '是素数')

 