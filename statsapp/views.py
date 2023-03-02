from django.shortcuts import render, redirect
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
            'stats' : statistikalar,
            'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user),
            'mijozlar':Mijoz.objects.filter(sotuvchi__user=request.user)
        }
        return render(request, 'stats.html', data)

    def post(self, request):
        Statistika.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get('pr')),
            mijoz = Mijoz.objects.get(id=request.POST.get('m')),
            miqdor = request.POST.get('miqdor'),
            jami = request.POST.get('summa'),
            tolandi = request.POST.get('tolandi'),
            nasiya = request.POST.get('nasiya'),
            sotuvchi = Sotuvchi.objects.get(user=request.user)
        )
        return redirect('/stats/')
