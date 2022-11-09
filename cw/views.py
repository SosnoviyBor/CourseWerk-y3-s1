from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import *

# Create your views here.

def home(req):
    pages = Page.objects
    # if "action" in req.GET:
    #     action = req.GET.get("action")
    #     # Фільтрація за пошуком
    #     if action == "search":
    #         query = req.GET.get("value")
    #         pages = pages.filter(head__icontains=query)
    #     # Отримали GET запит, але якийсь помилковий
    #     else:
    #         print("Home view; Recieved GET request with no 'action' param")
    # TODO Додати до веб-сторінки та контексту статуси сторінок
    # folders = Folder.objects.filter(page=pages)
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
    if Folder.objects.filter(user=req.user, page=page).exists():
        status = Folder.objects.get(user=req.user, page=page).status
    else:
        status = "none"
    return render(req, "cw/page.html", {"page":page, "status":status})

def profile(req):
    folders = Folder.objects.filter(user=req.user.id)
    return render(req, "cw/profile.html", {"folders":folders})