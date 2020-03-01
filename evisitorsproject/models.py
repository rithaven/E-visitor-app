from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models


# Create your models here.
class Idscan(models.Model):
      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      category=forms.CharField(max_length=30)
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)
      user=models.ForeignKey(User)

class Fingerprint(models.Model):
      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      category=forms.CharField(max_length=30)
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)

class Rfidscan(models.Model):
      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      category=forms.CharField(max_length=30)
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)

class Facerecognation(models.Model):
      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)

class  ScanEquipment(models.Model):
      FullName=forms.CharField(max_length=30)
      email=forms.CharField(max_length=30)
      phoneNumber=forms.CharField(max_length=30)
      PresentAddress=forms.CharField(max_length=30)
      PermanentAddress=forms.CharField(max_length=30)
      equipId=forms.CharField(max_length=30)

class Registration(models.Model):
      EquipNumber=forms.CharField(max_length=30)
      EquipName=forms.CharField(max_length=30)
      EquipRoom=forms.CharField(max_length=30)
      ProductName=forms.CharField(max_length=30)
      EquipIdcode=forms.CharField(max_length=30)
      equipLocation=forms.CharField(max_length=30)