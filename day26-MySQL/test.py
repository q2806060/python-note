from my_sql import My_sql

# sqlh = My_sql()
# sqlh.My_inputInfo('update t1 set score=100')

sqlj = My_sql()
score_info = sqlj.My_outputInfo("select * from t1")
for i in score_info:
    print("%s的成绩为：%s" % (i[1], i[2]))


















































