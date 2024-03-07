from django.shortcuts import render
from .models import Objetconnecte

def home(request):
    return render(request, 'ardjson/intro.html')

def objconnView(request):
    return render(request, 'ardjson/objconn.html')

def soundView(request):
    return render(request, 'ardjson/sound.html')

def photoresistanceView(request):
    return render(request, 'ardjson/photoresistance.html')

def dht11View(request):
    return render(request, 'ardjson/dht11.html')

def objconnView(request):
    objets = Objetconnecte.objects.all()
    return render(request, 'ardjson/objconn.html', {'objets': objets})

