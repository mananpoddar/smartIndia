from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator

class Aadhar(models.Model):
    aadhar_no = models.IntegerField(default=0, unique=True)
    name      = models.CharField(max_length=100,default = None)
    address   = models.TextField(max_length=100,default=None)

class Bank_formalities(models.Model):
    address =   models.TextField(max_length=100,default=None)
    ac_no   =   models.IntegerField(default=0,unique=True)
    aadhar_no = models.IntegerField(default=0, unique=True)


class tracked(models.Model):
    aadhar_no = models.IntegerField(default=0, unique=True)
    address   = models.TextField(max_length=100,default=None)


class bank_statement(models.Model):
    aadhar_no        =       models.IntegerField(default=0,unique=True)
    lEdu            =       models.IntegerField(default=0)
    hEdu            =       models.IntegerField(default=0)
    area            =       models.CharField(default=0,max_length=100)
    jewellery       =       models.IntegerField(default=0)
    cars            =       models.IntegerField(default=0)
    bikes           =       models.IntegerField(default=0)
    tax             =       models.IntegerField(default=0)
    credit          =       models.IntegerField(default=0)
    debit           =       models.IntegerField(default=0)


class Bank_details(models.Model):
    ac_no   =   models.IntegerField(default=0,unique=True)
    bank_statement  =   models.ForeignKey(bank_statement,on_delete=models.CASCADE)

class predicted_features(models.Model):
    aadhar_no        =       models.IntegerField(default=0,unique=True)
    lEdu            =       models.IntegerField(default=0)
    hEdu            =       models.IntegerField(default=0)
    area            =       models.CharField(default=0,max_length=100)
    jewellery       =       models.IntegerField(default=0)
    cars            =       models.IntegerField(default=0)
    bikes           =       models.IntegerField(default=0)
    tax             =       models.IntegerField(default=0)
    credit          =       models.IntegerField(default=0)
    debit           =       models.IntegerField(default=0)
    fraud           =       models.BooleanField(default=0)

class report(models.Model):
    aadhar_no        =       models.IntegerField(default=0,unique=False)
    reason           =       models.TextField(default='a')
    image            =       models.ImageField(upload_to='holidays/', default='default.jpg')
    amount           =       models.IntegerField(default=0,blank=True,null=True)
