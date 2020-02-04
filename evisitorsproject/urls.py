from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.welcome, name = 'welcome'),
    # url('',views.add_visitor, name='add_visitor'),
    url('',views.fingerPrint, name='fingerPrint'),
#     url('', views.post_list, name='post_list'),
#     url('post/<int:pk>/', views.post_detail, name='post_detail'),
]