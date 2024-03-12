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

def add_objView(request):
    return render(request, 'ardjson/add_obj.html')

def objconnView(request):
    objets = Objetconnecte.objects.all()
    return render(request, 'ardjson/objconn.html', {'objets': objets})

# from django.shortcuts import render
# from .models import Objetconnecte, Capteur, Actionneur

# def home(request):
#     return render(request, 'ardjson/intro.html')

# def objconnView(request):
#     objets = Objetconnecte.objects.all()
#     capteurs = Capteur.objects.all()
#     actionneurs = Actionneur.objects.all()

#     combined_data = []

#     for objet in objets:
#         obj_dict = {
#             'nom': objet.nom,
#             'device_id': objet.device_id,
#             'type': objet.type,
#             'typemesure': objet.typemesure,
#             'typeaction': objet.typeaction,
#             'capteur': None,
#             'actionneur': None,
#         }

#         # Find corresponding Capteur (if exists)
#         capteur = capteurs.filter(objet=objet).first()
#         if capteur:
#             obj_dict['capteur'] = {
#                 'status': capteur.status,
#                 'temperature': capteur.temperature,
#                 'humidite': capteur.humidite,
#                 'son': capteur.son,
#                 'distance': capteur.distance,
#                 'lumiere': capteur.lumiere,
#                 'formatted_date': capteur.formatted_date,
#                 'formatted_time': capteur.formatted_time,
#             }

#         # Find corresponding Actionneur (if exists)
#         actionneur = actionneurs.filter(objet=objet).first()
#         if actionneur:
#             obj_dict['actionneur'] = {
#                 'status': actionneur.status,
#                 'formatted_date': actionneur.formatted_date,
#                 'formatted_time': actionneur.formatted_time,
#             }

#         combined_data.append(obj_dict)

#     return render(request, 'ardjson/objconn.html', {'objets': combined_data})

# def soundView(request):
#     return render(request, 'ardjson/sound.html')

# def photoresistanceView(request):
#     return render(request, 'ardjson/photoresistance.html')

# def dht11View(request):
#     return render(request, 'ardjson/dht11.html')

# def add_objView(request):
#     return render(request, 'ardjson/add_obj.html')
