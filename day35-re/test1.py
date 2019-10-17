import re

s = 'a b a d b a f a b h b a'

lst = re.findall(r'(\w+)\s+(\w+)', s)

print(lst)














