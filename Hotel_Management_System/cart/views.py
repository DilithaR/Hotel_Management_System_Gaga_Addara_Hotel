from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import shopCart,shopCartForm


def index(request):
    return HttpResponse("Order Page")

@login_required(login_url='/login')
def addtocart(request,id):
    #return HttpResponse(str(id))
    current_user = request.user

    checkitem = shopCart.objects.filter(item_id=id)
    if checkitem:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = shopCartForm(request.POST)
        if form.is_valid():
            if control == 1: #update cart
                data = shopCart.objects.get(item_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else: #insert to cart
                data = shopCart()
                data.user_id = current_user.id
                data.item_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Menu Item added to Cart")
        return redirect('/menu')


def shopcart(request):
    current_user = request.user
    shopcart = shopCart.objects.filter(user_id=current_user.id)
    total = 0
    for a in shopcart:
        total = total + (a.item.price) * a.quantity

    context = {
        'shopcart':shopcart,
        'total':total,
    }

    return render(request, 'cart/cart_items.html', context)



@login_required(login_url='/login')
def deletefromcart(request,id):
    shopCart.objects.filter(id=id).delete()
    messages.success(request, "Item deleted from your cart")
    return HttpResponseRedirect("/shopcart")
