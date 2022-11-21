from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("page/<int:id>", views.page, name="page"),
    path("suggestions/", views.suggestions, name="suggestions"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("about/", views.about, name="index"),
]
