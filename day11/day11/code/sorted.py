L = [5, -2, -4, 0, 3, 1]

def myabs(x):
    print("x=", x)
    if x < 0:
        return -x
    return x

L6 = sorted(L, key=myabs)
print("L6=", L)