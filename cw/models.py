from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Page(models.Model):
    head = models.TextField()
    desc = models.TextField()
    img = models.TextField(blank=False)
    data = models.TextField()
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