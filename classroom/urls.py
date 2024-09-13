from django.urls import path

from .views import *

urlpatterns = [
    path('student/<int:classroom_id>', student, name='index'),
]