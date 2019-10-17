#   3. 输入Unicode的起始值用变量 begin绑定
#      输入终止值用变量end绑定
#        打印这些字符所应用的文字,结果如下:
#     如:
#       请输入起始值: 48
#       请输入终止值: 57
#     打印如下:
#       十进制编码    十六进制编码  文字
#         48           0x30      0
#         49           0x31      1
#         50           0x32      2
#         ....

begin = int(input("请输入Unicode的起始值: "))
end = int(input("请输入Unicode的终止值: "))
print('十进制编码    十六进制编码   文字')
while begin <= end:
    dec = "%d" % begin
    hexi = "0x%x" % begin
    text = "%c" % begin
    print("%s    %s   %s" % (
        dec.center(10),
        hexi.center(12),
        text.center(4)
    ))
    begin += 1
