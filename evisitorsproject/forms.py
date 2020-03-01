from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Idscan,Fingerprint,Rfidscan,Facerecognation,ScanEquipment,Registration



class idScanForm(forms.ModelForm):

      Idnumber=forms.CharField(max_length=30)
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      category=forms.CharField(max_length=30)
      propertycode=forms.CharField(max_length=30)
      propertyname=forms.CharField(max_length=30)

      class Meta:
            model= Idscan
            fields=('Idnumber','FirstName','LastName','EntryTime','ExitTime','category','propertycode','propertyname')
class FingerprintForm(forms.ModelForm):
     
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      tel=forms.CharField(max_length=30)
      recodedtime=forms.DateField()
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      propertyname=forms.CharField(max_length=30)
      propertyid=forms.CharField(max_length=30)

      class Meta:
            model= Fingerprint
            fields=('FirstName','LastName','tel','recodedtime','EntryTime','ExitTime','propertyname','propertyid',)
class RfidscanForm(forms.ModelForm):
     
      FirstName=forms.CharField(max_length=30)
      LastName=forms.CharField(max_length=30)
      tel=forms.CharField(max_length=30)
      recodedtime=forms.DateField()
      EntryTime=forms.DateField()
      ExitTime=forms.DateField()
      propertyname=forms.CharField(max_length=30)
      propertyid=forms.CharField(max_length=30)

      class Meta:
            model= Rfidscan
            fields=('FirstName','LastName','tel','recodedtime','EntryTime','ExitTime','propertyname','propertyid',)

class Registration(forms.ModelForm):
     
      EquipNumber=forms.CharField(max_length=30)
      EquipName=forms.CharField(max_length=30)
      EquipRoom=forms.CharField(max_length=30)
      ProductName=forms.CharField(max_length=30)
      EquipIdcode=forms.CharField(max_length=30)
      equipLocation=forms.CharField(max_length=30)

      class Meta:
            model= Registration
            fields=('EquipNumber','EquipName','EquipRoom','ProductName','EquipIdcode','equipLocation',)



