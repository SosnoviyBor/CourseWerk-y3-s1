"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Додаємо до проекту адміністраторський дешборд для управління підключенною БД
    path('admin/', admin.site.urls),
    # Додаємо до проекту сторінки застосунку "cw"
    # Темплейти сторінок зберігаються у "./templates/cw"
    path("", include("cw.urls")),
    # Додаємо до проекту вбудовані сторінки для регістрації, логіну та всякого такого
    # Темплейти сторінок зберігаються у "./templates/registration"
    path("", include("django.contrib.auth.urls")),
]
