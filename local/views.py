from django.shortcuts import render
from .forms import Formname

# Create your views here.
def crocks(request) :
    return render(request, "crocks/index.html")

def forms(request) :
    # if request.method == "POST" :
    data = Formname()

    if request.method == "POST" :
        data = Formname(request.POST)

        if data.is_valid() :
            print("Success")
            print("name :"+data.cleaned_data["name"])
            print("email :"+data.cleaned_data["email"])
            print("phone number :"+data.cleaned_data["phone"])

    return render(request, "crocks/basic_form.html",{"data":data})