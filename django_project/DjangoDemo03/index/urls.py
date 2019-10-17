from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^01-add/$", views.add_views),
    url(r"^02-query/$", views.query_views),
    url(r"^03-query-filter/$", views.query_filter),
    url(r"^04-update/$", views.update_views),
    url(r"^05-query-author/$", views.query_author),
    url(r"^06-delete/(\d+)/$", views.delete_views),
]
urlpatterns += [
    url(r"^07-oto/$", views.oto_views),
]
urlpatterns += [
    url(r"^10-request/$", views.request_views),
    url(r"^11-get/$", views.get_views),
    url(r"^12-post/$", views.post_views),
]
urlpatterns += [
    url(r"^13-form/$", views.form_views),
    url(r"^13-register/$", views.form_register),
    url(r"^15-modelform/$", views.modelform_views),
    url(r"^16-widgetform/$", views.widgetform_views),
]
urlpatterns += [
    url(r"^17-setcookie/$", views.setcookie),
    url(r"^18-getcookie/$", views.getcookie),
    url(r"^19-setsession/$", views.setsession),
    url(r"^20-getsession/$", views.getsession),
]
