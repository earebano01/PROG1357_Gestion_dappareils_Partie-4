from django.shortcuts import render

def home(request):
    return render(request, 'ardjson/intro.html')

def jsonView(request):
    return render(request, 'ardjson/json.html')

def soundView(request):
    return render(request, 'ardjson/sound.html')

def photoresistanceView(request):
    return render(request, 'ardjson/photoresistance.html')

def dht11View(request):
    return render(request, 'ardjson/dht11.html')
