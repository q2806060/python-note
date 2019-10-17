# 完成mysql 基本功能的封装
import pymysql 


class My_sql:

    def __init__(self, host = 'localhost', user = 'root', password = '123456', database = 'db5', charset = 'utf8', port = 3306):
        self.host = host
        self.user = user 
        self.password = password   
        self.database = database
        self.charset = charset
        self.port = port 

    def My_open(self):
        self.db = pymysql.connect(host=self.host,
                                  user=self.user, 
                                  password=self.password, 
                                  database=self.database, 
                                  charset=self.charset, 
                                  port=self.port)
        self.cur = self.db.cursor()

    def My_close(self):
        self.cur.close()
        self.db.close()


    def My_inputInfo(self, sql, l=[]):
        self.My_open()
        self.cur.execute(sql, l)
        self.db.commit()
        self.My_close()
    
    def My_outputInfo(self, sql, l=[]):
        self.My_open()
        self.cur.execute(sql, l)
        My_tuple = self.cur.fetchall()
        self.My_close()
        return My_tuple



































































