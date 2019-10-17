from django.conf.urls import url
import userinfo.views as views

urlpatterns = [
    url(r'register/$', views.register),
    url(r'register_in/$', views.register_),
    url(r'login/$', views.login_views),
    url(r'loginin/$', views.login_),
    url(r'logout/$', views.logout_),
]