from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show01(request):
    return HttpResponse("This is music's show01 request.")

def index(request):
    return HttpResponse("This is music's index request.")