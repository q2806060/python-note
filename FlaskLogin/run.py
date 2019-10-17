from flask import Flask, render_template, request, session, redirect, make_response

app = Flask(__name__)

app.config["SECRET_KEY"] = "shdvashdbh"

@app.route("/login", methods=["GET", "POST"])
def login_views():
    if request.method == "GET":
        url = request.headers.get("Referer", "/")
        session["url"] = url
        #判断session有没有uname的值
        if "uname" in session:
            return redirect(url)
        else:
            if "uname" in request.cookies:
                uname = request.cookies["uname"]
                if uname == "admin":
                    session["uname"] = uname
                    return redirect(url)
                else:
                    resp = make_response(render_template("login.html"))
                    resp.delete_cookie("uname")
                    return resp
            else:
                return render_template("login.html")
        
    else:
        uname = request.form["uname"]
        upwd = request.form["upwd"]
        if uname == "admin" and upwd == "admin":
            session["uname"] = uname
            url = session["url"]
            resp = redirect(url)
            if "isSaved" in request.form:
                resp.set_cookie("uname", uname, 60*60*24*365*10)
            return resp
        else:
            return render_template("login.html")

@app.route("/")
def index():
    return "Hello World."


if __name__ == "__main__":
    app.run(debug=True)