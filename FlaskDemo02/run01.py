from flask import Flask, render_template

app = Flask(__name__)

#目的：实现变量在模板中的显示问题
@app.route("/01-var")
def var_views():
    return render_template("01-var.html", name="wangwc", age=37, song="<<绿光>>", writer="宝强", song_owner="羽凡", singer="乃亮")

#允许放在模板中作为变量的数据类型
@app.route("/02-var")
def var02():
    name = "wangwc"
    age = 37
    tup = ("抽烟", "喝酒", "保健")
    lst = ["赵丽颖", "赵萌萌", "葛老师"]
    dic = {
        "WFR" : "王夫人",
        "LXC" : "李小超",
        "LEG" : "李二狗",
    }
    person = Person()
    person.name = "王伟超老师"
    # params = {
    #     'name' : name,
    #     'age' : age,
    #     'tup' : tup,
    #     'lst' : lst,
    #     'dic' : dic,
    #     'person' : person,
    # }

    # params = locals()

    return render_template("02-var.html", params=locals())


@app.route("/03-if")
def if_views():
    name = "wanglaoshi"
    age = 63
    return render_template("03-if.html", params=locals())


@app.route("/04-for")
def for_views():
    lst = ['嫦娥','百里守约','鲁班七号','王昭君']
    dic = {
        'SWK' : "孙悟空",
        'PJL' : '潘金莲',
        'GY' : "关羽",
        'LLL' : "刘姥姥",
    }
    return render_template("04-for.html", params=locals())

@app.route("/05-macro")
def macro_views():
    lst = ['嫦娥','百里守约','鲁班七号','王昭君']
    return render_template("05-macro.html", params=locals())


@app.route("/06-static")
def static_views():
    return render_template("06-static.html")



class Person(object):
    name = None
    def say(self):
        return "Hello, my name is " + self.name



if __name__ == ("__main__"):
    app.run(debug=True)


















