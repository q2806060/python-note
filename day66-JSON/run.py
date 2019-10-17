from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/ajax"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

db = SQLAlchemy(app)



class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30), nullable=False)
    upwd = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

db.create_all()

@app.route("/query-all")
def queryAll():
    s = request.args.get("uname", "")
    l = []
    if s != "":
        msg = "%"+s+"%"
        users = db.session.query(Users.uname).filter(Users.uname.like(msg)).all()
        for u in users:
            l.append(u[0])
    jsonStr = json.dumps(l)
    return jsonStr









if __name__ == "__main__":
    app.run(debug=True)
