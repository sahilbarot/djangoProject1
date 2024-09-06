from django.urls import path
from .views  import *
urlpatterns = [
    # path('', index, name='index'),
    path("",home,name="home"),
    path("friction/",friction,name="friction"),
    path("dramatic/",dramatic,name="dramatic"),
    path("action/",action,name="action"),
]