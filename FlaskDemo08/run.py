from flask import Flask, make_response, request, render_template, redirect, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "sdjbsdjhabd"


@app.route("/01-setcookie")
def setCookies():
    resp = make_response("add cookie ok.")
    resp.set_cookie("uname", "wangwc", 60*60*24*365)
    return resp

@app.route("/02-getcookie")
def getCookie():
    print(request.cookies)
    return "Get cookie ok."

@app.route("/03-deletecookie")
def deleteCookie():
    resp = make_response("delete cookie ok.")
    resp.delete_cookie("uname")
    
    return resp

@app.route("/login", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html",params=locals())
    else:
        uname = request.form["uname"]
        upwd = request.form["upwd"]
        if uname == "admin" and upwd == "admin":
            if len(request.form) == 2:
                return redirect("/")
            else:
                resp = redirect("/")
                resp.set_cookie("uanme", uname, 60*60*24*365)
                resp.set_cookie("upwd", upwd, 60*60*24*365)
                return resp

@app.route("/")
def umain():
    if "uname" in request.cookies:
        uname = request.cookies("uname")
    return render_template("main_html.html", params=locals())

@app.route("/logout")
def logout():
    url = request.headers.get("Referer", "/")
    #通过url构建响应对象
    resp = redirect(url)
    if "uname" in request.cookies:
        resp.delete_cookie("uname")
        resp.delete_cookie("upwd")
    return resp

@app.route("/01-setsession")
def setSession():
    session["uname"] = "wangwc"
    return "Save session ok."

@app.route("/02-getsession")
def getSession():
    if "uname" in session:
        uname = session["uname"]
        return "Save value:"+uname
    else:
        return "No save data."





if __name__ == "__main__":
    app.run(debug=True)