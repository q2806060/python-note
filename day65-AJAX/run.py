from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import pymysql

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/ajax"
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
    uname = db.Column(db.String(30), nullable=False)
    upwd = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)



@app.route("/")
def helloworld():
    return "Hello World."

@app.route("/01-server")
def server01():
    return "this is my first AJAX request"

@app.route("/02-server")
def server02():
    uname = request.args.get("uname")
    return "welcome:%s" % uname

@app.route("/04-server", methods=["POST"])
def server04():
    uname = request.form["uname"]
    upwd = request.form["upwd"]
    return "name:%s, password:%s" %(uname, upwd)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        uname = request.args.get("uname")
        ret = Users.query.filter_by(uname=uname).first()
        if ret:
            return "1"
        return "0"
    else:
        user = Users()
        uname = request.form["uname"]
        upwd = request.form["upwd"]
        email = request.form['uemail']
        user.uname = uname
        user.upwd = upwd
        user.email = email
        db.session.add(user)
        
        return "注册成功"

@app.route("/02-query")
def query_views():
    users = Users.query.all()
    ustr = ""
    for u in users:
        ustr += str(u.id)+'-'+str(u.uname)+'-'+str(u.upwd)+'-'+str(u.email)+"|"
    ustr = ustr[:-1]
    return ustr


if __name__ == "__main__":
    manager.run()