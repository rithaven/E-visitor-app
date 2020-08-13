from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url('^$', views.welcome, name = 'welcome'),
    url(r'^add_visitor/',views.add_visitor, name='add_visitor'),
    url(r'^ajax/add_visitor/$', views.add_visitor, name='add_visitor'),
    url(r'^edit_visitor/(?P<Id_number>\d+)/$',views.edit_visitor, name='edit_visitor'),
    url(r'viewReport/',views.viewReport, name='viewReport'),
    url(r'Attend/',views.Attend, name='Attend'),
    url('<id>/delete$',views.visitor_delete, name='visitor_delete'),
    # url(r'check/',views.check,name='check'),
    url(r'fingerPrint/',views.fingerPrint, name='fingerPrint'),
    url(r'^searchbar/', views.searchbar, name='searchbar'),
    url(r'rfidScan/', views.rfidScan, name='rfidScan'),
    url(r'faceRecognation/', views.faceRecognation, name='faceRecognation'),
    url(r'ScanEquip/', views.ScanEquip, name='ScanEquip'),
    url(r'RegisterEqipment/', views.RegisterEqipment, name='RegisterEqipment'), 
    url(r'borcodeRead/', views.borcodeRead, name='borcodeRead'),
    # url(r'updateVisitor/<str:pk>/',views.updateVisitor,name='updateVisitor')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
