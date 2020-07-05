from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url('^$', views.welcome, name = 'welcome'),
    url(r'^add_visitor/',views.add_visitor, name='add_visitor'),
    url(r'^edit/visitor/(?P<id>\d+)/$',views.edit_visitor, name='edit_visitor'),
    url(r'viewReport/',views.viewReport, name='viewReport'),
    # url(r'today/',views.entryDate,name='entryDate'),
    url(r'fingerPrint/',views.fingerPrint, name='fingerPrint'),
    url(r'^search/', views.search, name='search'),
    url(r'rfidScan/', views.rfidScan, name='rfidScan'),
    url(r'faceRecognation/', views.faceRecognation, name='faceRecognation'),
    url(r'ScanEquip/', views.ScanEquip, name='ScanEquip'),
    url(r'RegisterEqipment/', views.RegisterEqipment, name='RegisterEqipment'), 
    url(r'borcodeRead/', views.borcodeRead, name='borcodeRead')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
