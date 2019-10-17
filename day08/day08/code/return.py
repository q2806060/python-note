# return.py

def say_hello():
    print("hello aaa")
    print("hello bbb")
    return [1, 2, 3]
    print("hello ccc")

v = say_hello()
print('v=', v)  # None

v2 = say_hello()
print('v2=', v)
print(id(v))
print(id(v2))
print(v is v2)
