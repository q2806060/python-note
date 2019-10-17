from flask import Flask, render_template

app = Flask(__name__)

@app.route("/calc/<int:num1>/<int:num2>")
def calc(num1, num2):
    s = '%d + %d = %d<br>' % (num1, num2, num1 + num2)
    s += '%d - %d = %d<br>' % (num1, num2, num1 - num2)
    s += '%d * %d = %d<br>' % (num1, num2, num1 * num2)
    s += '%d / %d = %d<br>' % (num1, num2, num1 / num2)

    return s

@app.route("/")
@app.route("/index")
@app.route("/<int:num>")
@app.route("/index/<int:num>")
def index(num=1):
    s = render_template("01-template.html")
    return s

if __name__ == "__main__":
    app.run(debug=True)










