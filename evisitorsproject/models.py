from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms
from django.db import models



# Create your models here.
class Idscan(models.Model):
      CHOICES = (
        ('A visitor', (
            (11, 'v_Laptop'),
            (12, 'v_tablet'),
            (13, 'v_Desktop machine'),
        )),

        ('Instutition', (
            (11, 'inst_Laptop'),
            (12, 'inst_tablet'),
            (13, 'inst_Desktop machine'),
        )),

        ('current instutition', (
            (11, 'current_Laptop'),
            (12, 'current_tablet'),
            (13, 'current_Desktop machine'),
        )),
    )
      Id_number=models.CharField(null=True,max_length=21)
      First_name=models.CharField(max_length=50, null=True)
      Last_name=models.CharField(max_length=30,null=True)
      place_Of_Isue=models.CharField(max_length=21,null=True)
     
      property_owner=models.CharField(choices=CHOICES,max_length=300,null=True)
      property_code=models.CharField(max_length=300,null=True)
      Institution_name=models.CharField(max_length=1000,null=True)
      date = models.DateTimeField(auto_now_add=True,null=True)



      def save_visitor(self):
        self.save()

      @classmethod
      def todays_visitor(cls):
        today = dt.date.today()
        visitors = cls.objects.filter(pub_date__date = today)
        return vistors
      @classmethod
      def search_by_Id(cls,search_term):
        visitors = cls.objects.filter(Idscan__date__icontains=search_term)
        return visitors

      def __str__(self):
        return str(self.indanga)

      # class Meta:
      #   ordering = ['indanga']
    
      
      #     @classmethod
      #     def search_by_category(cls,search_term):
      #       visitors = cls.objects.filter(category__name__icontains=search_term)
      #       return images

      # class Meta:
      #       ordering = ['indanga']

class VisitorInfo(models.Model):
      Idnumber=models.CharField(max_length=30,null=True)
      FirstName=models.CharField(max_length=30,null=True)
      LastName=models.CharField(max_length=30,null=True)
      EntryTime=models.DateField(null=True)
      ExitTime=models.DateField(null=True)
      category=models.CharField(max_length=30,null=True)
      propertycode=models.CharField(max_length=30,null=True)
      propertyname=models.CharField(max_length=30,null=True)

class Fingerprint(models.Model):
      Idnumber=models.CharField(max_length=30,null=True)
      FirstName=models.CharField(max_length=30,null=True)
      LastName=models.CharField(max_length=30,null=True)
      EntryTime=models.DateField(null=True)
      ExitTime=models.DateField(null=True)
      category=models.CharField(max_length=30,null=True)
      propertycode=models.CharField(max_length=30,null=True)
      propertyname=models.CharField(max_length=30,null=True)

class Rfidscan(models.Model):
      Idnumber=models.CharField(max_length=30,null=True)
      FirstName=models.CharField(max_length=30,null=True)
      LastName=models.CharField(max_length=30,null=True)
      EntryTime=models.DateField(null=True)
      ExitTime=models.DateField(null=True)
      category=models.CharField(max_length=30,null=True)
      propertycode=models.CharField(max_length=30,null=True)
      propertyname=models.CharField(max_length=30,null=True)

class Facerecognation(models.Model):
      
      face=models.ImageField(upload_to ='viewReport/')
      Id_number=models.CharField(null=True,max_length=21)
      First_name=models.CharField(max_length=50, null=True)
      Last_name=models.CharField(max_length=30,null=True)
      place_Of_Isue=models.CharField(max_length=21,null=True)
     
      property_owner=models.CharField(max_length=300,null=True)
      property_code=models.CharField(max_length=300,null=True)
      Institution_name=models.CharField(max_length=1000,null=True)
      date = models.DateTimeField(auto_now_add=True,null=True)

      def __str__(self):
            return self.Id_number


class  ScanEquipment(models.Model):
      FullName=models.CharField(max_length=30,null=True)
      email=models.CharField(max_length=30,null=True)
      phoneNumber=models.CharField(max_length=30,null=True)
      PresentAddress=models.CharField(max_length=30,null=True)
      PermanentAddress=models.CharField(max_length=30,null=True)
      equipId=models.CharField(max_length=30,null=True)

class Registration(models.Model):
      EquipNumber=models.CharField(max_length=30,null=True)
      EquipName=models.CharField(max_length=30,null=True)
      EquipRoom=models.CharField(max_length=30,null=True)
      ProductName=models.CharField(max_length=30,null=True)
      EquipIdcode=models.CharField(max_length=30,null=True)
      equipLocation=models.CharField(max_length=30,null=True)