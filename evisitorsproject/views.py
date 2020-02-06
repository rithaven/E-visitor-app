from django.http import HttpResponseRedirect
from django.shortcuts import render
# from models import Visitors
# from .forms import VisitorsForm

# Create your views here.
def welcome(request):
  
    return render(request,'welcome.html')

def add_visitor(request):

    return  render(request,'add_visitor.html')
    
def fingerPrint(request):

    return  render(request,'fingerPrint.html')
def rfidScan(request):

    return  render(request,'RFIDscan.html')
    
def faceRecognation(request):

    return  render(request,'faceRecognation.html')   

def ScanEquip(request):

    return  render(request,'ScanEquip.html') 

def RegisterEqipment(request):

    return  render(request,'RegisterEqipment.html') 