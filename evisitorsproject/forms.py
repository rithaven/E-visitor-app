from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Idscan,VisitorInfo,Fingerprint,Rfidscan,Facerecognation,Registration,ScanEquipment


class idScanForm(ModelForm):
      class Meta:
            model= Idscan
            fields='__all__'
           
     
class FacerecognationForm(ModelForm):
      class Meta:
            model=Facerecognation
            fields='__all__'

class ScanEquipmentForm(ModelForm):
       class Meta:
            model=ScanEquipment
            fields='__all__'

class FingerprintForm(ModelForm):
      class Meta:
            model= Fingerprint
            fields='__all__'
class RfidscanForm(ModelForm):
      class Meta:
            model= Rfidscan
            fields='__all__'

class RegistrationForm(ModelForm):
      class Meta:
            model= Registration
            fields='__all__'


