from django.shortcuts import render, redirect
from .forms import CashForm

def cashPayment(request):

    form = CashForm()

    if request.method == 'POST':
        form = CashForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/method")

    context = {'form':form}
    return render(request, "CashPayment.html", context)

