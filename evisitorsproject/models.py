from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms
from django.db import models
from django.core.exceptions import ValidationError



# Create your models here.
class Idscan(models.Model):
      
      ID_card_No=models.CharField(max_length =21,null=True,blank=False,help_text="Scan the  ID card*")
      # Names=models.CharField(max_length=50, null=True,blank=False,help_text="Names must much*")
      date= models.DateTimeField(auto_now_add=True,null=True,blank=False,)
 
      def save_visitor(self):
        self.save()
      

      # @classmethod
      # def todays_visitor(cls):
      #   today = dt.date.today()
      #   visitors = cls.objects.filter(pub_date__date=today)
      #   return vistors

      @classmethod
      def search_by_visitor(cls,visitor_term):
        visitorrr = cls.objects.filter(Id_number__icontains=visitor_term)
        return visitorrr

      # def __str__(self):
      #   return str(self. Id_number)

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
      StaffRoom='StaffRoom'
      ComputerLab='ComputerLab'
      EmployeeRoom='EmployeeRoom'
      equip_CHOICES = [
            (StaffRoom, 'StaffRoom'),
            (ComputerLab, 'ComputerLab'),
            (EmployeeRoom, 'EmployeeRoom'),
        
      ]
      
      Id_number=models.CharField(max_length=21,null=True)
      Names=models.CharField(max_length=50,null=True)
      Destination=models.CharField(max_length=50,null=True,choices=equip_CHOICES,default=StaffRoom)
      Tel=models.CharField(null=True,max_length=21)
      date= models.DateTimeField(auto_now_add=True,null=True)

      def save_visitor(self):
        self.save()
      

      @classmethod
      def todays_visitor(cls):
        today = dt.date.today()
        visitors = cls.objects.filter(pub_date__date=today)
        return vistors

      @classmethod
      def search_by_Id(cls,search_term):
        visitors = cls.objects.filter(Idscan__date__icontains=search_term)
        return visitors

      def __str__(self):
        return str(self. Id_number)

class Rfidscan(models.Model):
      RFId_number=models.CharField(null=True,max_length=21)
      Names=models.CharField(max_length=50, null=True)
      Tel=models.CharField(null=True,max_length=21)
      date = models.DateTimeField(auto_now_add=True,null=True)
      def save_visitor(self):
        self.save()
      

      @classmethod
      def todays_visitor(cls):
        today = dt.date.today()
        visitors = cls.objects.filter(pub_date__date=today)
        return vistors

      @classmethod
      def search_by_Id(cls,search_term):
        visitors = cls.objects.filter(Idscan__date__icontains=search_term)
        return visitors

      def __str__(self):
        return str(self. Id_number)

class Facerecognation(models.Model):
      
      # face_image=models.ImageField(upload_to ='viewReport/',null=True)
      Id_number=models.CharField(null=True,max_length=21)
      Names=models.CharField(max_length=50, null=True)
      Tel=models.CharField(null=True,max_length=21)
      date = models.DateTimeField(auto_now_add=True,null=True)


      def __str__(self):
            return self.Id_number

class attendanceEquip(models.Model):
      Laptop ='Laptop'
      Tablet='Tablet'
      none='none'
      DestopMachine='DestopMachine'
      equip_CHOICES = [
            (Laptop, 'Laptop'),
            (Tablet, 'Tablet'),
            (DestopMachine, 'DestopMachine'),
            (none,'none'),
        
      ]
      
      # EquipNumber =models.CharField(max_length=100,null=True,help_text="Scan the  equipment's barcode*")
      ID_card_No=models.CharField(max_length=21,null=True,blank=False,help_text="Visitor's ID Card number*")
      Names=models.CharField(max_length=100,null=True,help_text="Provide the names of owner of Equipment*")
      # EquipName=models.CharField(max_length=20,null=True,choices=equip_CHOICES ,
      #   default=none,help_text="Type of Equipment*")
      # Destination= models.CharField(max_length=30,null=True,blank=False,help_text="Destination is required*")
      # Owner= models.CharField(max_length=30,null=True,blank=False,help_text="Names  of the owner*")
      Tel= models.CharField(max_length=30,null=True,blank=False,help_text="Phone number*")
      date= models.DateTimeField(auto_now_add=True,null=True)

      def __str__(self):
            return self.Id_number
class  ScanEquipment(models.Model):
      Laptop ='Laptop'
      Tablet='Tablet'
      none='none'
      DestopMachine='DestopMachine'
      equip_CHOICES = [
            (Laptop, 'Laptop'),
            (Tablet, 'Tablet'),
            (DestopMachine, 'DestopMachine'),
            (none,'none'),
        
      ]
      
      # EquipNumber =models.CharField(max_length=100,null=True,help_text="Scan the  equipment's barcode*")
      ID_card_No=models.CharField(max_length=21,null=True,blank=False,help_text="Visitor's ID Card number*")
      Names=models.CharField(max_length=100,null=True,help_text="Provide the names of owner of Equipment*")
      # EquipName=models.CharField(max_length=20,null=True,choices=equip_CHOICES ,
      #   default=none,help_text="Type of Equipment*")
      # Destination= models.CharField(max_length=30,null=True,blank=False,help_text="Destination is required*")
      # Owner= models.CharField(max_length=30,null=True,blank=False,help_text="Names  of the owner*")
      Tel= models.CharField(max_length=30,null=True,blank=False,help_text="Phone number*")
      date= models.DateTimeField(auto_now_add=True,null=True)

      def __str__(self):
            return self.Id_number

class attendance(models.Model):
          # EquipNumber =models.CharField(max_length=100,null=True,help_text="Scan the  equipment's barcode*")
          Equip_No=models.CharField(max_length=21,null=True,blank=False,help_text="Scan Equipment*")
          Equip_Name=models.CharField(max_length=21,null=True,blank=False,help_text="Provide  equipment name*")
         

          def __str__(self):
                return self.Id_number


class Registration(models.Model):
      visitor ='visitor'
      current_instutition='urrent_instutition'
      visited_instutition='visited_instutition'
      Property_CHOICES = [
            (visitor,'visitor'),
            (current_instutition,'current_instutition'),
            (visited_instutition,'visited_instutition'),
        
      ]
      
      EquipNumber=models.CharField(max_length=30,null=True,blank=False,)
      owner=models.CharField(max_length=30,null=True,blank=False,choices=Property_CHOICES,
        default=visitor)
      Id_number=models.CharField(max_length=30,null=True,blank=False,)
      Equip_Name=models.CharField(max_length=30,null=True,blank=False,)
      Tel=models.CharField(max_length=30,null=True,blank=False,)
      date = models.DateTimeField(auto_now_add=True,null=True,blank=False,)

     