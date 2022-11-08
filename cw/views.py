from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(req):
    pages = Page.objects
    if "action" in req.GET:
        action = req.GET.get("action")
        if action == "search":
            query = req.GET.get("value")
            pages = pages.filter(head__icontains=query)
        else:
            print("Recieved GET request with no 'action' param")
    return render(req, "cw/home.html", {"pages":pages})

def about(req):
    return render(req, "cw/about.html", {})

def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("..")
    else:
        form = RegisterForm()
    return render(req, "cw/register.html", {"form":form})

# def login(req):
#     if req.method == "POST":
#         form = Login(req.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             # user = User(email=data["email"],
#             #             login=data["login"],
#             #             password=data["password"])
#         return HttpResponseRedirect("..")
#     else:
#         form = Login()
#     return render(req, "cw/login.html", {"form":form})

def page(req, id):
    page = Page.objects.get(id=id)
    return render(req, "cw/page.html", {"page": page})