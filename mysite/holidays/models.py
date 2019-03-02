from django.db import models

# Create your models here.
class HolidayImage(models.Model):
    thumb = models.ImageField(default='default.jpg')
