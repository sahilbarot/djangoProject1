from django.shortcuts import render,redirect

names = ["parth", "vansh","sarthak"]
# Create your views here.
def home(request):
    return render(request,"emp_temp/home_page.html",{"names":names})
def information(request):
    if request.method == "POST":
        name = request.POST["name1"]
        print(name)
        names.append(name)
        return redirect("home-page")
    else:
        return render(request,"emp_temp/information.html")