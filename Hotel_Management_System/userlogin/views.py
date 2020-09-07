from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer , Admin
from .models import generateRandomeNum
from django.contrib.auth.models import auth
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def admin(request):
    return render(request, 'Dashboard.html')

# login function
def vertifyLogin(request):
    
    Email = request.POST['loginEmail']
    Password = request.POST['loginPw']

    print(Password)

    customer = Customer()
    admin = Admin()

    customer = auth.authenticate(email=Email, password = Password)
    print("cus checked")
    if customer is not None:
        auth.login(request, customer)
        print("Customer")
        return redirect("admin")
        
    else:
        admin = auth.authenticate(adminid=Email, password = Password)
        print("add checked")
        if admin is not None:
            auth.login(request, admin)
            print("Customer")
            return redirect('admin')

    print("function skiped")
    return render(request, 'login.html')

# Signup function
def signUp(request):

    rand = generateRandomeNum() 


    custId = 'CUS' + rand.fiveNums()
    print("custId" + custId)
    Email = request.POST['signEmail']
    Password = request.POST['signPW']
    ConPw = request.POST['signConfermPw']
    fname = request.POST['signFname']
    lname = request.POST['signLname']

    if ConPw != Password:
        return render(request, 'login.html')

    elif Customer.objects.filter(email=Email).exists:
        return render(request, 'login.html')

    elif Customer.objects.filter(cusid=custId).exists:
        return render(request, 'login.html')

    else:
        customer = Customer(cusid=custId, email=Email,
                            password=Password, f_name=fname, l_name=lname)
        customer.save()
        print("Saved Customer")
        return render(request, 'index.html')


    



