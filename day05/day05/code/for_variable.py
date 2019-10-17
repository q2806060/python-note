
# 此示例示意x变量将不会被创建 

for x in range(4, 0):
    print(x)
else:
    print('else子句中的x=', x)

print("循环结束后的x的值是", x)  # 出错,x变量不存在

