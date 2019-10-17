#处理与用户业务逻辑相关的视图和路由
from . import users
from .. import db
from flask import render_template, request, redirect, session
from ..models import *
import os
import datetime


@users.route("/login", methods=["GET","POST"])
def users_login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        #接收数据，查询数据库，验证用户名密码，根据结果保存进session
        loginname = request.form["username"]
        upwd = request.form["password"]
        user = User.query.filter_by(loginname=loginname,upwd=upwd).first()
        if user:
            #登录成功，保存进session，并跳转至首页
            #将id和loginname同时保存进session
            session["id"] = user.ID
            session["loginname"] = loginname
            return redirect("/")
        else:
            #登录失败，返回至首页
            return redirect("/login")


