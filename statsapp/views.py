from django.shortcuts import render
from django.views import View
from .models import *
from userapp.models import *
from asosiyapp.models import *

class StatistikaView(View):
    def get(self, request):
        statistikalar = Statistika.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi = request.GET.get('soz')
        if qidiruv_sozi is not None:
            statistikalar = statistikalar.filter(mahsulot__nom__contains=
            qidiruv_sozi)|statistikalar.filter(mahsulot__brend__contains=
            qidiruv_sozi)|statistikalar.filter(mijoz__nom__contains=qidiruv_sozi)|statistikalar.filter(
                mijoz__ism__contains=qidiruv_sozi)
        data = {
            'stats' : statistikalar
        }
        return render(request, 'stats.html', data)


