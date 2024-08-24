from django.shortcuts import render

from .models import info

# Create your views here.
def data(request):

    stu=info.objects.all()

    return render(request,"student/front.html",{"stu":stu})