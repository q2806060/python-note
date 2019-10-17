import re 

# regex = re.compile(r'\s+')

# ret = regex.sub(r"***", 'hello wprld hello terena', 4)

# print(ret)


ret = re.search(r'(\w+)\s+(\w+)', 'a b c d')
print(ret)
print(ret.group())


ret = re.match(r'(\w+)\s+(\w+)', 'a b c d')
print(ret)
print(ret.group())


ret = re.findall(r'(\w+)\s+(\w+)', 'a b c d')
print(ret)






























