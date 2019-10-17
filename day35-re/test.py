
# s = '21546564@qq.com 465484@163.com 65464984@qq.com'

# # l = s.split()

# # for i in l:
# #     if 'qq' in i:
# #         print(i)

# import re

# lst = re.findall('\d+@qq.com', s)

# print(lst)


# import re 

# s = 'hello 12899999999 Insdi iajidanuf  nund ndsnusdn undai19999999999'

# rlist = re.findall('\d{11}', s)

#  prin(rlist)


# import re

# with open('/etc/passwd', 'r') as f:
#     rlists = f.readlines()
#     count = 0
#     for rlist in rlists:
#         ret = re.findall('/user/sbin/nologin$', rlist)
#         if ret:
#             count += 1
#     print(count)
        


# import re 

# s = 'd2ad543145192.168.163.156 jhgada558da5265.575.55.754 kjnhj564khbjh564.354.5.1 211.889.1.5'

# rlist = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s)
# for i in rlist:
#     print(i)


# import re 

# s = "256456@qq.comawnahu@126.comekwii@163.commifnisi@tedu.cn"

# rlist = re.findall('\w+@\w+\.com|\w+@\w+\.cn', s)

# print(rlist)



import re 

s = """
<div class="动物">
  <p class="名字">
    <a title="兔子"></a>
  </p>
  <p class="描述">
    小白兔,白又白,两只耳朵竖起来
  </p>
</div>
<div class="动物">
  <p class="名字">
    <a title="老虎"></a>
  </p>
  <p class="描述">
    两只老虎两只老虎跑的快跑的快
  </p>
</div>
"""

rlist = re.findall(r'<a title="(.*?)"></a>[\s\S]*?<p class="描述">\n    (.*?)\n  </p>', s)

print(rlist)






















