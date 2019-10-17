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

@app.route("/register", methods=["POST"])
def register_views():
    uname = request.form["uname"]
    upwd = request.form["upwd"]
    uemail = request.form["uemail"]
    print(request.form)
    user = Users()
    user.uname = uname
    user.upwd = upwd
    user.email = uemail
    try:
        db.session.add(user)
        db.session.commit()
        return "register ok."
    except Exception as e:
        print(e)
        return "register fail."





if __name__ == "__main__":
    app.run(debug=True)