from django.shortcuts import render, get_object_or_404
from .models import Promo

def promo(request):
    promos = Promo.objects.all()
    return render(request, 'promotions/promotions.html', {'promos':promos})
