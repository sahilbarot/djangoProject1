from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request,"cource/photos.html")
def action(request):
    return render(request,"cource/action.html")
def dramatic(request):
    return render(request,"cource/dramatic.html")
def friction(request):
    return render(request,"cource/friction.html")