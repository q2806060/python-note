from django.conf.urls import url 
from . import views 

urlpatterns = [
    url(r"^show01/$", views.show01),
    url(r"^$", views.index),
]