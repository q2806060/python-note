"""
demo03_ctype.py 测试自定义复合类型
"""
import numpy as np

data = [
	('zs', [90, 80, 70], 15),
	('ls', [86, 76, 69], 16),
	('ww', [22, 11, 34], 17)]

# 第一种设置dtype属性的方式
# U3:     3个Unicode字符 
# 3int32: 3个int32整数 (列表)
# int32:  1个int32整数
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
# 获取第三个用户的姓名  'f0':第一个字段
print(a[2]['f0'])

# 第二种设置dtype属性的方式
b = np.array(data, dtype=[
				('name',   'str_',  2),
				('scores', 'int32', 3),
				('age',    'int32', 1)])
print(b)
print(b[1]['scores'])

# 第三种设置dtype的方式
c = np.array(data, dtype={
		'names':['name', 'scores', 'age'],
		'formats':['U3', '3int32', 'int32']})
print(c)
print(c[2]['age'])

# 第四种设置dtype的方式
# 0, 16, 28表示数据存储时的字节偏移位置
# 在0字节位置输出name, 16字节位置输出scores..
d = np.array(data, dtype={
		'name': ('U3', 0),
		'scores': ('3int32', 16),
		'age': ('int32', 28)})
print(d)
print(d[2]['age'])

# ndarray数组中存放日期类型数据
f = np.array(['2011', '2012-01-01', 
	'2013-11-11 11:11:11', '2013-01-01'])
print(f)
# datetime64[D]: 描述时间(精确到day)
g = f.astype('M8[D]')
print(g, g.dtype)
print(g[3] - g[1])
print(g.astype('int32'))

print(np.array([0]).astype('M8[s]'))