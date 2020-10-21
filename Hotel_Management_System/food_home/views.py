from django.shortcuts import render
from promotions.models import Promo

def homepage(request):
    promos = Promo.objects.all()
    return render(request, 'food_home/food_home.html',{'promos':promos})
