from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/01-parent")
def parent():
    return render_template("01-parent.html")

@app.route("/02-child")
def child():
    return render_template("02-child.html")

@app.route("/03-request")
def request_views():
    # print(dir(request))
    #获取请求的各种参数
    scheme = request.scheme
    method = request.method
    args = request.args
    form = request.form
    cookies = request.cookies
    files = request.files
    path = request.path
    full_path = request.full_path
    url = request.url
    headers = request.headers
    referer = request.headers.get("Referer", "/")
    return render_template("03-request.html", params=locals())

@app.route("/04-referer")
def index_referer():
    return "<a href='03-request'>去往03-request</a>"

@app.route("/")
def index():
    return "<h1>这是首页</h1>"

@app.route("/05-get")
def get_views():
    name = request.args["name"]
    age = request.args["age"]
    return "<h1>提交的数据：name:%s,age:%s</h1>" %(name, age)




if __name__ == "__main__":
    app.run(debug=True)























