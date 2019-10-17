#   1. 用字符串"ABC" 和 "123" 生成如下列表:
#   ['A1', 'A2', 'A3',
#    'B1', 'B2', 'B3',
#    'C1', 'C2', 'C3']

L = [x + y for x in "ABC" for y in "123"]
print(L)

