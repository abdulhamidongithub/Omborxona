from django.db import models
from userapp.models import *

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    miqdor = models.PositiveIntegerField()
    narx = models.PositiveIntegerField()
    olchov = models.CharField(max_length=30)
    kelgan_sana = models.DateTimeField(auto_now_add=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    qarz = models.PositiveSmallIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism}, {self.nom}({self.manzil})"

