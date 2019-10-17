#处理与博客相关的路由和视图
from . import main
from flask import render_template, request, session, redirect
from ..models import *
from .. import db
import os, datetime

@main.route("/")
def main_index():
    #查询Category中的所有分类信息
    categories = Category.query.all()
    topics = db.session.query(Topic).limit(20).all()
    #判断session中是否有id 和loginname的值
    if "id" in session and "loginname" in session:
        id = session["id"]
        user = User.query.filter_by(ID=id).first()
    return render_template("index.html", params=locals())

@main.route("/release", methods=["GET", "POST"])
def release_views():
    if request.method == "GET":
        #权限验证，没权限，从哪来回哪去
        if "id" in session and "loginname" in session:
            userid = session["id"]
            user = User.query.filter_by(ID=userid).first()
            if user.is_author:
                categorys = Category.query.all()
                return render_template("release.html", params=locals())
        url = request.headers.get("Referer", "/")
        return redirect(url)
    else:
        topic = Topic()
        if request.files:
            image = request.files["image"]
            now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            new_name = now_time + image.filename
            basedir = os.path.dirname(os.path.dirname(__file__))
            name = os.path.join(basedir,"static/upload",new_name)
            image.save(name)
            topic.images = "upload/"+new_name
        topic.title = request.form["author"]
        topic.topictype_id = request.form["list"]
        topic.category_id = request.form["category"]
        topic.user_id = session["id"]
        topic.content = request.form["content"]
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(topic)
        return redirect("/")