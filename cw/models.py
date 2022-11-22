from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q
from datetime import date

# Create your models here.

class Page(models.Model):
    head = models.TextField()
    desc = models.TextField()
    # Зараз відображення альбомних зображень у картках криве, тому майте це на увазі
    img = models.TextField(blank=False)
    data = models.TextField()
    author = models.CharField(max_length=100)
    date_created = models.DateField(default=date.today)

class PageRelation(models.Model):
    which = models.ForeignKey(Page, related_name="which", on_delete=models.CASCADE)
    comes_after = models.ForeignKey(Page, related_name="comes_after", on_delete=models.CASCADE)
    strength = models.IntegerField(     # Обмеження на рівні моделі
        validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        unique_together = [["which", "comes_after"]]
        constraints = ([     # Обмеження на рівні БД
            CheckConstraint(
                check=Q(strength__gte=0) & Q(strength__lte=100),
                name='strength_range')])

class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    status = models.IntegerField()  # 0 - активні, 1 - плани, 2 - пройдені

    class Meta:
        unique_together = [["user", "page"]]