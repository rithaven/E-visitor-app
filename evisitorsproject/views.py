from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect,get_object_or_404
from .forms import idScanForm,FacerecognationForm,attendanceForm,attendanceEquipForm,ScanEquipmentForm,FingerprintForm,RfidscanForm,RegistrationForm
from .models import Idscan,ScanEquipment,Facerecognation,attendanceEquip,Rfidscan,Fingerprint,Registration,attendance
from django.conf import settings
from . import models
from django.http import JsonResponse
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
@login_required(login_url='/accounts/login/')
def welcome(request):

    return render(request,'welcome.html')

def add_visitor(request):
    # my_file =  open("127.0.0.1/add_visitor/test.txt", 'r') 
    # response = HttpResponse(my_file.read(), mimetype='text/plain')
    # response['Content-Disposition'] = 'inline;filename=some_file.txt'
    # print(response)
    # handle = open("","r")

    # data = str(handle.readline())
    # print(data[0:21])
    # handle.close()
    form=idScanForm
    formI=ScanEquipmentForm
    formB=attendanceForm
    formC=attendanceEquipForm
    if request.is_ajax():
        form=idScanForm(request.POST)
        formI=ScanEquipmentForm(request.POST)
        formB=attendanceForm(request.POST)
        formC=attendanceEquipForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if Idscan.objects.filter(Id_number=request.POST['Id_number']).exists():
               messages.info(request, 'recorded data already exists in system!')
               return HttpResponseRedirect('/add_visitor/'+Id_number)
            instance.save()
           
            data={
                'message':'form is saved'
            }
        if formB.is_valid():
            instance=formB.save(commit=False)
            instance.save() 
            data={
                'message':'form is saved'
            }
        if formC.is_valid():
            instance=formC.save(commit=False)
            instance.save() 
            data={
                'message':'form is saved'
            }
        if formI.is_valid():
            instance=formI.save(commit=False)
            instance.save()
            data={
                'message':'formI is saved'
            }
            return JsonResponse(data)
    context={
    'form':form,'formI':formI,'formB':formB,'formC':formC
    }
    return  render(request,'add_visitor.html',context)

    # if request.method=="POST":
    #     v_form=idScanForm(request.POST)
    #     if v_form.is_valid():
    #        v_form.save()
    #        return HttpResponseRedirect('/viewreport/')
    # else:
    #     form=idScanForm()
    # if request.method=="POST":
    #     Eq_form=ScanEquipmentForm(request.POST)
    #     if Eq_form.is_valid():
    #         Eq_form.save()
    #         return HttpResponseRedirect('/viewreport/')
    # else:
    #     form=ScanEquipmentForm()
    # data = {'success': 'You have been successfully added recorded data!!'}
    
    # return  render(request,'add_visitor.html',{'v_form':v_form,'Eq_form':Eq_form})
    # return JsonResponse(data) 
# def check(request):
#     if request.method == "POST":
#         form = idScanForm(request.POST)
#         if form.is_valid():
#             Id_number = form.cleaned_data("Id_number ")
#             try:
#                  friend = Idscan.objects.get(Id_number=Id_number)
#                  return render(request,"add_visitor.html",
#                        {"friend":friend})
#             except Idscan.DoesNotExist:
#                 return render(request, "add_visitor.html", {"form":form})
def edit_visitor(request, Id_number):
    item= get_object_or_404(Idscan,id=edit_visitor)
    # form=idScanForm(request.GET or None, instance=item) 
    if request.method =='POST':
        form=idScanForm(request.POST,instance=item)
        if form.is_valid():
           form.save()
        return HttpResponseRedirect("/viewReport")
    else:
        form=idScanForm(instance=item)
    context= {'form':form,'edit_mode':True}
    return  render(request,'add_visitor.html',context)
