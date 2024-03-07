#from django.db import models

# Create your models here.


from django.db import models
from django.shortcuts import render

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.nom} - {self.date}"

class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    justifiee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.etudiant} - {self.cours}"
