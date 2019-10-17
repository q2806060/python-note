# return_function.py


def get_function():
    s = input("请输入您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 8, 6, 4, 0]
fn = get_function()
print(fn(L))

