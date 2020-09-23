from django.shortcuts import render
from cashPayment.models import cashPayment
from cardPayment.models import cardPayment
from django.db.models import Sum

def paymentReport(request):
    return render(request, "PaymentReport.html", {'totcash':cashPayment.objects.aggregate(Sum('Net_amount')), 'totcard':cardPayment.objects.aggregate(Sum('Amount'))})