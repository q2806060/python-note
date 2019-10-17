from my_sql import My_sql
from hashlib import sha1

sqlh = My_sql()

username = input('请输入用户名：')

r = sqlh.My_outputInfo('select password from user where name=%s', [username])


if r:
    print('用户已存在！')
    password = input('请输入密码：')
    s = sha1()
    s.update(password.encode('utf-8'))
    password = s.hexdigest()
    if password == r[0][0]:
        print('登录成功！')
    else:
        print('密码错误！')

    
#注册
else:
    print('请注册！')k
    new_passw1 = input('请输入密码：')
    new_passw2 = input('请再次输入密码：')
    if new_passw1 == new_passw2:
        s = sha1()
        s.update(new_passw1.encode('utf-8'))
        new_passw = s.hexdigest()
        ins = 'insert into user values(%s,%s)' 
        sqlh.My_inputInfo(ins, [username, new_passw])
        print('注册成功！')
    else:
        print('两次密码输入不一致！')














































