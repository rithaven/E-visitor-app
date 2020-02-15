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

    form=idScanForm(request.POST)
    if form.is_valid():
        add_visitor=form.save(commit=False)
        add_visitor.user=request.user
        add_visitor.save()
        # text=form.clear_data['add_visitor']
        form=idScanForm()
    
        return redirect('welcome')
    # args={'form':form,'text':text}
   
    return  render(request,'add_visitor.html')

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