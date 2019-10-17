# global.py

# 此示例示意global语句的用法

v = 100

def f1(v):  # <<<-- 这里有个v
    global v  # 此种做法错误
    v = 300

f1(200)
print(v)  # 100

