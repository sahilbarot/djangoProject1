from django.urls import path
from .views import *
urlpatterns = [
    path("student/", data, name="student"),
]