from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "shdvashdbh"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("01-login.html")
    else:
        uname = request.form["uname"]
        upwd = request.form["upwd"]
        if uname == "admin" and upwd == "admin":
            session["uname"] = uname
            session["upwd"] = upwd
            return "Login ok."
        else:
            return render_template("01-login.html")

@app.route("/")
def index():
    if "uname" in session:
        return "<h2>Welcome:%s</h2>" % session["uname"]
    else:
        return "Please login first."




if __name__ == "__main__":
    app.run(debug=True)