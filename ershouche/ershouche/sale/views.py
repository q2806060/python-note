from django.shortcuts import render
import random
from .models import UsedCar

# Create your views here.

def index(request):
    car_list = UsedCar.objects.filter(carisbuy=False,carisdel=False)
    # car_list = random.choices(car_list,k=4)
    car_four = random.sample(list(car_list), 4)
    return render(request, 'index.html',locals())