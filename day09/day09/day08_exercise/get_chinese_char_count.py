#   2. 写一个函数 get_chinese_char_count(s) , 此函数返回
#     一个字符串s中所有中文字符的个数
#         def get_chinese_char_count(s):
#             ...
#         s = input("请输入中英文混合的字符串: ")
#         print("您输入的中文字符的个数是:", 
#             get_chinese_char_count(x))
#     注:
#       中文编码范围是: 0x4E00 ~ 0x9FA5(包含)

def get_chinese_char_count(s):
    count = 0  # 用来记录个数
    for ch in s:
        # 判断ch是否绑定一个中文字符
        if 0x4E00 <= ord(ch) <= 0x9FA5:
            count += 1
    return count

s = input("请输入中英文混合的字符串: ")  # "ABC中文"
print("您输入的中文字符的个数是:", 
    get_chinese_char_count(s))
