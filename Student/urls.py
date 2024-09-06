from django.urls import path
from .views import *
urlpatterns = [
    # path("home/",data,name="home"),
    path("sighnup/",forms,name="data"),
    path("index/",index,name="index"),
]