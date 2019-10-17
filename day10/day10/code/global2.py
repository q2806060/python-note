# global.py

# 此示例示意global语句的用法

v = 100

def f1():
    v = 200
    global v
    # v = 300

f1()
print(v)  # 100

