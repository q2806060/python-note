from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import pymysql
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/info"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["DEBUG"] = True

db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

class Province(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(30), nullable=False)
    cities = db.relationship("City", backref="province", lazy="dynamic")
    
    def to_dict(self):
        d = {}
        d["id"] = self.id
        d["province"] = self.province
        return d

class City(db.Model):
    __tablename__ = "cities"
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey("provinces.id"), nullable=False)

    def to_dict(self):
        dic = {
            "id":self.id,
            "city":self.city,
            "province_id":self.province_id
        }
        return dic

@app.route("/")
def hell_world():
    return "Hello World"

@app.route("/01-flight")
def flight_views():
    cb = request.args["callback"]
    dic = {
        "flightNO":"MU763",
        "from":"BJ",
        "to":"SPA",
        "time":"16:55"
    }
    jsonStr = json.dumps(dic)
    return cb+"("+jsonStr+")"

@app.route("/query-province")
def query_province():
    provinces = Province.query.all()
    p = []
    for i in provinces:
        i = i.to_dict()
        p.append(i)
    jsonStr = json.dumps(p)
    return jsonStr

@app.route("/query-city")
def query_city():
    pid = request.args["pid"]
    cities = City.query.filter_by(province_id=pid).all()
    l=[]
    for c in cities:
        l.append(c.to_dict())
    return json.dumps(l)


if __name__ == "__main__":
    manager.run()