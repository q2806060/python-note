# for_range.py

# 观察打印结果
i = 6
for x in range(1, i):  # range(1,6)只执行一次
    print('x=', x, 'i=', i)
    i -= 1

# 结果
# x= 1 i= 6
# x= 2 i= 5
# x= 3 i= 4
# x= 4 i= 3
# x= 5 i= 2
