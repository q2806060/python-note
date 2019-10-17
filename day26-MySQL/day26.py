#1

# import pymysql

# #1.创建数据库连接
# db = pymysql.connect('localhost', 'root', '123456', 'db5', charset='utf8')

# #2.创建游标对象
# cur = db.cursor()

# #3.利用游标对象的方法执行sql命令
# cur.execute('insert into t1 values(4,"王维",78)')

# #4.提交到数据库（commit；）
# db.commit()

# #5.关闭游标对象
# cur.close()

# #6.关闭数据库连接
# db.close()

# print('保存成功！')


#2

# import pymysql

# db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', database = 'db5', charset = 'utf8')
# cur = db.cursor()
# ins = 'insert into t1 values(1,"李白",95),(2,"杜甫",90),(3,"李清照",85)'
# # slet = 'select * from t1'
# try:
#     cur.execute(ins)
#     db.commit()

# except Exception as err:
#     db.rollback()
#     print(err)
#     print('操作失败！')
# cur.close()
# db.close()



#3 

import pymysql

db = pymysql.connect(host = 'localhost', user = 'root', password = '123456', database = 'db5', charset = 'utf8', port = 3306)

cur = db.cursor()

sel = 'select * from t1'
cur.execute(sel)
s = cur.fetchall()
print(s)
print(s[2][2])
cur.close()
db.close()





















