def validate_Id(request):
    Visitor_Id= request.GET.get('Id_number', None)
    data = {
        'is_taken': User.objects.filter(Id_number__iexact=Visitor_Id).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this ID card number already exists.'
    return JsonResponse(data)  
# def visitor_delete(request, Id_number):
 
#     # dictionary for initial data with  
#     # field names as keys 
#     context ={} 
  
#     # fetch the object related to passed id 
#     obj = get_object_or_404(Idscan, id = Id_number) 
  
  
#     if request.method =="POST": 
#         # delete object 
#         obj.delete() 
#         # after deleting redirect to  
#         # home page 
#         return HttpResponseRedirect("/viewReport") 
  
#     return render(request, "viewReport.html", context) 

    
@login_required(login_url='/accounts/login/')
def viewReport(request):
    # cou=Idscan.objects.get(id=2)
    viewReport=Idscan.objects.all()
    viewReportE=ScanEquipment.objects.all()
    viewReportF=Fingerprint.objects.all()
    viewReportG=Rfidscan.objects.all()
    viewReportH=Facerecognation.objects.all()
    viewReportI=ScanEquipment.objects.all()
    viewReportK=Registration.objects.all()
    return render (request, 'viewReport.html',{'viewReport':viewReport,'viewReportE':viewReportE,'viewReportF':viewReportF,'viewReportG':viewReportG,'viewReportH':viewReportH,'viewReportH':viewReportH,'viewReportI':viewReportI,'viewReportK':viewReportK})
@login_required(login_url='/accounts/login/')
def Attend(request):
    # cou=Idscan.objects.get(id=2)
    visita=Idscan.objects.all()
    visitaE=ScanEquipment.objects.all()
    visitaF=attendanceEquip.objects.all()
    visitaG=attendance.objects.all()
    
    return render (request, 'visitors.html',{'visita':visita,'visitaE':visitaE,'visitaF':visitaF,'visitaG':visitaG})

def visitor_delete(request, id):
    workout = get_object_or_404(Idsca, id= Id_number)
    print(workout)
    if request.user != workout.created_by:
        return HttpResponse('Not ur workout')
    else:
        workout.delete()
        return HttpResponseRedirect('/viewReport')
def searchbar(request):
        '''
        a function to search visitor based on their categories.
        '''

        visitors = Idscan.objects.all()
        if 'Id_number' in request.GET and request.GET['Id_number']:
                visitor_item = request.GET.get('Id_number')
                searched_visitor = Image.search_by_visitor(visitor_item)
                message = f"{visitor_item}"

                return render(request, 'search.html', {"visitorrr":searched_visitor,"message":message, "visitors":visitors})

        else:
                message = "You have'nt search for any term"
        return render(request, 'search.html', {"message": message})
            

   

def fingerPrint(request):
    finger_form=FingerprintForm
    Equip_form=ScanEquipmentForm
    if request.method=="POST":
        finger_form=FingerprintForm(request.POST)
        if  finger_form.is_valid():
            finger_form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        finger_form=FingerprintForm()
    if request.method=="POST":
        Equip_form=ScanEquipmentForm(request.POST)
        if Equip_form.is_valid():
            Equip_form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        Equip_form=ScanEquipmentForm()
    
    return  render(request,'fingerPrint.html',{'finger_form':finger_form,'Equip_form':Equip_form})
    # finger_form=FingerprintForm
    # Eq_form=ScanEquipmentForm
    # if request.method=="POST":
    #     finger_form=FingerprintForm(request.POST)
    #     if  finger_form.is_valid():
    #         finger_form.save()
    #         return HttpResponseRedirect('/viewreport/')
    # else:
    #     form=FingerprintForm()
    # if request.method=="POST":
    #     Eq_form=ScanEquipmentForm(request.POST)
    #     if Eq_form.is_valid():
    #         Eq_form.save()
    #         return HttpResponseRedirect('/viewreport/')
    # else:
    #     form=ScanEquipmentForm()
    
    # return  render(request,'fingerPrint.html',{'finger_form':finger_form,'Eq_form':Eq_form})


def rfidScan(request):
    rf_form=FingerprintForm
    Equipm_form=ScanEquipmentForm
    if request.method=="POST":
        rf_form=RfidscanForm(request.POST)
        if  rf_form.is_valid():
           rf_form.save()
           return HttpResponseRedirect('/viewreport/')
    else:
        rf_form=RfidscanForm()
    if request.method=="POST":
        Equipm_form=ScanEquipmentForm(request.POST)
        if Equipm_form.is_valid():
            Equipm_form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        Equipm_form=ScanEquipmentForm()
    
    return  render(request,'RFIDscan.html',{'rf_form':rf_form,'Equipm_form':Equipm_form})
    # RFID_form=RfidscanForm
    # equip_form=ScanEquipmentForm
    # if request.method=="POST":
    #     RFID_form=RfidscanForm(request.POST)
    #     if RFID_form.is_valid():
    #        RFID_form.save()
    #        return HttpResponseRedirect('/viewreport/')
    # else:
    #    RFID_form=RfidscanForm()

    # if request.method=="POST":
    #     equip_form=ScanEquipmentForm(request.POST)
    #     if equip_form.is_valid():
    #         equip_form.save()
    #         return HttpResponseRedirect('/viewreport/')
    # else:
    #     equip_form=ScanEquipmentForm()
    
    # return  render(request,'RFIDscan.html',{'RFID_form':RFID_form,'equip_form':equip_form})
  

   
    
def faceRecognation(request):
    face_form=FacerecognationForm
    Equipment_form=ScanEquipmentForm
    if request.method=="POST":
        face_form=FacerecognationForm(request.POST)
        if  rf_form.is_valid():
           rf_form.save()
           return HttpResponseRedirect('/viewreport/')
    else:
        face_form=FacerecognationForm()
    if request.method=="POST":
        Equipment_form=ScanEquipmentForm(request.POST)
        if Equipment_form.is_valid():
            Equipment_form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        Equipment_form=ScanEquipmentForm()
    
    
    return  render(request,'faceRecognation.html',{'face_form':face_form,'Equipment_form':Equipment_form})
  

def ScanEquip(request):
    if request.method=="POST":
        s_form=ScanEquipmentForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            return HttpResponseRedirect('/viewreport/')
    else:
        s_form=ScanEquipmentForm()
    
    return  render(request,'ScanEquip.html',{'s_form':s_form})
# def updateVisitor(request,pk):
#     visita=Idscan.objects.get(id=pk)
#     form=idScanForm(instance=visita)
#     context={'form':form}
#     return render(request,'ScanEquip.htm',context)
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

 

