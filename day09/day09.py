 a = s[:4]  # 'ABCD'
    a = s[:]  # 'ABCDE'  等同于a=s[0:5]
    a = s[1:1]  # ''   空字符串
    a = s[0::2]  # 'ACE'
    a = s[::2]  # 等同于a = s[0:5:2]
    a = s[4:0:-1]  # 'EDCB'
    a = s[3:0:-2]  # 'DB'
    a = s[4::-2]   # 'ECA'
    a = s[::-2]   # 'ECA'
 
python 运算符的优先级
  文档参见:
    python_base_docs_html/运算符优先级.html

python3 中常用的序列函数:
  len(x)     返回容器中数据的个数(长度)
  max(x)     返回容器中的最大值元素
  min(x)     返回容器中的最小值元素
  示例:
    s = "ABCD1234"
    print(len(s))  # 8
    print(max(s))  # D
    print(min(s))  # 1

字符串编码转换函数:
   ord(c)   返回一个字符串的Unicode编码值
   chr(i)   返回整数i这个值所对应的字符
   示例:
     print(ord('A'))  # 65
     print(ord('中'))  # 20013

整数转换为字符串函数
  bin(i)   将整数转为二进制字符串
  oct(i)   将整数转为八进制字符串
  hex(i)   将整数转为十六进制字符串
  示例: x = 1234
       print(bin(x))
       print(oct(x))
       print(hex(x))

字符串的构造(创建)函数 str
  str(obj='')  将对象转换为字符串
  示例:
    a = str(100)  # a = '100'
    a = str(3.14)  # a = '3.14'
    a = str(None)  # a = 'None'

查看函数的帮助:
    >>> help(函数名)
    >>> help(类型名)
    >>> help(对象)

python3中 常用的字符串方法(method)
  语法:对象.方法名(方法传参)
  示例:
    'abc'.isalpha()  # 语法是对的
    123.isalpha()   # 错的
  文档参见:
    python_base_docs_html/str.html





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      