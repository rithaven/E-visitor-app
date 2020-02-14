from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

# from django.forms import extras
# from .models import Snippet

class idScanForm(forms.ModelForm):

      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      category=forms.CharField(max_length=30)
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)

      # class Meta:
      #       model= Idscan
      #       fields=('Idnumbe','FirstName','LastName','EntryTime','ExitTime','category','propertycode','propertyname')