from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.

def home(response):
    pages = Page.objects
    if action := response.GET.get("action"):
        if action == "search":
            query = response.GET.get("value")
            queries = [query.lower(), query.title(), query.upper()]
            pages = pages.filter(head__in=queries)
        else:
            print("Recieved GET request with no 'action' param")
    return render(response, "cw/home.html", {"pages":pages})

def register(response):
    if response.method == "POST":
        form = Register(response.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(email=data["email"],
                        login=data["login"],
                        password=data["password"])
            #user.save()
        return HttpResponseRedirect("..")
    else:
        form = Register()
    return render(response, "cw/register.html", {"form":form})

def page(response, id):
    page = Page.objects.get(id=id)
    return render(response, "cw/page.html", {"page": page})