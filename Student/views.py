from django.shortcuts import render

# from .models import info
from .forms import newform
# Create your views here.
def index(request):
    return render(request,"student/sighnup.html")
# def data(request):

    # stu=info.objects.all()

    # return render(request,"student/front.html",{"stu ":stu})

def forms(request):
    container=newform()

    if request.method=="POST":
        form=newform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request, "student/forform.html",{"form":container})