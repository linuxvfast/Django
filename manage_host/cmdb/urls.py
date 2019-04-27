from django.conf.urls import url
from cmdb import views

urlpatterns = [
    url('add', views.add_info), #为表添加信息
    url(r'^business$', views.business),
    url(r'^host$', views.hosts),
]