from flask import Flask, render_template, request, redirect
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import pymysql

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["DEBUG"] = True

db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean, default=True)
    #增加属性：关联属性，针对wife表的一对一关系的关联属性和反向引用关系属性
    wife = db.relationship("Wife", backref="user", uselist=False)
    def __repr__(self):
        return "<User:%r>" %self.username

class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)
    #实现与Teacher的关联关系（多对多，中间借助第三方表进行关联）
    teachers = db.relationship("Teacher", secondary="student_teacher", lazy="dynamic", backref=db.backref("students", lazy="dynamic"))


class Teacher(db.Model):
    __tablename__ = "teacher"
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    #增加关联属性和反向引用关系属性
    teachers = db.relationship("Teacher", backref="course", lazy="dynamic")

class Wife(db.Model):
    __tablename__ = "wife"
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30), nullable=False)
    wage = db.Column(db.Integer)
    #增加外键，引用自 users 表的主键id(一对一)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=True)

#声明一个实体类表示关联Student和Teacher的第三张表
class StudentTeacher(db.Model):
    __tablename__ = "student_teacher"
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))



@app.route("/01-regtea")
def regtea_views():
    # teacher = Teacher()
    # teacher.tname = "Mr Wei"
    # teacher.tage = 40
    # teacher.course_id = 1
    # db.session.add(teacher)

    course = db.session.query(Course).filter(Course.cname=="爬虫").first()
    teacher = Teacher()
    teacher.tname = "Mr Wang"
    teacher.tage = 37
    teacher.course = course
    db.session.add(teacher)
    return "Teacher rigister ok."

@app.route("/02-query")
def query_views():
    # tea = Teacher.query.filter_by(tname="Mr Wang").first()
    # print("Name:%s, Age:%s, Teacher_course:%s" %(tea.tname, tea.tage, tea.course.cname))

    course = Course.query.filter_by(cname="爬虫").first()
    print("课程名称："+course.cname)
    teachers = course.teachers.all()
    return "Query ok."

@app.route("/03-query-exer")
def query_exer():
    courses = Course.query.all()
    if not request.args:
        course_id = 0
    else:
        course_id = int(request.args.get("cid"))
    if course_id == 0:
        teachers = db.session.query(Teacher).all()
    else:
        course = Course.query.filter_by(id=course_id).first()
        teachers = course.teachers.all()
    return render_template("03-query-exer.html", params=locals())

@app.route("/04-oto")
def oto_views():
    # wife = Wife()
    # wife.wname = "王夫人"
    # wife.wage = 18
    # wife.user_id = 1
    # db.session.add(wife)


    #通过反向引用关系属性
    user = Users.query.filter_by(id=2).first()
    wife = Wife()
    wife.wname = "张夫人"
    wife.wage = 16
    wife.user = user
    db.session.add(wife)
    return "Register ok."
    
@app.route("/05-oto-exer", methods=["GET", "POST"])
def oto_exer():
    if request.method == "GET":
        users = Users.query.all()
        return render_template("05-oto-exer.html", params=locals())
    else:
        wname = request.form["wname"]
        wage = request.form["wage"]
        wuser = request.form["user"]
        wife = Wife.query.filter_by(user_id=wuser).first
        if wife:
            errMsg = "user already exist."
            users = Users.query.all()
            return render_template("05-oto-exer.html", params=locals())
        wife = Wife()
        wife.wname = wname
        wife.wage = wage
        wife.user_id = wuser
        db.session.add(wife)
        return "Register ok."
        
@app.route("/06-mtm")
def mtm_views():
    stu = Student()
    stu.sname = "漩涡鸣人"
    stu.sage = 17
    db.session.add(stu)
    db.session.commit()
    #查询出 id 为1 的老师的信息
    tea = Teacher.query.filter_by(id=1).first()
    stu.teachers.append(tea)
    
    return "insert ok."
    
@app.route("/07-mtm-exer", methods=["GET", "POST"])
def mtm_exer():
    if request.method == "GET":
        teachers = Teacher.query.all()
        return render_template("07-mtm-exer.html", params=locals())
    else:
        sname = request.form["sname"]
        sage = request.form["sage"]
        stutea = request.form.getlist("StuTea")
        if not stutea:
            msg = "Please select teacher."
            return render_template("07-mtm-exer.html", params=locals())
        student = Student()
        student.sname = sname
        student.sage = sage
        db.session.add(student)
        db.session.commit()
        for t in stutea:
            teacher = Teacher.query.filter_by(id=t).first()
            student.teachers.append(teacher)
        return "Register ok."

@app.route("/08-mtm-query")
def mtm_query():
    # student = Student.query.filter_by(id=3).first()
    # teachers = student.teachers.all()
    # print(teachers)
    # print(type(teachers))
    # for t in teachers:
    #     print(t.tname)

    teacher = Teacher.query.filter_by(id=1).first()
    students = teacher.students.all()
    for s in students:
        print(s.sname)
    



    return "Query ok." 

if __name__ == "__main__":
    manager.run()