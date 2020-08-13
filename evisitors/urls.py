"""evisitors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from evisitorsproject.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('evisitorsproject.urls')),
    url(r'^viewreport/$',add_visitor),
    url(r'^searchbar/$',searchbar),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    # url(r'^add_visitor/(?P<>\d+)/delete$','evisitorsproject.views.visitor_delete', name='visitor_delete'),
    #  url(r'delete_visitor/<int:id>/delete/',visitor_delete_view, name='viewReport'),
    # url(r'^add_visitor/(?P<id>\d+)/delete$',evisitorsproject.views.delete_visitor, name='delete_visitor'),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^logout/$',views.logout,{"next_page":'/'})
]


