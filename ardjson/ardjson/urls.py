from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.jsonView, name='json'),    
    path('sound/', views.soundView, name='sound'),
    path('photoresistance/', views.photoresistanceView, name='photoresistance'),    
    path('dht11/', views.dht11View, name='dht11'),
]

