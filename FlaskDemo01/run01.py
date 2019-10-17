from flask import Flask
#将当前运行的主程序构建成Flask应用，以便接收用户的请求，并给出响应
app = Flask(__name__)

#flask中的路由定义，主要去匹配用户的访问路径，"/"表示的是整个网站的根目录
@app.route("/")
#表示的是匹配上访问路径之后的处理程序，视图函数（Views），视图处理函数中必须要有返回值，现阶段必须返回一个字符串，表示要响应给客户端浏览器的内容
def index():
    return "This is my first flask demo."

@app.route("/abc")
def abc():
    return "This is ABC application"

@app.route("/show/<name>/<age>")
def show(name,age):
    return  "姓名为：%s，年龄为：%s" %(name,age)

if __name__ == "__main__":
    app.run(debug=True)









