from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
#导入pymysql用来替代MySQLdb
import pymysql

# pymysql.install_as_MySQLdb()


app = Flask(__name__)
#为app指定连库字符
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:123456@localhost:3306/flask"
#取消SQLAlchemy的信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#创建SQLAlchemy程序实例
db = SQLAlchemy(app)










if __name__ == "__main__":
    app.run(debug=True)





