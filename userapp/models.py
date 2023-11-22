from django.contrib.auth.models import AbstractUser
from django.db import models

class Ombor(AbstractUser):
    ism = models.CharField(max_length=50, blank=True)
    nom = models.CharField(max_length=50, blank=True)
    manzil = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return f'{self.ism}, {self.nom}({self.manzil})'
