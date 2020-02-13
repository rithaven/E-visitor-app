from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models
# from django.forms import extras
# from tinymce.models import HTMLField

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
      
      def __str__(self):
        return self.Idnumber
               