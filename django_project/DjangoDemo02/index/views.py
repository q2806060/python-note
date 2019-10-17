from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def temp(request):
    # t = loader.get_template("01-temp.html")
    # html = t.render()
    # return HttpResponse(html)

    return render(request, "01-temp.html")

def param(request):
    name = "Wangwc"
    age = 98 
    salary = 123.45
    list = ["白眉鹰王", "紫衫龙王"]
    tup = ("赵敏", "周芷若", "小昭")
    dic = {
        "xyj":"西游记",
        "hlm":"红楼梦",
        "shz":"水浒传",
    }
    per = Person()
    per.name = "wangwc"
    per.age = 37 
    return render(request, "03-param.html", locals())

class Person(object):
    name = None
    age = None

    def show(self):
        return "name:%s,age:%d" % (self.name,self.age)

def static(request):
    return render(request, "04-static.html")

def parent(request):
    lst = ["孙悟空", "猪八戒", "沙僧", "唐僧"]
    return render(request, "05-parent.html", locals())

def child(request):
    lst = ["西游记", "三国演义", "红楼梦", "水浒传"]
    return render(request, "06-child.html", locals())

def auth(request):
    return HttpResponse("<h1>url:07-fruit/admin/user/manage/login/</h1>")

def birthday(request, year, month):
    return HttpResponse("<h1>Birthday:%s-%s</h1>" % (year, month))