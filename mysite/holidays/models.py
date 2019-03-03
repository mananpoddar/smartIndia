from django.db import models

# Create your models here.
class HolidayImage(models.Model):
    thumb = models.ImageField(upload_to='holidays/', default='default.jpg')
