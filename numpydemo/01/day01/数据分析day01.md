# 数据分析day01

## 徐铭 xuming@tedu.cn 15201603213

## 什么是数据分析?

数据分析是指用适当的统计分析方法对收集到的大量数据进行分析,提取对于业务有用的信息形成结论并加以详细研究和概括的过程.

**数据分析相关的python常用库**

1. numpy      基础数值运算
2. scipy          科学计算
3. matplotlib       数据可视化
4. pandas     处理序列高级函数

## numpy概述

1. Numerical Python(数值python). 补充了python欠缺的数值运算能力.
2. Numpy是其他数据分析及机器学习的底层库.
3. Numpy完全标准C语言实现, 运行效率高.
4. 开源免费.

### numpy的历史

1. 1995年, 发布Numeric python. 
2. 2001年, Scipy 提供 Numarray. (提供了多维数组)
3. 2005年, Numeric + Numarray -> Numpy.
4. 2006年, Numpy脱离Scipy成为独立的项目.

### numpy的核心:多维数组

```python
import numpy as np
ary = np.array([1, 2, 3, 4])
print(ary)
```

## numpy基础

### ndarray数组

```python
import numpy as np
ary = np.array([1, 2, 3, 4])
print(ary)
```

#### 内存中的ndarray对象

**元数据(metadata)**

存储对目标数组的描述信息,如: 维度 / 元素类型 等等.

**实际数据**

存储完整的数组数据.

将实际数据与元数据分开存放,一方面提高了内存空间的使用效率,另一方面减少对实际数据的访问频率,提高性能.

**ndarray数组对象的特点**

ndarray数组是同质数组, 即所有元素的数据类型必须相同.

#### ndarray数组对象的创建

```python
np.array(任何可被解释为数组的逻辑结构)

np.arange(起始值[0], 终止值, 步长[1])

np.zeros(数组元素个数, dtype='元素类型')

np.ones(数组元素个数, dtype='元素类型') 

np.zeros_like(ary)

np.ones_like(ary)
```

案例:

```python
"""
demo02_ndarray.py
"""
import numpy as np
a = np.array([[1, 2, 3, 4], 
		      [5, 6, 7, 8]])
print(a, a.shape)
# 起始值1, 终止值10, 步长1
b = np.arange(1, 10, 2)
print(b)

# 创建5个元素全为0的数组
c = np.zeros(5, dtype='int32')
print(c, c.dtype)

# 创建5个元素全为1的数组
d = np.ones(5, dtype='int32')
print(d, d.dtype)
# 创建数组e与f, 结构与a相同, e中全0, f中全1
e = np.zeros_like(a)
f = np.ones_like(a)
print(e)
print(f / 5)
```

#### ndarray对象属性的基本操作

**数组的维度:**  ndarray.shape

**元素的类型:**  ndarray.dtype

**数组元素的个数:**  ndarray.size    len(ndarray)

**数组元素的索引(下标):**  ary[0]

```python
"""
demo03_attr.py
"""
import numpy as np

# 测试数组的维度
a = np.arange(1, 10)
print(a, a.shape)
a.shape = (3, 3)
print(a, a.shape)

# 测试元素的类型
print(a.dtype)
b = a.astype(float)
print(b, b.dtype)

b[0][0] = 999
print(b)
print(a)

# 测试元素的个数
print('a.size:', a.size, 'len(a):', len(a))

# 数组元素的索引
c = np.arange(1, 19).reshape(3, 2, 3)
print(c)
print(c[0])
print(c[0][0])
print(c[0][0][0])
print(c[0, 0, 0])

# 遍历c中的每个元素并输出
for i in range(c.shape[0]):
	for j in range(c.shape[1]):
		for k in range(c.shape[2]):
			print(c[i,j,k], end=' ')
```

#### ndarray对象属性操作详解

##### 内部基本数据类型

| 类型名       | 类型表示符                             |
| ------------ | -------------------------------------- |
| 布尔型       | bool_                                  |
| 有符号整数型 | int8(-128~127) / int16 / int32 / int64 |
| 无符号整数型 | uint8 / uint16 / uint32 / uint64       |
| 浮点型       | float16 / float32 / float64            |
| 复数型       | complex64 / complex128                 |
| 字串型       | str_                                   |

**ndarray数组中存储自定义复合类型数据**

```python
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
```

**类型字符码**

