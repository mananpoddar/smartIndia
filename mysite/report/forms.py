from django import forms
from . import models

class ReportForm(forms.ModelForm):
    # aadhar_no = forms.IntegerField()
    # name      = forms.CharField(max_length=100)
    # address   = forms.TextField(max_length=100)
    # statement = forms.TextField()
    # title = forms.CharField(max_length=128)
    # body = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = models.Report
        fields = ('aadhar_no', 'name', 'address','statement' )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = models.Images
        fields = ('image', )