from django.shortcuts import render

# Create your views here.
def crocks(reqest) :
    return render(reqest,"index.html")
