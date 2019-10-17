from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.db import DatabaseError
import logging
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    return render(request,'register.html')

def register_(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        cpassword = request.POST.get("cpassword", '')
        if username and password and cpassword:
            olduser  = User.objects.filter(username=username)
            if olduser:
                return render(request,"register.html",{'msg':"该用户已存在"})
            if password != cpassword:
                return  render(request,"register.html",{'msg':"两次密码不一致"})
            newpassword = make_password(password, None, "pbkdf2_sha1")
            try:
                User.objects.create(username=username,password=newpassword)
            except DatabaseError as e:
                logging.warning(e)
            return   render(request, "register.html",{'msg', '注册成功'})
        else:
            return render(request, "register.html", {"msg":"输入项不能为空"})


def login_views(request):
    return render(request,'login.html')

def login_(request):
    if request.method == "POST":
        username = request.POST.get("username",'')
        password = request.POST.get("password", '')
        if username and password:
            # user = User.objects.filter(username=username)

            # if not olduser:
            #     return render(request,'login.html',{'msg':'该用户未注册'})

            user = authenticate(username=username,password=password)

            # else:
                #  check_password(password,)

            if user is not None and user.is_active:
                login(request,user)
                return render(request, "login.html", {'msg':"登陆成功"})
            else:
                return render(request,'login.html',{'msg':"用户名或密码错误"})
        else:
            return render(request,'login.html',{'msg':'请输入登录信息'})

def logout_(request):
    logout(request)
    url = request.META.get("HTTP_REFERER",'/')
    return redirect(url)