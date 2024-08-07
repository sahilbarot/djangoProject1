from django.shortcuts import render

# Create your views here.

def shope(request) :
    return render(request, "files/shope.html")
def oppo(request) :
    return render(request, "files/oppo.html")

def vivo(request) :
    return render(request, "files/vivo.html")
