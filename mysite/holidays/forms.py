from django import forms
from . import models

class HolidayImageForm(forms.ModelForm):
    class Meta:
        model = models.HolidayImage
        fields = ['thumb']

