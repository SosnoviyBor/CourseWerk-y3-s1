from enum import unique
from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        result = f"{self.email}, {self.login}, {self.password}"
        return result

class Page(models.Model):
    head = models.TextField()
    desc = models.TextField()
    img = models.TextField(blank=False)
    author = models.CharField(max_length=100)
    date_created = models.DateField(default=date.today)

class PageRelation(models.Model):
    which = models.ForeignKey(Page, related_name="which", on_delete=models.CASCADE)
    comes_after = models.ForeignKey(Page, related_name="comes_after", on_delete=models.CASCADE)
    strength = models.FloatField()

    class Meta:
        unique_together = [["which", "comes_after"]]

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    status = models.IntegerField()

    class Meta:
        unique_together = [["user", "page"]]