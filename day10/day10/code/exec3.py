

s = '''
x = 10000
y = 20000
z = x + y
print(x, "+", y, "=", z)
'''

global_dict = {}
exec(s, global_dict)
# print("global_dict=", global_dict)
for key in global_dict:
    print(key)


# exec(s)
# print(x, y, z)
