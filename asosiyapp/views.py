from django.shortcuts import render, redirect
from django.views import View
from .models import *


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class MahsulotlarView(View):
    def get(self, request):
        data = {
            'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user)
        }
        return render(request, 'products.html', data)

    def post(self, request):
        Mahsulot.objects.create(
            nom = request.POST.get('pr_name'),
            brend = request.POST.get('pr_brand'),
            miqdor = request.POST.get('pr_amount'),
            narx = request.POST.get('pr_price'),
            olchov = request.POST.get('pr_olchov'),
            sotuvchi = Sotuvchi.objects.filter(user=request.user)[0]
        )
        return redirect('mahsulotlar')

class ProductDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            hozirgi_sotuvchi = Sotuvchi.objects.get(user=request.user)
            m = Mahsulot.objects.get(id=pk)
            if m.sotuvchi == hozirgi_sotuvchi and request.user.is_staff:
                m.delete()
            return redirect('mahsulotlar')
        return redirect('login')

class MahsulotUpdateView(View):
    def get(self, request, pk):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and hozirgi_ombor == product.sotuvchi:
            data = {
                'mahsulot':product
            }
            return render(request, 'product_update.html', data)
        else:
            return redirect('/bolimlar/mahsulotlar/')

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            nom = request.POST.get('name'),
            brend = request.POST.get('brand_name'),
            narx = request.POST.get('price'),
            miqdor = request.POST.get('amount'),
            olchov = request.POST.get('olchov')
        )
        return redirect('/bolimlar/mahsulotlar/')

