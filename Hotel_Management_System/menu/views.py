from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Project
from .forms import MenuBackendForm,promoBackendForm
from promotions.models import Promo
from cart.models import shopCart
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template


def home(request):
    projects = Project.objects.all()
    return render(request, 'menu/menu.html', {'projects':projects})



def customize(request, food):
    food = get_object_or_404(Project, pk=food)
    return render(request, 'menu/customize.html',{'food':food})



def menuBackCreate(request):

    form = MenuBackendForm()

    if request.method == 'POST':

        form = MenuBackendForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu Item successfully added")
            return redirect('/menuBackend/')
        else:
            form = MenuBackendForm()

    return render(request, 'menu/menuBackendCreate.html',{'form':form})



def menuBackUpdate(request, pk):

    projects = Project.objects.get(id=pk)
    form = MenuBackendForm(instance=projects)

    if request.method == 'POST':

        form = MenuBackendForm(request.POST, request.FILES, instance=projects)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu Item successfully updated")
            return redirect('/menuBackend/')

    return render(request, 'menu/menuBackendUpdate.html',{'form':form})



def menuBackDelete(request, pk):

    projects = Project.objects.get(id=pk)

    if request.method == 'POST':
        projects.delete()
        messages.success(request, "Menu Item successfully deleted")
        return redirect('/menuBackend/')

    return render(request, 'menu/menuBackendDelete.html',{'item':projects})


def menuBack(request):

    projects = Project.objects.all()
    promos = Promo.objects.all()
    cart = shopCart.objects.all()
    return render(request, 'menu/menuBackend.html',{'projects':projects,'promos':promos,'cart':cart})



def promoBackCreate(request):

    form = promoBackendForm()

    if request.method == 'POST':

        form = promoBackendForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Promotion Item successfully added")
            return redirect('/menuBackend/')

    return render(request, 'menu/promoBackendCreate.html',{'form':form})




def promoBackUpdate(request, pk):

    promos = Promo.objects.get(id=pk)
    form = promoBackendForm(instance=promos)

    if request.method == 'POST':

        form = promoBackendForm(request.POST, request.FILES, instance=promos)
        if form.is_valid():
            form.save()
            messages.success(request, "Promotion Item successfully updated")
            return redirect('/menuBackend/')

    return render(request, 'menu/promoBackendUpdate.html',{'form':form})



def promoBackDelete(request, pk):

    promos = Promo.objects.get(id=pk)

    if request.method == 'POST':
        promos.delete()
        messages.success(request, "Promotion Item successfully deleted")
        return redirect('/menuBackend/')

    return render(request, 'menu/promoBackendDelete.html',{'item':promos})


@login_required(login_url='/login')
def deletefromcartback(request, id):
    shopCart.objects.filter(id=id).delete()
    messages.success(request, "Item deleted from the cart")
    return redirect("/menuBackend/")


def getPdfPage(request):
    projects = Project.objects.all()
    promos = Promo.objects.all()
    cart = shopCart.objects.all()
    data = {'projects':projects,'promos':promos,'cart':cart}
    template = get_template("menu/pdfFoods.html")
    data_d = template.render(data)
    response = BytesIO()

    pdfpage = pisa.pisaDocument(BytesIO(data_d.encode("UTF-8")),response)
    return HttpResponse(response.getvalue(),content_type="application/pdf")
