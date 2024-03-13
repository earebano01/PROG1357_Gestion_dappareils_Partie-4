from django.shortcuts import render
from .models import Objetconnecte, Capteur, Actionneur
from django.http import JsonResponse
import json

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
        try:
            form_data = json.loads(request.body.decode('utf-8'))
            print('Données du formulaire reçues :', form_data)
            
            objet = Objetconnecte.objects.create(
                nom=form_data.get('nom'),
                device_id=form_data.get('Device ID'),
                type=form_data.get('type'),
                typemesure=form_data.get('typemesure')
            )

            capteur = Capteur.objects.create(
                objet=objet,
                status=form_data.get('Status'),
                temperature=form_data.get('Temperature'),
                humidite=form_data.get('Humidite'),
                son=form_data.get('Son'),
                distance=form_data.get('Distance'),
                lumiere=form_data.get('Lumiere'),
                formatted_date=form_data.get('Date'),
                formatted_time=form_data.get('Time')
            )

            actionneur = Actionneur.objects.create(
                objet=objet,
                status=form_data.get('Status'),
                formatted_date=form_data.get('Date'),
                formatted_time=form_data.get('Time')
            )

            print('Données enregistrées avec succès')
            return JsonResponse({'message': 'Données enregistrées avec succès'})
        except Exception as e:
            print('Échec de l\'enregistrement des données :', e)
            return JsonResponse({'erreur': 'Échec de l\'enregistrement des données'}, status=500)
    else:
        return JsonResponse({'erreur': 'Méthode non autorisée'}, status=405)
