#当前程序的初始化
#1.创建Flask应用(app)以及各种配置
#2.创建SQLAlchemy的应用实例(db)

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import pymysql

#声明SQLAlchemy的实例
db = SQLAlchemy()

def create_app():
    #创建Flask程序实例 - app
    #为app指定各种配置
    #返回创建好的程序实例app

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/blog"
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True

    #配置session所需要的SECRET_KEY
    app.config["SECRET_KEY"] = "niniubi"

    #关联db以及app
    db.init_app(app)

    #将main蓝图与app关联到一起(让app托管main)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    return app

