from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *
from .utils import *

# Create your views here.

def home(req):
    query = ""
    pages = Page.objects.all()
    if req.GET.get("search"):
        # Користувач використав пошук
        query = req.GET.get("search")
        pages = pages.filter(head__icontains=query, desc__icontains=query)

    cards = cards_ctx(req, pages)
    return render(req, "cw/home.html", {"cards":cards, "search":query})

def about(req):
    return render(req, "cw/about.html", {})

def suggestions(req):
    cards = cards_ctx(req, Page.objects.all())
    return render(req, "cw/suggestions.html", {"cards":cards})

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

@csrf_exempt
def page(req, id):
    page = Page.objects.get(id=id)
    if req.method == "POST":
        action = req.POST.get("action")
        # Користувач намагається змінити категорію теми
        if action == "setfolder" and req.user.is_authenticated:
            status = req.POST.get("value")
            # Видалення об'єкту
            if status == "none":
                Folder.objects.filter(user=req.user, page=page).delete()
            # Оновлення або створення об'єкту
            else:
                # obj - об'єкт, що був створений/оновлений
                # created - True якщо створений, False якщо оновлений
                obj, created = Folder.objects.update_or_create(
                    user=req.user, page=page,
                    defaults={"status":status}
                )
            return HttpResponse(req)
        else:
            print("Page view; Recieved POST request with no 'action' param")

    # Отримання статусу для відображення на сторінці
    status = None
    if (req.user.is_authenticated and
            Folder.objects.filter(user=req.user, page=page).exists()):
        status = Folder.objects.get(user=req.user, page=page).status
    return render(req, "cw/page.html", {"page":page, "status":status})

def profile(req):
    cards = cards_ctx(req, Page.objects.all())
    return render(req, "cw/profile.html", {"cards":cards})