from django.shortcuts import render
from cashPayment.models import cashPayment
from cardPayment.models import cardPayment
from django.db.models import Sum

def paymentReport(request):
    
    totcash = 0.0
    totcard = 0.0

    queryset = cashPayment.objects.all()
    queryset2 = cardPayment.objects.all()

    for a in queryset:
        totcash = totcash + a.Net_amount

    for b in queryset2:
        totcard = totcard + b.Amount

    total = totcash + totcard

    context = {
        'totcash': totcash, 'totcard': totcard, 'total': total
    }

    return render(request, "PaymentReport.html", context)