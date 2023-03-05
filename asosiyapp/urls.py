from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('clientlar/', ClientView.as_view(), name='clientlar'),
    path('pr_delete/<int:pk>/', ProductDeleteView.as_view(), name='m-ochirish'),
    path('cl_delete/<int:pk>/', ClientDeleteView.as_view(), name='cl-ochirish'),
    path('pr_update/<int:pk>/', MahsulotUpdateView.as_view(), name='m-update'),
]



