from django.shortcuts import render, redirect
from cardPayment.models import cardPayment

def cardDashboard(request):
    queryset = cardPayment.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "CardDashboard.html", context)

def delete_card(request, id):
    cardPayment.objects.filter(id=id).delete()

    items = cardPayment.objects.all()

    context = {
        'items': items
    }
    return render(request, "DeletePayment.html", context)
