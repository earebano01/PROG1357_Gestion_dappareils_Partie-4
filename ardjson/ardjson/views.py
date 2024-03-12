from django.shortcuts import render
from .models import Objetconnecte, Capteur, Actionneur
from django.http import JsonResponse

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

def add_objView(request):
    return render(request, 'ardjson/add_obj.html')

def objconnView(request):
    objets = Objetconnecte.objects.all()
    return render(request, 'ardjson/objconn.html', {'objets': objets})

def save_data_view(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        type = request.POST.get('type')
        typemesure = request.POST.get('typemesure')
        device_id = request.POST.get('deviceid')
        temperature = request.POST.get('temperature')
        humidity = request.POST.get('humidity')
        sound = request.POST.get('sound')
        distance = request.POST.get('distance')
        lumiere = request.POST.get('lumiere')
        date = request.POST.get('date')
        time = request.POST.get('time')

        objet = Objetconnecte.objects.create(
            nom=nom,
            device_id=device_id,
            type=type,
            typemesure=typemesure
        )

        capteur = Capteur.objects.create(
            objet=objet,
            status="Actif",
            temperature=temperature,
            humidite=humidity,
            son=sound,
            distance=distance,
            lumiere=lumiere,
            formatted_date=date,
            formatted_time=time
        )

        actionneur = Actionneur.objects.create(
            objet=objet,
            status="Actif",
            formatted_date=date,
            formatted_time=time
        )

        return JsonResponse({'message': 'Data saved successfully'})
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
