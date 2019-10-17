from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def indexList():
    return render_template("list.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        uname = request.form.get("username")
        pwd = request.form.get("password")
        return "<h1>username:%s<br>password:%s</h1>" %(uname, pwd)

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        email = request.form.get("email")
        url = request.form.get("url")
        return "<h1>username:%s<br>password:%s<br>email:%s<br>url:%s</h1>" %(username, password, email, url)


@app.route("/list_new")
def list_new():
    return render_template("list_new.html")












if __name__ == "__main__":
    app.run(debug=True)

























