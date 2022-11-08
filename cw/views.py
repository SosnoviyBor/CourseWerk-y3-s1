from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def home(req):
    pages = Page.objects
    if "action" in req.GET:
        action = req.GET.get("action")
        # Фільтрація за пошуком
        if action == "search":
            query = req.GET.get("value")
            pages = pages.filter(head__icontains=query)
        # Отримали GET запит, але якийсь помилковий
        else:
            print("Recieved GET request with no 'action' param")
    return render(req, "cw/home.html", {"pages":pages})

def about(req):
    return render(req, "cw/about.html", {})

def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        # Користувач намагається зареєструватись
        if form.is_valid():
            # Він зміг!
            form.save()
            return redirect("..")
    else:
        # Генерація пустої форми для реєстрації
        form = RegisterForm()
    return render(req, "cw/register.html", {"form":form})

def page(req, id):
    page = Page.objects.get(id=id)
    return render(req, "cw/page.html", {"page": page})

def profile(req):
    folders = Folder.objects.filter(user=req.user.id)
    return render(req, "cw/profile.html", {"folders":folders})