| 类型                             | 字符码                         |
| -------------------------------- | ------------------------------ |
| bool_                            | ?                              |
| int8 / int16 / int32 / int64     | i1 / i2 / i4 / i8              |
| uint8 / uint16 / uint32 / uint64 | u1 / u2 / u4 / u8              |
| float16 / float32 / float64      | f2 / f4 / f8                   |
| complex64 / complex128           | c8 / c16                       |
| str_                             | U<字符数> 一个字符占4字节      |
| datetime64                       | M8[Y \| M \| D \| h \| m \| s] |

**ndarray数组对象的维度操作**

**视图变维**(数据共享)  ary.reshape()   ary.ravel()

```python
import numpy as np

a = np.arange(1, 9)
print(a)
# 视图变维
b = a.reshape(2, 4)
print(b)
b[0, 0] = 999
print(b)
c = a.ravel()
print(c)
c[1] = 888
print(c)
print(a)
```

**复制变维**  a.flatten()  a.copy()

```python
print('-' * 45)
d = b.flatten()
print(b)
print(d)
d[2] = 777
print(b)
print(d)

```

**就地变维**  直接改变原数组的维度  a.shape   a.resize()

```python
b.shape = (4, 2)
print(b)
b.resize(2, 2, 2)
print(b)
```

##### ndarray对象的切片操作

```python
# 数组对象的切片与列表切片参数含义相似
# 步长+: 从前向后切
# 步长-: 从后向前切
ary[起始位置:终止位置:步长]
```

```python
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])
print(a[3:6])
print(a[6:])
print(a[::-1])
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[-7::-1])
print(a[:])
print(a[::3])
print(a[1::3])
```

多维数组的切片操作:

```python
# 以,作为分隔符, 分别对 页/行/列 每一维度执行切片
ary[::, ::, ....]
```

##### ndarray数组的掩码操作

```python
"""
demo07_mask.py  ndarray的掩码操作
"""
import numpy as np
a = np.arange(1, 10)
mask = (a%2==0)
print(a)
print(mask)
print(a[mask])
# 使用掩码对数组排序
mask = [8, 1, 2, 7, 3, 4, 6, 5, 0]
print(a[mask])

# 输出100以内3与7的倍数
b = np.arange(100)
print(b[(b%3==0) & (b%7==0)])
```

##### 多维数组的组合与拆分

垂直方向的操作:

```python
# 垂直方向执行组合操作
c = np.vstack((a, b))
print(c, c.shape)
# 垂直方向执行拆分操作
a, b, c, d = np.vsplit(c, 4)
print(a, b, sep='\n')
```

水平方向的操作:

```python
# 水平方向的组合与拆分
d = np.hstack((a, b))
print(d, d.shape)
a, b = np.hsplit(d, 2)
print(a, b, sep='\n')
```

深度方向的操作:

```python
# 深度方向的组合与拆分
e = np.dstack((a, b))
print(e, e.shape)
a, b = np.dsplit(e, 2)
print(a, b, sep='\n')
```

组合与拆分的相关函数:

```python
# 以axis作为轴向,把a与b进行组合操作
# 若a与b都是二维数组:
#  0: 垂直方向组合
#  1: 水平方向组合
# 若a与b都是三维数组:
#  0: 垂直方向组合
#  1: 水平方向组合
#  2: 深度方向组合
c = np.concatenate((a, b), axis=0)
# 以axis作为轴向,把c拆成两部分 a与b
a, b = np.split(c, 2, axis=0)
```

简单一维数组的组合方案:

```python
# 简单一维数组的组合方案
a = a.ravel()
b = b.ravel()
# 把a与b合并成2行
c = np.row_stack((a, b))
# 把a与b合并成2列
d = np.column_stack((a, b))
print(c)
print(d)
```

#### ndarray的其他常用属性

* ndim            维数
* itemsize      元素字节数
* nbytes         数组的总字节数
* real              返回复数数组所有元素的实部
* imag            返回复数数组所有元素的虚部
* T                   返回数组的转置视图
* flat               多维数组的扁平迭代器

```python
"""
demo09_attrs.py  测试常用属性
"""
import numpy as np

data = np.array([[1+1j, 2+4j, 3+7j],
				 [4+2j, 5+5j, 6+8j],
				 [7+3j, 8+6j, 9+9j]])
print(data.dtype)
print(data.ndim)
print(data.itemsize)
print(data.nbytes)
print(data.real)
print(data.imag)
print(data.T)

for item in data.flat:
	print(item, end=' ')
```







































































