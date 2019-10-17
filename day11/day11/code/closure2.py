# closure2.py


def get_fx(a, b, c):
    def fx(x):
        return a*x**2 + b*x + c
    return fx

f234 = get_fx(2, 3, 4)
print(type(f234))
print("f234(10)=", f234(10))
print("f234(20)=", f234(20))

f567 = get_fx(5, 6, 7)
print("f567(30)=", f567(30))
print("f567(50)=", f567(50))
