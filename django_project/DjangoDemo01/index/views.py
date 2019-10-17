from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is index's index request.")

def login(request):
    return HttpResponse("This is index's login request.")

def register(request):
    return HttpResponse("This is index's register request.")
    