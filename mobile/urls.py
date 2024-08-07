from django.urls import path
from .views import *

urlpatterns = [
    path("shope/",shope,name="files-shope"),
    path("oppo/",oppo,name="files-oppo"),
    path("vivo/",vivo,name="files-vivo"),

]