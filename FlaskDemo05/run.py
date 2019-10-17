from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func
import math

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

#设置程序的启动模式为调试模式
app.config["DEBUG"] = True

db = SQLAlchemy(app)

#创建Manager对象并制定要管理哪个应用(app)
manager = Manager(app)
#创建Migrate对象，并指定关联的app和db
migrate = Migrate(app, db)
#为manager增加命令，允许做数据库的迁移操作
#为manager绑定一个叫db的子命令，该子命令执行操作由MigrateCommand来提供
manager.add_command("db", MigrateCommand)


#创建实体类 - Users，映射到数据库中叫users表
#创建字段id，主键，自增
#创建字段username，长度为80的字符串，不允许为空，值唯一，加索引
#创建字段age，整数，允许为空
#创建字段email，长度为120的字符串，必须唯一
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    #增加字段 isActive，表示用户是否被激活，布尔类型，默认为True
    isActive = db.Column(db.Boolean, default=True)
    def __repr__(self):
        return "<User:%r>" %self.username



class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)

class Wife(db.Model):
    __tablename__ = "wife"
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30), nullable=False)
    wage = db.Column(db.Integer)


#db.drop_all():删表，跑路
# db.drop_all()

#db.create_all():将创建好的实体映射回数据库，生成表
# db.create_all()






@app.route('/')
def hello_world():
    return "hello world."

@app.route("/01-add")
def add_views():
    #1.创建Users的对象，并为各个属性赋值
    #2.将Users的对象通过db.session.add()保存回DB
    #3.手动提交操作回数据库
    user = Users()
    user.username = "wangwc"
    user.age = 37
    user.email = "wangwc@163.com"
    db.session.add(user)
    # db.session.commit()
    return "<h1>update ok.</h1>"

@app.route("/02-query")
def query_views():
    query = db.session.query(Users.id, Users.username, Users.age)
    print(query)
    print(type(query))
    return "query ok."

@app.route("/03-query")
def query03_views():
    query = db.session.query(Users).all()
    for u in query:
        print("姓名：%s，年龄：%s，邮箱：%s" %(u.username, u.age, u.email))
    # print(query[0])
    # print(type(query[0]))
    # print(type(query))
    return "query ok."

@app.route("/04-register", methods=["GET", "POST"])
def register_views():
    if request.method == "GET":
        return render_template("04-register.html")
    else:
        username = request.form["username"]
        age = request.form["age"]
        email = request.form["email"]
        user = Users()
        user.username = username
        user.age = age
        user.email = email 
        db.session.add(user)
        # return "<a href="">review all</a>"
        #通过重定向跳转到/05-queryall
        return redirect("/05-queryall")

@app.route("/05-queryall")
def queryall_views():
    queryall_view = db.session.query(Users).filter(Users.isActive==True).all()
    return render_template("05-queryall.html", params=locals())

@app.route("/06-filter")
def filter_views():
    # ret = db.session.query(Users).filter(or_(Users.age>17,Users.age>1)).all()
    # for u in ret:
    #     print("ID:%s,NAME:%s,AGE:%s" %(u.id, u.username, u.age))
    # rst = db.session.query(Users).filter(Users.username.like(r"%a%")).all()
    # for i in rst:
    #     print("ID:%s,NAME:%s,AGE:%s" %(i.id, i.username, i.age))
    # rst1 = db.session.query(Users).filter(Users.username.like(r"a%")).first()
    # print("ID:%s,NAME:%s,AGE:%s" %(rst1.id, rst1.username, rst1.age))
    # rst2 = db.session.query(Users).filter(Users.age.in_(["24","25","37"])).all()
    # for m in rst2:
    #     print("ID:%s,NAME:%s,AGE:%s" %(m.id, m.username, m.age))
    rst3 = db.session.query(Users).filter(Users.age.between(30,45)).all()
    for n in rst3:
        print("ID:%s,NAME:%s,AGE:%s" %(n.id, n.username, n.age))
    return "query ok."

@app.route("/07-filter-exer")
def filter_exer():
    data = request.args.get("msg", "")
    if data:
        users = db.session.query(Users).filter(or_(Users.username.like("%"+data+"%"), Users.email.like("%"+data+"%"))).all()
    else:
        users = db.session.query(Users).all()
    return render_template("07-filter.html", params=locals())

@app.route("/08-exer")
def exer_views():
    users = db.session.query(Users).filter_by(isActive=True).all()
    for u in users:
        print(u)
    return "<h1>query ok.</h1>"

#通过 offset() 和 limit() 实现分页查询
@app.route("/09-page")
def page_views():
    #变量 - pageSize，表示每页显示的记录数
    pageSize = 2
    #接收前端传递过来的请求参数 - page，如果没有设置为1，保存在变量 page 中
    page = int(request.args.get("page", 1))
    #查询第page页的数据
    users = db.session.query(Users).offset(pageSize*(page-1)).limit(pageSize).all()
    totalCount = db.session.query(Users).count()
    lastPage = math.ceil(totalCount / pageSize)
    prevPage = 1
    if page > 1:
        prevPage = page -1
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1
    return render_template("09-page.html", params=locals())

@app.route("/10-aggregate")
def aggregate_views():
    # res = db.session.query(func.avg(Users.age)).all()
    # print(res)
    # print("平局年龄是：%f" % res[0])
    ret = db.session.query(func.avg(Users.age), func.sum(Users.age), func.max(Users.age), func.min(Users.age)).all()
    print(ret)
    return "Query ok."

@app.route("/13-delete")
def delete_views():
    id = request.args.get("id")
    user = db.session.query(Users).filter(Users.id==id).first()
    user.isActive = False
    db.session.add(user)
    return redirect("/05-queryall")



if __name__ == "__main__":
    #通过manager管理对象启动服务
    #通过python run.py runserver 启动
    #无法制定调试模式(debug=True) ---> app.config["DEBUG"] = True
    #无法指定启动端口(port=5555) ---> python run.py runserver --port 5555
    #无法制动主机地址(host=0.0.0.0) ---> python run.py runserver --host 0.0.0.0
    #合体 ---> python run.py --host 0.0.0.0 --port 5555
    manager.run()























