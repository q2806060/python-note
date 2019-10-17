from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def login(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "login.html", locals())
    else:
        uphone = request.POST.get("uphone")
        upwd = request.POST.get("upwd")
        users = Users.objects.filter(uphone=uphone)
        if users:
            return HttpResponse("Welcome:"+users[0].uname)
        else:
            return HttpResponse("Login failed.")
        

def index(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html") 

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        uphone = request.POST.get("uphone")
        upwd = request.POST.get("upwd")
        uname = request.POST.get("uname")
        uemail = request.POST.get("uemail")
        users = Users.objects.filter(uphone=uphone)
        if users:
            msg = "用户已存在"
            return render(request, "register.html", locals())
        user = Users()
        user.uphone = uphone
        user.upwd = upwd
        user.uname = uname
        user.uemail = uemail
        user.save()
        return redirect("/")
    

