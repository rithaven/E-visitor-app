from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect,get_object_or_404
from .forms import idScanForm,FacerecognationForm,ScanEquipmentForm,FingerprintForm,RfidscanForm,RegistrationForm
from .models import Idscan,ScanEquipment,Facerecognation,Rfidscan,Fingerprint,Registration
from django.conf import settings
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# from imutils.video import VideoStream
# from pyzbar import pyzbar
import argparse
from datetime import timedelta
# import imutils
import time


continue_reading = True
# Create your views here.
def welcome(request):

    return render(request,'welcome.html')

def add_visitor(request):
    if request.method=="POST":
        form=idScanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=idScanForm()
    
    return  render(request,'add_visitor.html',{'form':form})

     
def edit_visitor(request, id=None):
    item= get_object_or_404(Idscan,id=id)
    form=idScanForm(request.GET or None, instance=item) 
    if form.is_valid():
       form.save()
       return redirect('/viewReport/' +str(item.id)+'/')
    return  render(request,'add_visitor.html',{'form':form})

@login_required(login_url='/accounts/login/')
def viewReport(request):
    viewReport=Idscan.objects.all().order_by('-date')
    viewReportE=ScanEquipment.objects.all().order_by('-date')
    viewReportF=Fingerprint.objects.all().order_by('-date')
    viewReportG=Rfidscan.objects.all().order_by('-date')
    viewReportH=Facerecognation.objects.all().order_by('-date')
    viewReportI=ScanEquipment.objects.all().order_by('-date')
    viewReportK=Registration.objects.all().order_by('-date')
    return render (request, 'viewReport.html',{'viewReport':viewReport,'viewReportE':viewReportE,'viewReportF':viewReportF,'viewReportG':viewReportG,'viewReportH':viewReportH,'viewReportH':viewReportH,'viewReportI':viewReportI,'viewReportK':viewReportK})

def search(request):
    if request.method=='POST':
        srch=request.POST['srh']
        if srch:
            match=Idscan.objects.filter(Q(date__icontains=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                message.error(request,'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')
          

   

def fingerPrint(request):
    if request.method=="POST":
        form=FingerprintForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=FingerprintForm()
    
    return  render(request,'fingerPrint.html',{'form':form})


def rfidScan(request):
    if request.method=="POST":
        form=FingerprintForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=FingerprintForm()
    return  render(request,'RFIDscan.html',{'form':form})
    
def faceRecognation(request):
    if request.method=="POST":
        form= FacerecognationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=FacerecognationForm()
    return  render(request,'faceRecognation.html',{'form':form})   

def ScanEquip(request):
    if request.method=="POST":
        form=ScanEquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=ScanEquipmentForm()
    
    return  render(request,'ScanEquip.html',{'form':form})

@login_required(login_url='/accounts/login/')
def RegisterEqipment(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        form=RegistrationForm()
    
    return  render(request,'RegisterEqipment.html',{'form':form})
   
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
    return render(request, 'welcome.html', {'form': form})
   

def borcodeRead(request):

    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="barcodes.csv", help="path to output CSV file containing barcodes")
    args = vars(ap.parse_args())
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    #time.sleep(0.5)
    csv = open(args["output"], "a") #a
    found = set()
    # loop over the frames from the video stream
    while True:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        cv2.line(frame, (85, 50), (100, 50), (255, 255, 255), 2)
        #cv2.line(frame, (100, 30), (100, 50), (255, 255, 255), 2)
        
        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw
            # the bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it
            # on our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # if the barcode text is currently not in our CSV file, write
            # the timestamp + barcode to disk and update the set
            if barcodeData not in found:
                csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
                csv.flush()
                found.add(barcodeData)
                
            # show the output frame
            cv2.imshow("QR-Code Scanner", frame)
            key = cv2.waitKey(1) & 0xFF
            
            # if the <code data-enlighter-language="generic" class="EnlighterJSRAW">q</code> key was pressed, break from the loop
            if key == ord("q"):
                break
            # close the output CSV file do a bit of cleanup
            print("[INFO] cleaning up...")
            csv.close()
            cv2.destroyAllWindows()
            return redirect('welcome')
            
    return render('request','barcodeRead.html')    

 

