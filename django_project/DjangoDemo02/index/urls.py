from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^01-temp/$", views.temp),
    url(r"^03-param/$", views.param),
    url(r"^04-static/$", views.static),
    url(r"^05-parent/$", views.parent),
    url(r"^06-child/$", views.child),
    url(r"^07-fruit/admin/user/manage/login/$", views.auth, name="auth"),
    url(r"^08-birthday/(\d{4})/(\d{2})/$", views.birthday, name="birth"),
]
