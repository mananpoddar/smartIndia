from django.db import models

# Create your models here.
class Report(models.Model):
    aadhar_no = models.IntegerField(default=0, unique=True)
    name      = models.CharField(max_length=100,default = None)
    address   = models.TextField(max_length=100,default=None)
    statement = models.TextField()

def get_image_filename(instance, filename):
    id = instance.report.id
    return "report_images/%s" % (id)  

class Images(models.Model):
    report = models.ForeignKey(Report, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
