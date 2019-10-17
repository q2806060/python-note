from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Avg, Count, F
from .forms import *

# Create your views here.

def add_views(request):
    #方式1：使用Entry.objects.create()
    # dic = {
    #     "name":"爱因斯坦",
    #     "age":200,
    #     "email":"aiyinsitan@163.com",
    # }
    # author = Author(**dic)
    # author.save()

    # book = Book.objects.create(title="神墓",publicate_date="2015-03-20")
    book = Book()
    book.title = "盘龙"
    book.publicate_date = "2014-08-24"
    book.save()
    # dic = {
    #     "title":"遮天",
    #     "publicate_date":"2016-09-30",
    # }
    # book = Book(**dic)
    # book.save()

    # publisher = Publisher.objects.create(name="人民出版社",address="北京一环",city="北京",country="中国",website="www.renmin.com")
    # publisher = Publisher()
    # publisher.name = "新华出版社"
    # publisher.address = "上海陆家嘴"
    # publisher.city = "上海"
    # publisher.country = "中国"
    # publisher.website = "www.xinhua.com"
    # publisher.save()
    # dic = {
    #     "name":"安徽出版社",
    #     "address":"安徽合肥",
    #     "city":"安徽",
    #     "country":"中国",
    #     "website":"www.anhui.com",
    # }
    # publisher = Publisher(**dic)
    # publisher.save()
    return HttpResponse("Create Success.")

def query_views(request):
    authors = Author.objects.all()
    # print(authors)
    # print(type(authors))
    for au in authors:
        print("ID:%s,Name:%s,Age:%d,Email:%s" % (au.id, au.name, au.age, au.email))

    authors = Author.objects.values("name", "email")
    for au in authors:
        print(au)
    return HttpResponse("Query ok.")

def query_filter(request):
    # ret1 = Author.objects.filter(id=1)
    # ret2 = Author.objects.filter(id=1, isActive=True)
    # for i in ret1:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # for i in ret2:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # authors1 = Author.objects.filter(age__gte=80).aggregate(avgAge=Avg("age"))
    # authors2 = Author.objects.filter(name__startswith="巴")
    # authors3 = Author.objects.filter(email__contains="in")
    # authors4 = Author.objects.filter(age__gt=authors2[0].age)
    # for i in authors1:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # for i in authors2:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # for i in authors3:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # for i in authors4:
    #     print("ID:%d,Name:%s,Age:%d,Email:%s" % (i.id, i.name, i.age, i.email))
    # print(authors1)
    books = Book.objects.aggregate(countBook=Count("*"))
    books2 = Book.objects.values("publicate_date").annotate(count=Count("*")).values("publicate_date","count")
    book3 = Book.objects.filter(publicate_date__year__gt=1986).aggregate(count=Count("*"))
    publishers = Publisher.objects.filter(city="北京").aggregate(countCity=Count("id"))
    print(books)
    print(books2)
    print(book3)
    print(publishers)
    return HttpResponse("Query ok.")

def update_views(request):
    # au = Author.objects.get(name="老舍")
    # au.email = "laoshe@sina.com"
    # au.save()
    # Author.objects.filter(isActive=False).update(isActive=True)
    Author.objects.all().update(age=F("age")+10)
    
    return HttpResponse("Update ok.")

def query_author(request):
    authors = Author.objects.filter(isActive=True)
    return render(request, "query-author.html", locals())

def delete_views(request, id):
    author = Author.objects.get(id=id)
    author.isActive = False
    author.save()
    return redirect("/05-query-author")

def oto_views(request):
    # wife = Wife.objects.get(name="舒夫人")
    # print(wife.author.name)
    # author = Author.objects.get(name="老舍")
    # print(author.wife.name)
    book = Book.objects.get(title="遮天")
    # print(book.publisher.name)
    # publisher = Publisher.objects.get(name="人民出版社")
    # books = publisher.book_set.all()
    # for book in books:
    #     print(book.title)
    authors = book.authors.all()
    for au in authors:
        print(au.name)
    author = Author.objects.get(name="爱因斯坦")
    books = author.book_set.all()
    for book in books:
        print(book.title)
    return HttpResponse("Query ok.")

def request_views(request):
    print(request.scheme)
    print(request.body)
    print(request.path)
    print(request.get_full_path)
    print(request.get_host())
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.COOKIES)
    print(request.META)
    
    return HttpResponse("Query ok.")

def get_views(request):
    pname = request.GET.get("pname", "")
    return HttpResponse("您搜索的产品名称为："+pname)


def post_views(request):
    #判断请求方法
    if request.method == "GET":
        return render(request,"12-post.html")
    else:
        uname = request.POST.get("uname", "")
        return HttpResponse("name:"+uname)

def form_views(request):
    form = RemarkForm()
    return render(request,"13-form.html",locals())

def form_register(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "13-register.html", locals())
    else:
        # 标准取值
        # uname = request.POST.get("uname")
        # uage = request.POST.get("uage")
        # upwd = request.POST.get("upwd")
        # uemail = request.POST.get("uemail")
        # print(uname)
        # print(uage)
        # print(upwd)
        # print(uemail)
        # return HttpResponse("recv ok.")
        
        # 通过 form 取值
        #1.将 request.POST 提交给 RegisterForm
        form = RegisterForm(request.POST)
        #2.验证数据是否通过所有的验证
        if form.is_valid():
            #3.通过验证后取值
            cd = form.cleaned_data
            print(cd)
        return HttpResponse("get success.")

def modelform_views(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, "15-modelform.html", locals())
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Author(**cd).save()
            return HttpResponse("register ok.")
        return HttpResponse("data error.")

def widgetform_views(request):
    # form = WidgetForm()
    form = WidgetModelForm()
    return render(request, "16-widgetform.html", locals())

def setcookie(request):
    resp = HttpResponse("save cookie ok.")
    resp.set_cookie("uphone","13988888888",60*60*24*365*10)
    resp.set_cookie("upwd","123456",60*60*24*365*10)
    return resp

def getcookie(request):
    uphone = request.COOKIES.get("uphone", "none")
    upwd = request.COOKIES.get("upwd", "none")
    return HttpResponse("uphone:"+uphone+"upwd:"+upwd)

def setsession(request):
    request.session["uphone"] = "13988888888"
    return HttpResponse("添加session成功")

def getsession(request):
    uphone = request.session["uphone"]
    return HttpResponse("uphone:"+uphone)