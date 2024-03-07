#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Etudiant, Cours, Absence

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'absences/liste_etudiants.html', {'etudiants': etudiants})

def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'absences/liste_cours.html', {'cours': cours})

def enregistrer_absence(request):
    if request.method == 'POST':
        # Traitement du formulaire d'enregistrement d'absence
        pass
    else:
        etudiants = Etudiant.objects.all()
        cours = Cours.objects.all()
        return render(request, 'absences/enregistrer_absence.html', {'etudiants': etudiants, 'cours': cours})
