from django.urls import path
from .views import *
urlpatterns = [
    path('',crocks,name="crocks"),
    path('forms/',forms,name="form")
]