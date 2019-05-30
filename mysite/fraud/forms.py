from django.db import models
from django import forms
from fraud.models import User,report



class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name","email",)

class Reporting(forms.ModelForm):
    class Meta:
        model = report
        fields = "__all__"