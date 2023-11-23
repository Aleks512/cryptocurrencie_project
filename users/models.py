# Dans votre fichier models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    date_naissance = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)  # Ajoutez cette ligne pour inclure l'e-mail
