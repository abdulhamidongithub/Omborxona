from django.db import models
from userapp.models import Sotuvchi
from asosiyapp.models import Mahsulot, Mijoz

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField(default=1)
    jami = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    sana = models.DateTimeField(auto_now_add=True, null=True)
    nasiya = models.PositiveSmallIntegerField(default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)


