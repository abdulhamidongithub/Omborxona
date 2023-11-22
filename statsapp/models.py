from django.db import models
from userapp.models import Ombor
from asosiyapp.models import Mahsulot, Mijoz

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField(default=1)
    summa = models.PositiveSmallIntegerField()
    tolangan_summa = models.PositiveSmallIntegerField()
    sana = models.DateTimeField(auto_now_add=True, null=True)
    nasiya = models.PositiveSmallIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)


