from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import idScanForm
from django.conf import settings
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from models import Visitors
# from .forms import VisitorsForm

# Create your views here.
def welcome(request):
  
    return render(request,'welcome.html')

def add_visitor(request):
    if request.method=='POST':
        form=idScanForm(request.POST)
        if form.is_valid():
            Idnumber =form.cleaned_data['Idnumber']
            FirstName =form.cleaned_data['FirstName']
            LastName =form.cleaned_data['LastName']
            EntryTime =form.cleaned_data['EntryTime']
            ExitTime =form.cleaned_data['ExitTime']
            category=forms.cleaned_data['category']
            propertycode=forms.cleaned_data['category']
            propertyname=forms.cleaned_data['category']
    print("VALID")
    # form=idScanForm()
    return  render(request,'add_visitor.html')
# def Snippet_details(request):
#     if request.method=='POST':
#         form=SnippetForm(request.POST)
#         if form.is_valid():
#             Idnumber =form.cleaned_data['Idnumber']
#             FirstName =form.cleaned_data['FirstName']
#             LastName =form.cleaned_data['LastName']
#             EntryTime =form.cleaned_data['EntryTime']
#             ExitTime =form.cleaned_data['ExitTime']
#     print("VALID")
#     form=SnippetForm()
#     return  render(request,'add_visitor.html',{'form':form})

def fingerPrint(request):

    return  render(request,'fingerPrint.html')
def rfidScan(request):

    return  render(request,'RFIDscan.html')
    
def faceRecognation(request):

    return  render(request,'faceRecognation.html')   

def ScanEquip(request):

    return  render(request,'ScanEquip.html') 
@login_required(login_url='/accounts/login/')
def RegisterEqipment(request):

    return  render(request,'RegisterEqipment.html') 
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'welcome.html', {
        'form': form
    })