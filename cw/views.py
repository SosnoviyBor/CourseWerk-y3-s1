from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
import operator
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
    if (req.user.is_authenticated and Folder.objects.filter(user=req.user, page=page).exists()):
        # Користувач зареєстрований ТА вже виставив статус цієї сторінки
        status = Folder.objects.get(user=req.user, page=page).status
    else:
        status = None

    # Перелік рекомендованих тем перед проходженням
    r_cards = []
    for relation in PageRelation.objects.filter(which=id):
        r_cards.append(relation.comes_after)
    recommended = cards_ctx(req, r_cards)
    return render(req, "cw/page.html", {"page":page, "status":status, "recommended": recommended})

def suggestions(req):
    if (not req.user.is_authenticated
            or not Folder.objects.filter(user=req.user, status=2).exists()):
        # Користувач не має папок для генерації рекомендацій
        # Тому ми даємо йому такий собі "набір початківця"
        top_ids = [4,5,6,20]
        # 4 - ООП
        # 5 - SQL
        # 6 - Git
        # 20 - Linux
        if req.user.is_authenticated:
            msg = "Оскільки у Вас нема жодних тем у 'Пройдених', \
                   ми підготували Вам набір для початку своєї мандрівки у світ ІТ-технологій"
        else:
            msg = "Оскільки ви не зареєстровані, ми не можемо згенерувати рекомендації саме для Вас"
    else:
        msg = ""
        all_ids = {}
        folders = Folder.objects.filter(user=req.user)

        # Рахуємо загальну вигідність кожної сторінки
        for relation in PageRelation.objects.all():
            if (folders.filter(page=relation.comes_after, status=2).exists()
                    and not folders.filter(page=relation.which, status=2).exists()):
                if not relation.which.id in all_ids.keys():         # Більше фантомних помилок!
                    all_ids[relation.which.id] = relation.strength
                else:
                    all_ids[relation.which.id] += relation.strength
        # Отримуємо 4 найоптимальніші варіанти
        top_pages = sorted(all_ids.items(), key=operator.itemgetter(1), reverse=True)[:4]
        top_ids = [i[0] for i in top_pages]

    # І замість звичайного фільтру по масиву, дістаємо сторінки поштучно, аби зберегти їх порядок
    # Інакше вони будуть відсортовані по айдішці
    pages = []
    for id in top_ids:
        pages.append(Page.objects.get(id=id))
    cards = cards_ctx(req, pages)
    return render(req, "cw/suggestions.html", {"cards":cards, "msg":msg})

def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        # Перевірка, чи точно це дані для реєстрації
        if form.is_valid():
            form.save()
            return redirect("..")
    else:
        # Генерація пустої форми для реєстрації
        form = RegisterForm()
    return render(req, "cw/register.html", {"form":form})

def profile(req):
    cards = cards_ctx(req, Page.objects.all())
    return render(req, "cw/profile.html", {"cards":cards})

def stats(req):
    stats = []  # [page, active, planned, done]
    pages = Page.objects.all()
    raw = Folder.objects.all().values("page", "status").annotate(total=Count("status")).order_by("page").all()
    for page in pages:              # Ітеруємо усі існуючі теми/сторінки
        tmp = [page.head]
        for i in range(3):          # Допоміжна змінна для парсу усіх статусів по черзі
            count_was_added = False
            for data in raw:        # Ітеруємо усі словники із даними, щоб перевірити, чи є дані по нашій сторінці чи ні
                if data["page"] == page.id and data["status"] == i: # <-- Чомусть тут (page.id) VS Code каже, що э помилка
                    tmp.append(data["total"])                       # При тому, що все працює як і потрібно...
                    count_was_added = True
                    break
            if not count_was_added:
                tmp.append(0)   # Теж фантомна помилка у VS Code
        stats.append(tmp)
    usercount = len(User.objects.all())
    return render(req, "cw/stats.html", {"stats": stats, "usercount":usercount})

def about(req):
    return render(req, "cw/about.html", {})